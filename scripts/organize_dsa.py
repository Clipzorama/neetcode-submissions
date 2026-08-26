#!/usr/bin/env python3
"""Create an incrementally organized view of NeetCode submissions."""

from __future__ import annotations

import argparse
import filecmp
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import sys
from typing import Any

import requests


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = REPOSITORY_ROOT / "Data Structures & Algorithms"
DEFAULT_DESTINATION = REPOSITORY_ROOT / "DSA Organized"
DEFAULT_CACHE_FILE = REPOSITORY_ROOT / "scripts/problem_metadata.json"

CATALOG_URL = (
    "https://raw.githubusercontent.com/neetcode-gh/leetcode/"
    "main/.problemSiteData.json"
)
PROBLEM_URL = "https://neetcode.io/problems/{slug}/question"
DIFFICULTIES = {"Easy", "Medium", "Hard"}

# NeetCode roadmap patterns converted into this repository's folder names.
# This is intentionally a category mapping, never a per-problem mapping.
PATTERN_CATEGORIES = {
    "Arrays & Hashing": "Arrays-and-Hashing",
    "Two Pointers": "Two-Pointers",
    "Sliding Window": "Sliding-Window",
    "Stack": "Stack",
    "Queue": "Queue",
    "Binary Search": "Binary-Search",
    "Linked List": "Linked-List",
    "Trees": "Trees",
    "Tries": "Tries",
    "Heap / Priority Queue": "Heap",
    "Backtracking": "Backtracking",
    "Graphs": "Graphs",
    "Advanced Graphs": "Advanced-Graphs",
    "1-D Dynamic Programming": "Dynamic-Programming",
    "2-D Dynamic Programming": "Dynamic-Programming",
    "Greedy": "Greedy",
    "Intervals": "Intervals",
    "Math & Geometry": "Math-and-Geometry",
    "Bit Manipulation": "Bit-Manipulation",
}

# Used only when a problem is newer than the official roadmap catalog. More
# specific algorithm tags are checked before broad data-structure tags.
TOPIC_CATEGORIES = [
    ({"two pointers"}, "Two-Pointers"),
    ({"sliding window"}, "Sliding-Window"),
    ({"binary search"}, "Binary-Search"),
    ({"monotonic stack", "stack"}, "Stack"),
    ({"queue", "monotonic queue"}, "Queue"),
    ({"heap (priority queue)", "priority queue", "heap"}, "Heap"),
    ({"backtracking"}, "Backtracking"),
    ({"trie"}, "Tries"),
    ({"linked list", "doubly-linked list"}, "Linked-List"),
    ({"binary tree", "binary search tree", "tree"}, "Trees"),
    (
        {"shortest path", "minimum spanning tree", "strongly connected component"},
        "Advanced-Graphs",
    ),
    (
        {
            "graph",
            "depth-first search",
            "breadth-first search",
            "union find",
            "topological sort",
        },
        "Graphs",
    ),
    ({"dynamic programming", "memoization"}, "Dynamic-Programming"),
    ({"greedy"}, "Greedy"),
    ({"intervals", "interval"}, "Intervals"),
    ({"bit manipulation", "bitmask"}, "Bit-Manipulation"),
    ({"matrix"}, "Matrix"),
    ({"math", "geometry", "number theory", "combinatorics"}, "Math-and-Geometry"),
    ({"array", "hash table", "string", "sorting", "counting"}, "Arrays-and-Hashing"),
]


class OrganizerError(RuntimeError):
    """A safe, user-actionable organizer failure."""


class ScriptJSONParser(HTMLParser):
    """Extract the contents of a script element by id."""

    def __init__(self, script_id: str) -> None:
        super().__init__()
        self.script_id = script_id
        self.capturing = False
        self.parts: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag == "script" and dict(attrs).get("id") == self.script_id:
            self.capturing = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self.capturing:
            self.capturing = False

    def handle_data(self, data: str) -> None:
        if self.capturing:
            self.parts.append(data)


def normalize_slug(value: str) -> str:
    return value.strip().strip("/").casefold()


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def validate_metadata(slug: str, metadata: Any) -> dict[str, str]:
    if not isinstance(metadata, dict):
        raise OrganizerError(f"Cache entry for {slug!r} is not an object.")

    difficulty = metadata.get("difficulty")
    category = metadata.get("category", metadata.get("topic"))
    if difficulty not in DIFFICULTIES:
        raise OrganizerError(
            f"Cache entry for {slug!r} has invalid difficulty {difficulty!r}."
        )
    if not isinstance(category, str) or not re.fullmatch(r"[A-Za-z0-9-]+", category):
        raise OrganizerError(
            f"Cache entry for {slug!r} has invalid category {category!r}."
        )

    result = {"difficulty": difficulty, "category": category}
    for key in ("title", "source"):
        if isinstance(metadata.get(key), str):
            result[key] = metadata[key]
    return result


