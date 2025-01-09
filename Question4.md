---
title: Maximize Non-Overlapping Lecture Hall Utilization
---

# Problem Statement

Given a list of lecture hall bookings represented as tuples of `(start_time, end_time)`, implement a function `max_lectures` that selects the maximum number of non-overlapping lectures to maximize the utilization of the lecture hall in terms of the number of bookings served.

The function should return the selected bookings in sorted order of start time.

**Constraints**:
1. Each booking is represented as a tuple `(start_time, end_time)` where `0 <= start_time < end_time <= 24`.
2. The input list will have at least 1 booking and at most 100 bookings.

**Example**

```python
bookings = [(0, 4), (1, 3), (4, 6), (5, 8), (5, 10), (7, 9)] max_lectures(bookings)
# Output: [(1, 3), (4, 6), (7, 9)]
```
Explanation:
- Out of the bookings, `(1, 3), (4, 6), (7, 9)` are selected as they form the largest set of non-overlapping bookings.
- If there are multiple valid solutions, return any one of them.

# Solution
```py3 test.py -r 'python test.py'
<template>
def max_lectures(bookings):
    """
    Finds the maximum number of non-overlapping lectures that can be scheduled.

    Arguments:
    bookings : list[tuple[int, int]] - List of tuples where each tuple represents (start_time, end_time).

    Returns:
    list[tuple[int, int]] - List of selected non-overlapping bookings sorted by start time.
    """
    <los>...</los>
    <sol>
    # Sort bookings by their end time (greedy approach)
    bookings.sort(key=lambda x: x[1])

    selected = []
    last_end = 0

    for start, end in bookings:
        if start >= last_end:  # Check if the booking doesn't overlap
            selected.append((start, end))
            last_end = end

    return selected
    </sol>
</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
bookings = [(0, 4), (1, 3), (4, 6), (5, 8), (5, 10), (7, 9)]
is_equal(
    max_lectures(bookings),
    [(1, 3), (4, 6), (7, 9)]
)

```

## Output 1

```
[(1, 3), (4, 6), (7, 9)]

```


## Input 2

```
bookings = [(2, 3), (3, 4), (1, 2), (5, 7), (6, 8)]
is_equal(
    max_lectures(bookings),
    [(1, 2), (2, 3), (3, 4), (5, 7)]
)

```

## Output 2

```
[(1, 2), (2, 3), (3, 4), (5, 7)]

```


# Private Test Cases

## Input 1

```
bookings = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
is_equal(
    max_lectures(bookings),
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
)
bookings = [(5, 6), (1, 3), (4, 6), (2, 5), (6, 8)]
is_equal(
    max_lectures(bookings),
    [(1, 3), (4, 6), (6, 8)]
)
bookings = [(7, 9), (0, 2), (2, 4), (4, 6), (6, 8)]
is_equal(
    max_lectures(bookings),
    [(0, 2), (2, 4), (4, 6), (6, 8)]
)

```

## Output 1

```
[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
[(1, 3), (4, 6), (6, 8)]
[(0, 2), (2, 4), (4, 6), (6, 8)]

```
