from pathlib import Path
import shutil


# Folder created automatically by NeetCode
SOURCE = Path("Data Structures & Algorithms")

# Folder that OUR script will generate
DESTINATION = Path("DSA Organized")


# Information about each problem
PROBLEMS = {
    "anagram-groups": {
        "difficulty": "Medium",
        "topic": "Arrays-and-Hashing",
    },

    "binary-search": {
        "difficulty": "Easy",
        "topic": "Binary-Search",
    },

    "concatenation-of-array": {
        "difficulty": "Easy",
        "topic": "Arrays-and-Hashing",
    },

    "duplicate-integer": {
        "difficulty": "Easy",
        "topic": "Arrays-and-Hashing",
    },

    "is-anagram": {
        "difficulty": "Easy",
        "topic": "Arrays-and-Hashing",
    },

    "is-palindrome": {
        "difficulty": "Easy",
        "topic": "Two-Pointers",
    },

    "is-subsequence": {
        "difficulty": "Easy",
        "topic": "Two-Pointers",
    },

    "longest-consecutive-sequence": {
        "difficulty": "Medium",
        "topic": "Arrays-and-Hashing",
    },

    "majority-element": {
        "difficulty": "Easy",
        "topic": "Arrays-and-Hashing",
    },

    "number-of-students-unable-to-eat-lunch": {
        "difficulty": "Easy",
        "topic": "Queue",
    },

    "products-of-array-discluding-self": {
        "difficulty": "Medium",
        "topic": "Arrays-and-Hashing",
    },

    "remove-element": {
        "difficulty": "Easy",
        "topic": "Two-Pointers",
    },

    "replace-elements-with-greatest-element-on-right-side": {
        "difficulty": "Easy",
        "topic": "Arrays-and-Hashing",
    },

    "score-of-a-string": {
        "difficulty": "Easy",
        "topic": "Arrays-and-Hashing",
    },

    "string-encode-and-decode": {
        "difficulty": "Medium",
        "topic": "Arrays-and-Hashing",
    },

    "top-k-elements-in-list": {
        "difficulty": "Medium",
        "topic": "Arrays-and-Hashing",
    },

    "two-integer-sum-ii": {
        "difficulty": "Medium",
        "topic": "Two-Pointers",
    },

    "two-integer-sum": {
        "difficulty": "Easy",
        "topic": "Arrays-and-Hashing",
    },

    "validate-parentheses": {
        "difficulty": "Easy",
        "topic": "Stack",
    },
}


def organize_problems():
    # Make sure the NeetCode folder exists
    if not SOURCE.exists():
        print(f"Could not find: {SOURCE}")
        return

    # Rebuild the organized folder each time the script runs
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)

    # Look through every NeetCode problem folder
    for problem_folder in SOURCE.iterdir():

        # Ignore anything that is not a folder
        if not problem_folder.is_dir():
            continue

        problem_name = problem_folder.name

        # Check whether we know this problem
        if problem_name not in PROBLEMS:
            destination = (
                DESTINATION
                / "Uncategorized"
                / problem_name
            )

            shutil.copytree(problem_folder, destination)

            print(
                f"Unknown problem: {problem_name} "
                f"-> Uncategorized"
            )

            continue

        info = PROBLEMS[problem_name]

        difficulty = info["difficulty"]
        topic = info["topic"]

        destination = (
            DESTINATION
            / difficulty
            / topic
            / problem_name
        )

        # Copy the entire problem folder
        shutil.copytree(problem_folder, destination)

        print(
            f"Organized {problem_name} "
            f"-> {difficulty}/{topic}"
        )


if __name__ == "__main__":
    organize_problems()

    print("\nDone organizing DSA problems!")