def load_cache(cache_file: Path) -> dict[str, dict[str, str]]:
    if not cache_file.exists():
        return {}
    try:
        raw = json.loads(cache_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise OrganizerError(f"Could not read metadata cache {cache_file}: {error}") from error
    if not isinstance(raw, dict):
        raise OrganizerError(f"Metadata cache {cache_file} must contain a JSON object.")
    return {str(slug): validate_metadata(str(slug), item) for slug, item in raw.items()}


def save_cache(cache_file: Path, cache: dict[str, dict[str, str]]) -> None:
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(cache, indent=2, sort_keys=True) + "\n"
    if cache_file.exists() and cache_file.read_text(encoding="utf-8") == serialized:
        return
    temporary = cache_file.with_suffix(cache_file.suffix + ".tmp")
    temporary.write_text(serialized, encoding="utf-8")
    temporary.replace(cache_file)


def existing_locations(destination: Path, slug: str) -> list[Path]:
    if not destination.is_dir():
        return []
    locations: list[Path] = []
    for first_level in destination.iterdir():
        if not first_level.is_dir():
            continue
        if first_level.name in DIFFICULTIES:
            for category in first_level.iterdir():
                candidate = category / slug
                if category.is_dir() and candidate.is_dir():
                    locations.append(candidate)
        else:
            candidate = first_level / slug
            if candidate.is_dir():
                locations.append(candidate)
    return sorted(locations)


def is_classified_location(destination: Path, location: Path) -> bool:
    relative_parts = location.relative_to(destination).parts
    return len(relative_parts) == 3 and relative_parts[0] in DIFFICULTIES


def learn_existing_metadata(
    source: Path, destination: Path, cache: dict[str, dict[str, str]]
) -> int:
    learned = 0
    for problem_path in sorted(path for path in source.iterdir() if path.is_dir()):
        slug = problem_path.name
        locations = existing_locations(destination, slug)
        classified = [
            location
            for location in locations
            if is_classified_location(destination, location)
        ]
        if len(classified) > 1:
            rendered = ", ".join(
                str(path.relative_to(destination)) for path in classified
            )
            raise OrganizerError(f"{slug!r} exists in multiple organized locations: {rendered}")
        if not classified:
            continue

        location = classified[0]
        discovered = {
            "difficulty": location.parent.parent.name,
            "category": location.parent.name,
            "source": "existing-organization",
        }
        discovered = validate_metadata(slug, discovered)
        if slug in cache:
            expected = cache[slug]
            if (
                expected["difficulty"] != discovered["difficulty"]
                or expected["category"] != discovered["category"]
            ):
                raise OrganizerError(
                    f"Cache says {slug!r} belongs in "
                    f"{expected['difficulty']}/{expected['category']}, but it already exists "
                    f"in {discovered['difficulty']}/{discovered['category']}."
                )
        else:
            cache[slug] = discovered
            learned += 1
    return learned


def request_json(session: requests.Session, url: str) -> Any:
    response = session.get(url, timeout=25)
    response.raise_for_status()
    return response.json()


def fetch_catalog(session: requests.Session) -> list[dict[str, Any]]:
    try:
        payload = request_json(session, CATALOG_URL)
    except (requests.RequestException, ValueError) as error:
        raise OrganizerError(
            f"Could not fetch NeetCode's official metadata catalog: {error}"
        ) from error
    if not isinstance(payload, list):
        raise OrganizerError("NeetCode's official metadata catalog had an unexpected format.")
    return [row for row in payload if isinstance(row, dict)]


def extract_problem_state(html: str, slug: str) -> dict[str, Any]:
    parser = ScriptJSONParser("ng-state")
    parser.feed(html)
    if not parser.parts:
        raise OrganizerError(
            f"NeetCode page for {slug!r} did not contain structured ng-state JSON."
        )
    try:
        payload = json.loads("".join(parser.parts))
    except json.JSONDecodeError as error:
        raise OrganizerError(f"NeetCode returned invalid structured JSON for {slug!r}.") from error

    problem = payload.get(f"problem-{slug}") if isinstance(payload, dict) else None
    if not isinstance(problem, dict):
        raise OrganizerError(f"NeetCode's structured JSON did not contain problem {slug!r}.")
    if normalize_slug(str(problem.get("id", ""))) != normalize_slug(slug):
        raise OrganizerError(f"NeetCode returned a mismatched problem for {slug!r}.")
    return problem


def fetch_problem_state(session: requests.Session, slug: str) -> dict[str, Any]:
    try:
        response = session.get(
            PROBLEM_URL.format(slug=slug),
            timeout=25,
            headers={"User-Agent": "NeetCode-Submission-Organizer/2.0"},
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise OrganizerError(f"Could not fetch NeetCode metadata for {slug!r}: {error}") from error
    return extract_problem_state(response.text, slug)


def catalog_indexes(
    catalog: list[dict[str, Any]],
) -> tuple[dict[str, dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    by_slug: dict[str, dict[str, Any]] = {}
    by_title: dict[str, list[dict[str, Any]]] = {}
    for row in catalog:
        slug = normalize_slug(str(row.get("link", "")))
        title = normalize_title(str(row.get("problem", "")))
        if slug:
            by_slug[slug] = row
        if title:
            by_title.setdefault(title, []).append(row)
    return by_slug, by_title


def metadata_from_catalog_row(
    slug: str, row: dict[str, Any], source: str
) -> dict[str, str]:
    difficulty = row.get("difficulty")
    pattern = row.get("pattern")
    category = PATTERN_CATEGORIES.get(pattern)
    if difficulty not in DIFFICULTIES or category is None:
        raise OrganizerError(
            f"Official catalog metadata for {slug!r} has unsupported values: "
            f"difficulty={difficulty!r}, pattern={pattern!r}."
        )
    return validate_metadata(
        slug,
        {
            "difficulty": difficulty,
            "category": category,
            "title": str(row.get("problem", slug)),
            "source": source,
        },
    )


def category_from_topics(topics: list[str]) -> str | None:
    normalized = {topic.casefold().strip() for topic in topics}
    for aliases, category in TOPIC_CATEGORIES:
        if normalized.intersection(aliases):
            return category
    return None


def discover_metadata(
    session: requests.Session,
    slug: str,
    by_slug: dict[str, dict[str, Any]],
    by_title: dict[str, list[dict[str, Any]]],
) -> dict[str, str]:
    exact = by_slug.get(normalize_slug(slug))
    if exact is not None:
        return metadata_from_catalog_row(slug, exact, "neetcode-official-catalog")

    state = fetch_problem_state(session, slug)
    title = str(state.get("name", "")).strip()
    difficulty = state.get("difficulty")
    topics = state.get("topics")
    if not title or difficulty not in DIFFICULTIES or not isinstance(topics, list):
        raise OrganizerError(f"NeetCode returned incomplete structured metadata for {slug!r}.")
    clean_topics = [str(topic) for topic in topics if isinstance(topic, str)]

    title_matches = by_title.get(normalize_title(title), [])
    compatible = [row for row in title_matches if row.get("difficulty") == difficulty]
    if len(compatible) == 1:
        return metadata_from_catalog_row(
            slug, compatible[0], "neetcode-catalog-title-match"
        )

    category = category_from_topics(clean_topics)
    if category is None:
        raise OrganizerError(
            f"No category rule matched NeetCode topics for {slug!r}: {clean_topics}. "
            "The source submission was left untouched."
        )
    return validate_metadata(
        slug,
        {
            "difficulty": difficulty,
            "category": category,
            "title": title,
            "source": "neetcode-page-structured-data",
        },
    )


def files_to_copy(source_problem: Path, target_problem: Path) -> list[tuple[Path, Path]]:
    copies: list[tuple[Path, Path]] = []
    for source_file in sorted(path for path in source_problem.rglob("*") if path.is_file()):
        target_file = target_problem / source_file.relative_to(source_problem)
        if not target_file.exists() or not filecmp.cmp(source_file, target_file, shallow=False):
            copies.append((source_file, target_file))
    return copies


def validate_legacy_migrations(legacy_locations: list[Path], target: Path) -> None:
    files_by_relative_path: dict[Path, Path] = {}
    if target.is_dir():
        for target_file in (path for path in target.rglob("*") if path.is_file()):
            files_by_relative_path[target_file.relative_to(target)] = target_file

    for legacy in legacy_locations:
        for legacy_file in (path for path in legacy.rglob("*") if path.is_file()):
            relative = legacy_file.relative_to(legacy)
            existing = files_by_relative_path.get(relative)
            if existing is not None and not filecmp.cmp(
                legacy_file, existing, shallow=False
            ):
                raise OrganizerError(
                    f"Cannot migrate {legacy}: {relative} conflicts with {existing}. "
                    "No files were changed."
                )
            files_by_relative_path[relative] = legacy_file


def migrate_legacy_locations(
    legacy_locations: list[Path], target: Path, destination: Path
) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for legacy in legacy_locations:
        for legacy_file in (path for path in legacy.rglob("*") if path.is_file()):
            target_file = target / legacy_file.relative_to(legacy)
            if not target_file.exists():
                target_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(legacy_file, target_file)
        shutil.rmtree(legacy)
        parent = legacy.parent
        if parent != destination and parent.is_dir() and not any(parent.iterdir()):
            parent.rmdir()


def display_path(path: Path) -> Path:
    try:
        return path.relative_to(REPOSITORY_ROOT)
    except ValueError:
        return path


def organize(
    source: Path,
    destination: Path,
    cache_file: Path,
    *,
    dry_run: bool = False,
    session: requests.Session | None = None,
) -> int:
    if not source.is_dir():
        raise OrganizerError(f"Source folder does not exist: {source}")

    cache = load_cache(cache_file)
    learned = learn_existing_metadata(source, destination, cache)
    problems = sorted(path for path in source.iterdir() if path.is_dir())
    unknown = [path.name for path in problems if path.name not in cache]

    if unknown:
        active_session = session or requests.Session()
        catalog = fetch_catalog(active_session)
        by_slug, by_title = catalog_indexes(catalog)
        for slug in unknown:
            print(f"Discovering metadata for {slug}...")
            cache[slug] = discover_metadata(active_session, slug, by_slug, by_title)

    migration_plan: list[tuple[list[Path], Path, str]] = []
    copy_plan: list[tuple[Path, Path, str]] = []
    for problem_path in problems:
        slug = problem_path.name
        metadata = cache[slug]
        target = destination / metadata["difficulty"] / metadata["category"] / slug
        locations = existing_locations(destination, slug)
        classified_elsewhere = [
            location
            for location in locations
            if location != target and is_classified_location(destination, location)
        ]
        if classified_elsewhere:
            rendered = ", ".join(
                str(path.relative_to(destination)) for path in classified_elsewhere
            )
            raise OrganizerError(
                f"Refusing to duplicate {slug!r}: it already exists at {rendered}, "
                f"but metadata points to {target.relative_to(destination)}."
            )
        
        legacy_locations = [
            location
            for location in locations
            if not is_classified_location(destination, location)
        ]
        if legacy_locations:
            validate_legacy_migrations(legacy_locations, target)
            migration_plan.append((legacy_locations, target, slug))
        for source_file, target_file in files_to_copy(problem_path, target):
            copy_plan.append((source_file, target_file, slug))

    if dry_run:
        print(f"Dry run: {learned + len(unknown)} metadata entrie(s) would be cached.")
        if not migration_plan and not copy_plan:
            print("Dry run: organized submissions are already synchronized.")
        for legacy_locations, target, _ in migration_plan:
            for legacy in legacy_locations:
                print(
                    f"Would migrate {display_path(legacy)} -> "
                    f"{display_path(target)}"
                )
        for source_file, target_file, _ in copy_plan:
            print(
                f"Would copy {display_path(source_file)} -> "
                f"{display_path(target_file)}"
            )
        return len(copy_plan)

    for legacy_locations, target, slug in migration_plan:
        migrate_legacy_locations(legacy_locations, target, destination)
        print(
            f"Migrated {slug} -> "
            f"{target.relative_to(destination).parent}"
        )

    for source_file, target_file, slug in copy_plan:
        target_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, target_file)
        metadata = cache[slug]
        print(f"Copied {slug} -> {metadata['difficulty']}/{metadata['category']}")

    save_cache(cache_file, cache)
    if not copy_plan:
        print("Organized submissions are already synchronized.")
    print(f"Metadata cache contains {len(cache)} problem(s).")
    return len(copy_plan)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show cache and copy operations without changing any files",
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help=argparse.SUPPRESS)
    parser.add_argument(
        "--destination", type=Path, default=DEFAULT_DESTINATION, help=argparse.SUPPRESS
    )
    parser.add_argument(
        "--cache-file", type=Path, default=DEFAULT_CACHE_FILE, help=argparse.SUPPRESS
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        organize(
            args.source.resolve(),
            args.destination.resolve(),
            args.cache_file.resolve(),
            dry_run=args.dry_run,
        )
    except OrganizerError as error:
        print(f"Organizer stopped safely: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
