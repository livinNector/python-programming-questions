---
title: Valid IITM Student Email ID
---

# Problem Statement

You are given an email ID, which follows the format `yyctxxxxxx@dd.iitm.ac.in`. The task is to validate the email ID and extract details from it.

- `yy` (2 digits): Year of joining (e.g., `22` for 2022).
- `c` (1 character): Admission category (`f` for regular or `d` for direct entry).
- `t` (1 character): Term of joining (`1` for January, `2` for May, `3` for September).
- `xxxxxxx` (7 digits): Unique roll number.
- `dd` (2 characters): Degree (`ds` for Data Science or `es` for Electronic Systems).

You need to:
1. Validate the email ID for the correct format and content.
2. Print the following information:
   - Degree (full form).
   - Year of joining.
   - Term of joining (e.g., T1 (January)).
   - Admission category (`f` -> Regular, `d` -> Direct Entry).
   - Roll number.
   - Number of terms completed till now (current term inclusive).

If the email ID is invalid, return `None`.

**Example**

```python
email = "22f1001128@ds.iitm.ac.in"
validate_email(email)
# Output:
# ('Data Science', 2022, 'T1 (January)', 'Regular', '1001128', 9)
```

# Solution
```python test.py  -r 'python test.py'
<prefix>

</prefix>
<template>
def validate_email(email: str) -> tuple:
    '''
    Validates the given email and extracts relevant information.

    Args:
    email: str - the student email ID.

    Returns:
    tuple: (Degree, Year of joining, Term of joining, Admission category, Roll number, Terms completed)
           or None if the email is invalid.
    '''
    <los>
    import datetime
    
    # Split the email
    try:
        username, domain = email.split('@')
        subdomain = domain.split('.')[0]
    except ValueError:
        return None  # Invalid email format
    
    # Validate username length
    if len(username) != 10:
        return None

    # Extract details from username
    yy, c, t, roll_no = username[:2], username[2], username[3], username[4:]

    # Degree validation
    degree = "Data Science" if subdomain == "ds" else "Electronic Systems" if subdomain == "es" else None

    # Year and term validation
    try:
        year = 2000 + int(yy)
        term_map = {'1': "T1 (January)", '2': "T2 (May)", '3': "T3 (September)"}
        term = term_map.get(t)
    except ValueError:
        return None

    # Admission category and roll number validation
    if not term or c not in ['f', 'd'] or len(roll_no) != 7:
        return None

    # Admission category full form
    category = "Regular" if c == 'f' else "Direct Entry"

    # Calculate number of terms
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    terms_per_year = 3

    current_term_index = (current_month - 1) // 4 + 1
    current_term = f"T{current_term_index}"

    terms_completed = (current_year - year) * terms_per_year + current_term_index - int(t) + 1

    return degree, year, term, category, roll_no, terms_completed
    </los>
    <sol>
    return degree, year, term, category, roll_no, terms_completed
    </sol>
</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
email = "22f1001128@ds.iitm.ac.in"
is_equal(
    validate_email(email),
    ('Data Science', 2022, 'T1 (January)', 'Regular', '1001128', 9)
)

```

## Output 1

```
('Data Science', 2022, 'T1 (January)', 'Regular', '1001128', 9)

```


## Input 2

```
email = "21d1002017@es.iitm.ac.in"
is_equal(
    validate_email(email),
    ('Electronic Systems', 2021, 'T1 (January)', 'Direct Entry', '1002017', 12)
)

```

## Output 2

```
('Electronic Systems', 2021, 'T1 (January)', 'Direct Entry', '1002017', 12)

```


## Input 3

```
email = "22f100001@ds.iitm.ac.in"
is_equal(
    validate_email(email),
    None
)

```

## Output 3

```
None

```



# Private Test Cases

## Input 1

```
email = "19f2000107@es.iitm.ac.in"
is_equal(
    validate_email(email),
    ('Electronic Systems', 2019, 'T2 (May)', 'Regular', '2000107', 18)
)
email = "23d3001128@ds.iitm.ac.in"
is_equal(
    validate_email(email),
    ('Data Science', 2023, 'T3 (September)', 'Direct Entry', '3001128', 3)
)
email = "20f000112@ds.iitm.ac.in"
is_equal(
    validate_email(email),
    None
)

```

## Output 1

```
('Electronic Systems', 2019, 'T2 (May)', 'Regular', '2000107', 18)
('Data Science', 2023, 'T3 (September)', 'Direct Entry', '3001128', 3)
None

```
