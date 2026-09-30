# Week 7 Assignment: Shopping List Manager

- `list_warmup.py` demonstrates list indexing, appending, removing, and counting.
- `shopping_list.py` provides an interactive menu to add, remove, and show shopping list items.
- `list_report.py` numbers the items, counts names with more than four letters, and finds the longest name.
- `screenshots/` is for screenshots of each program running.

Checking whether an item is in the list before calling `.remove()` is safer because `.remove()` raises an error when the item is missing. The membership check lets the program handle that situation with a helpful message instead. This keeps the manager running instead of stopping unexpectedly.