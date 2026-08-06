# Python Practice — Modular CLI Application

A small modular Python CLI application. Each task lives in its own module
and is imported into `main.py`, which provides an interactive menu.

## Project Structure

```
python-practice/
├── main.py          # Central entry point (CLI Menu)
├── string_utils.py  # Task 1: User input & string formatting
├── list_utils.py    # Task 2: Removing list duplicates
├── dict_utils.py     # Task 3: Merging dictionaries
├── file_utils.py    # Task 5: Persistent file operations
├── README.md
└── .gitignore
```


## when youRun


You will see a menu like this:

```
=== PYTHON PRACTICE MENU ===
1. Run User Input Task
2. Run List Duplicates Task
3. Run Merge Dictionaries Task
5A. Add Note (Append to file)
5B. Show Last 5 Notes
6. Exit
```

Enter the number (or `5A` / `5B`) corresponding to the task you want to run.

## Task Overview

| # | Module            | Description                                              |
|---|--------------------|------------------------------------------------------------|
| 1 | `string_utils.py`  | Prompts for name & topic, returns a formatted greeting     |
| 2 | `list_utils.py`     | Removes duplicates from a list, preserving order            |
| 3 | `dict_utils.py`     | Merges two dictionaries, summing values on matching keys    |
| 5A| `file_utils.py`     | Appends a new note to `notes.txt`                            |
| 5B| `file_utils.py`     | Displays the last 5 notes from `notes.txt`                   |

