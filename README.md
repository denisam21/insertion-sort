# insertion-sort
# Sorting Numbers with Lists

This program creates a list of 100 random integers between -1000 and 1000 and then sorts them step by step using only basic list operations.  
The goal is to show how sorting can be implemented manually, without calling `sort()` or `sorted()`.

## What it does
- A list of unsorted numbers is generated with `random.randint()`.
- Each number is placed into a new list at the correct position using only `append` and `insert`.
- At the end, the script prints the original unsorted list and the new sorted list.