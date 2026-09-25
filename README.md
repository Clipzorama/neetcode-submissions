# My NeetCode & LeetCode Solutions

Hey, I'm **@Clipzorama**. This is my personal collection of solutions to **NeetCode and LeetCode** problems, written in **Python**.

I'm using this repo to keep track of my practice, get more comfortable with data structures and algorithms, and build a collection I can come back to when revisiting a problem or pattern. It also keeps my different submissions together, so I can look back at how I approached each question.

## Browse my solutions

| Folder | What's inside |
| --- | --- |
| [DSA Organized](DSA%20Organized/) | Solutions grouped by difficulty and topic—the easiest place to browse. |
| [Data Structures & Algorithms](Data%20Structures%20%26%20Algorithms/) | Original problem folders and submission history. |
| [Python Coding Interviews](Python%20Coding%20Interviews/) | My Python practice, including sorting, lambda functions, and unpacking. |

The collection includes arrays and hashing, two pointers, sliding windows, stacks, queues, binary search, greedy algorithms, graphs, and bit manipulation. I'll keep adding to it as I work through more questions.

## Why I keep this repo

- **Keep a record of my practice.** Every problem adds to the collection.
- **Recognize patterns.** Grouping solutions by topic helps me connect similar problems.
- **Revisit my approaches.** Multiple submissions give me something to compare and learn from later.
- **Build fluency in Python.** Practice the language alongside the problem-solving skills.

This is a work in progress. The solutions reflect my learning along the way, and some problems have several submissions rather than a single polished answer.

## How it's organized

```text
DSA Organized/
  Easy/
    Arrays-and-Hashing/
      is-anagram/
        submission-0.py
        submission-1.py
  Medium/
    Two-Pointers/
      three-integer-sum/
        submission-1.py

Data Structures & Algorithms/
  <problem-slug>/
    submission-0.py

Python Coding Interviews/
  <exercise-slug>/
    submission-0.py
```

NeetCode submissions sync here through its GitHub integration. A [GitHub Actions workflow](.github/workflows/organize-dsa.yml) copies DSA solutions into the organized folder by difficulty and category, while preserving the original files and submission history. It runs on relevant pushes and every six hours to catch up on missed runs.

<details>
<summary>Run the organizer locally</summary>

The organizer discovers problem metadata from NeetCode and caches classifications in [`scripts/problem_metadata.json`](scripts/problem_metadata.json).

One-time setup:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --requirement requirements-organizer.txt
```

Preview the changes:

```bash
.venv/bin/python scripts/organize_dsa.py --dry-run
```

Apply them:

```bash
.venv/bin/python scripts/organize_dsa.py
```

Run the offline tests:

```bash
.venv/bin/python -m unittest discover -s tests -v
```

</details>
