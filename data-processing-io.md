---
title: Product of Prime Numbers from User Input
tags: [primes, I/O, filtering]
---

# Problem Statement

Given five numbers input by the user, determine which of them are prime numbers. Find the product of the prime numbers and print it.

Assume the numbers are non-negative integers. If no prime numbers are found, print 0.

# Solution
```python test.py -r 'python test.py'
<template>
<sol>
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = list(map(int, input().split()))
prime_nums = [num for num in nums if is_prime(num)]

if prime_nums:
    product = 1
    for prime in prime_nums:
        product *= prime
    print(product)
else:
    print(0)
</sol>
</template>

# Public Test Cases

## Input 1
```
1 2 3 4 5
```

## Output 1
```
30
```

## Input 2
```
10 15 18 7 4
```

## Output 2
```
7
```

# Private Test Cases


## Input 1
```
6 9 11 13 17
```

## Output 1
```
2002
```

## Input 2
```
29 34 37 40 42
```

## Output 2
```
1073
```