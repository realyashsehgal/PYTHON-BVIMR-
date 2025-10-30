# PYTHON-BVIMR-

A collection of short Python example scripts (numbered files) used for learning and demonstrations.

This repository contains many small Python files (e.g. `1First.py`, `2Second.py`, ...). Recently a maintenance
operation was performed to remove full-line comments from most files while preserving inline comments and
docstrings. The file `5Fifth.py` was intentionally left unchanged.

Contents
--------
- Many numbered example scripts (e.g. `42FortyTwo.py`, `43FortyThree.py`, ...)
- `Signature_folder/Signature.py` — helper used by some examples
- `scripts/remove_full_line_comments.py` — utility used to remove whole-line `#` comments (see below)

What was changed
-----------------
- Full-line comments (lines where the first non-space character is `#`) were removed from most `.py` files.
- Inline comments (trailing `#`) and triple-quoted strings / docstrings were preserved.
- `5Fifth.py` and any files in `__pycache__` were excluded from the change.

Why
---
This was done to produce a cleaner set of example files (e.g., for automated exercises or grading) while
keeping important inline notes and docstrings intact.

Tooling: how it was done
-----------------------
There is a small script used to perform the change:

- `scripts/remove_full_line_comments.py`

To re-run the script (Windows PowerShell):

```powershell
python .\scripts\remove_full_line_comments.py
```

What the script does
--------------------
- Walks the repository tree from the repo root.
- Skips any `__pycache__` directories and the file `5Fifth.py`.
- Removes lines where the first non-whitespace character is `#`.
- Writes changes back to the files (UTF-8). The script prints which files were modified.

Safety and undo
---------------
- The script intentionally only removes whole-line comments to reduce the risk of changing program logic.
- If your repository is under git, you can review or revert the changes with git. Example commands:

```powershell
# Show what changed
git status
git add -A
git diff --staged

# Commit (if you want to keep the changes)
git commit -m "Remove full-line comments (except 5Fifth.py)"

# To undo (if not yet committed)
git checkout -- .

# To revert an already committed change, use git revert with the commit hash.
```

If you want me to create a git commit for these changes, generate a patch, or revert specific files, tell me which option you prefer.

Notes
-----
- If you want comments removed differently (e.g., also remove inline comments or remove docstrings), that is
	more intrusive and can change program behavior — ask before running such transformations.
- A small sample of files that still contain helpful examples: `42FortyTwo.py` (slicing demo), `43FortyThree.py` (list comprehensions).

Contact
-------
If you want extra clean-up, formatting, or to convert these examples into a package or notebooks, say which files to
target and I'll prepare a plan.