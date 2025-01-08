
---

title: Dictionary Value Transformation

tags: ['dict', 'string', 'int']

---

  

# Problem Statement

Write a function that transforms the values in a dictionary based on their types. The function should:

1. Convert all string values to uppercase

2. Multiply all integer values by 2

3. Leave all other types of values unchanged

  

Example: if the input dictionary is {'name': 'john', 'age': 25, 'active': True}, the output should be {'name': 'JOHN', 'age': 50, 'active': True}.

  

# Solution

```python test.py -r 'python test.py'

<prefix>

  

</prefix>

<template>

    def transform_dict_values(input_dict: dict) -> dict:

    '''

    Transform values in a dictionary based on their types.

    Arguments:

    input_dict: dict - Dictionary containing various types of values

    Returns:

    dict - New dictionary with transformed values

    '''

    <los>pass</los>

    <sol>

    result = {}

    for key, value in input_dict.items():

        if isinstance(value, str):

            result[key] = value.upper()

        elif isinstance(value, int):

            result[key] = value * 2

        else:

            result[key] = value

    return result

    </sol>

</template>

  

<suffix_invisible>

def test_transform_dict(input_dict, expected_output):

    result = transform_dict_values(input_dict)

    assert result == expected_output, f"Expected {expected_output}, but got {result}"

</suffix_invisible>

```

  

# Public Test Cases

  

## Input 1

  

```

{'name': 'alice', 'score': 10}

```

  

## Output 1

  

```

{'name': 'ALICE', 'score': 20}

```

  
  

## Input 2

  

```

{'city': 'paris', 'population': 1000000, 'capital': True}

```

  

## Output 2

  

```

{'city': 'PARIS', 'population': 2000000, 'capital': True}

```

  
  
  

# Private Test Cases

  

## Input 1 (empty dictionary)

  

```

{}

```

  

## Output 1

  

```

{}

```

  

## Input 2

  

```

{'temp': 20.5, 'unit': 'celsius', 'reading': 100, 'valid': True}

```

  

## Output 2

  

```

{'temp': 20.5, 'unit': 'CELSIUS', 'reading': 200, 'valid': True}

```