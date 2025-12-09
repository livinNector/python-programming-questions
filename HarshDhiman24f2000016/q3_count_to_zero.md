---
title: count to 0
---

# Problem Statement
you have to write a code that will accept an input() as integer from user.

If input is +ve:
keep printing and subtracting 1 from number until 0 is printed.

If input is -ve:
keep printing and adding 1 to number until 0 is printed

If input is 0:
print "already zero"

note: you have to print each output in seperate line

# Solution
```python test.py  -r 'python test.py'
<prefix>

</prefix>
<template>
'''
you have to write a code that will accept an input() as integer from user.

If input is +ve:
keep printing and subtracting 1 from number until 0 is printed.

If input is -ve:
keep printing and adding 1 to number until 0 is printed

If input is 0:
print "already zero"

note: you have to print each output in seperate line
'''
<sol>
n = int(input())
if n > 0:
    while n >= 0:
        print(n)
        n = n - 1
elif n < 0:
    while n <= 0:
        print(n)
        n = n + 1
elif n == 0:
    print("already zero")
</sol>
</template>
<suffix>

</suffix>
<suffix_invisible>

</suffix_invisible>
```

# Public Test Cases

## Input 1

```
0
```

## Output 1

```
already zero
```


## Input 2

```
-5
```

## Output 2

```
-5
-4
-3
-2
-1
0
```


## Input 3

```
3
```

## Output 3

```
3
2
1
0
```


## Input 4

```
5
```

## Output 4

```
5
4
3
2
1
0
```


## Input 5

```
9
```

## Output 5

```
9
8
7
6
5
4
3
2
1
0
```


# Private Test Cases

## Input 1

```
-17
```

## Output 1

```
-17
-16
-15
-14
-13
-12
-11
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
```

## Input 2

```
8
```

## Output 2

```
8
7
6
5
4
3
2
1
0
```

## Input 3

```
0
```

## Output 3

```
already zero

```
