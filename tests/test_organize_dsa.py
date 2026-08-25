from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock

import requests

from scripts import organize_dsa


class FakeResponse:
    def __init__(self, *, payload=None, text=""):
        self.payload = payload
        self.text = text

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


class OrganizerTests(unittest.TestCase):
    def test_extracts_structured_problem_state(self):
        state = {
            "problem-new-problem": {
                "id": "new-problem",
                "name": "New Problem",
                "difficulty": "Medium",
                "topics": ["Array", "Sliding Window"],
            }
        }
        html = (
            '<html><script id="ng-state" type="application/json">'
            + json.dumps(state)
            + "</script></html>"
        )

        result = organize_dsa.extract_problem_state(html, "new-problem")

        self.assertEqual(result["difficulty"], "Medium")
        self.assertEqual(result["topics"], ["Array", "Sliding Window"])

    def test_specific_topic_wins_over_broad_graph_topic(self):
        category = organize_dsa.category_from_topics(["Graph", "Shortest Path"])

        self.assertEqual(category, "Advanced-Graphs")

    def test_catalog_title_matches_a_neetcode_specific_slug(self):
        catalog = [
            {
                "problem": "Two Sum",
                "link": "two-sum/",
                "difficulty": "Easy",
                "pattern": "Arrays & Hashing",
            }
        ]
        by_slug, by_title = organize_dsa.catalog_indexes(catalog)
        response = FakeResponse(
            text=(
                '<script id="ng-state" type="application/json">'
                + json.dumps(
                    {
                        "problem-two-integer-sum": {
                            "id": "two-integer-sum",
                            "name": "Two Sum",
                            "difficulty": "Easy",
                            "topics": ["Array", "Hash Table"],
                        }
                    }
                )
                + "</script>"
            )
        )
        session = Mock()
        session.get.return_value = response

        metadata = organize_dsa.discover_metadata(
            session, "two-integer-sum", by_slug, by_title
        )

        self.assertEqual(metadata["difficulty"], "Easy")
        self.assertEqual(metadata["category"], "Arrays-and-Hashing")
        self.assertEqual(metadata["source"], "neetcode-catalog-title-match")

    def test_incremental_copy_is_idempotent_and_preserves_old_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            destination = root / "organized"
            cache_file = root / "metadata.json"
            problem = source / "binary-search"
            problem.mkdir(parents=True)
            (problem / "submission-1.py").write_text("return 1\n", encoding="utf-8")
            target = destination / "Easy" / "Binary-Search" / "binary-search"
            target.mkdir(parents=True)
            (target / "submission-0.py").write_text("return 0\n", encoding="utf-8")

            first_count = organize_dsa.organize(source, destination, cache_file)
            second_count = organize_dsa.organize(source, destination, cache_file)

            self.assertEqual(first_count, 1)
            self.assertEqual(second_count, 0)
            self.assertTrue((target / "submission-0.py").exists())
            self.assertEqual(
                (target / "submission-1.py").read_text(encoding="utf-8"), "return 1\n"
            )

    def test_dry_run_does_not_create_cache_or_destination(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            destination = root / "organized"
            cache_file = root / "metadata.json"
            problem = source / "binary-search"
            problem.mkdir(parents=True)
            (problem / "submission-0.py").write_text("pass\n", encoding="utf-8")
            cache_file.write_text(
                json.dumps(
                    {
                        "binary-search": {
                            "difficulty": "Easy",
                            "category": "Binary-Search",
                        }
                    }
                ),
                encoding="utf-8",
            )
            original_cache = cache_file.read_text(encoding="utf-8")

            count = organize_dsa.organize(
                source, destination, cache_file, dry_run=True
            )

            self.assertEqual(count, 1)
            self.assertFalse(destination.exists())
            self.assertEqual(cache_file.read_text(encoding="utf-8"), original_cache)

    def test_network_failure_changes_nothing(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            destination = root / "organized"
            cache_file = root / "metadata.json"
            problem = source / "unknown-problem"
            problem.mkdir(parents=True)
            (problem / "submission-0.py").write_text("pass\n", encoding="utf-8")
            session = Mock()
            session.get.side_effect = requests.ConnectionError("offline")

            with self.assertRaises(organize_dsa.OrganizerError):
                organize_dsa.organize(
                    source, destination, cache_file, session=session
                )

            self.assertFalse(cache_file.exists())
            self.assertFalse(destination.exists())

    def test_legacy_uncategorized_location_is_migrated_without_data_loss(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            destination = root / "organized"
            cache_file = root / "metadata.json"
            source_problem = source / "new-problem"
            source_problem.mkdir(parents=True)
            (source_problem / "submission-0.py").write_text("pass\n", encoding="utf-8")
            legacy = destination / "Uncategorized" / "new-problem"
            legacy.mkdir(parents=True)
            (legacy / "submission-0.py").write_text("pass\n", encoding="utf-8")
            (legacy / "legacy-only.py").write_text("old\n", encoding="utf-8")
            cache_file.write_text(
                json.dumps(
                    {
                        "new-problem": {
                            "difficulty": "Easy",
                            "category": "Greedy",
                        }
                    }
                ),
                encoding="utf-8",
            )

            organize_dsa.organize(source, destination, cache_file)

            target = destination / "Easy" / "Greedy" / "new-problem"
            self.assertFalse(legacy.exists())
            self.assertEqual(
                (target / "submission-0.py").read_text(encoding="utf-8"), "pass\n"
            )
            self.assertEqual(
                (target / "legacy-only.py").read_text(encoding="utf-8"), "old\n"
            )

    def test_conflicting_legacy_file_stops_before_migration(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            destination = root / "organized"
            cache_file = root / "metadata.json"
            source_problem = source / "new-problem"
            source_problem.mkdir(parents=True)
            legacy = destination / "Uncategorized" / "new-problem"
            legacy.mkdir(parents=True)
            (legacy / "submission-0.py").write_text("legacy\n", encoding="utf-8")
            target = destination / "Easy" / "Greedy" / "new-problem"
            target.mkdir(parents=True)
            (target / "submission-0.py").write_text("different\n", encoding="utf-8")
            cache_file.write_text(
                json.dumps(
                    {
                        "new-problem": {
                            "difficulty": "Easy",
                            "category": "Greedy",
                        }
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaises(organize_dsa.OrganizerError):
                organize_dsa.organize(source, destination, cache_file)

            self.assertTrue(legacy.exists())
            self.assertEqual(
                (target / "submission-0.py").read_text(encoding="utf-8"),
                "different\n",
            )


if __name__ == "__main__":
    unittest.main()
