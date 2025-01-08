---
title: Access rights
---

# Problem Statement

You are trying to create a permission based filesystem access for the new unix-inspired Operating System you are developing. The requirements for this system is as given below.

For each file there is a known set of operations which may be applied to it:
write W,
read R,
execute X.

The first line contains the number N — the number of files contained in the filesystem. The following N lines contain the file names and allowed operations with them, separated by spaces. The next line contains an integer M — the number of operations to the files. In the last M lines specify the operations that are requested for files. One file can be requested many times.

For each request your program should return OK if the requested operation is valid or Access denied if the operation is invalid.

**Input Format:** An integer N, followed by N lines containing the file names and permissions. Then an integer M on the next line, followed by M lines specifying operation requests on the files.

**Output Format:** The response to each of the M requests, one per line, print `OK` if the requested operation is allowed or `Access denied` if it is disallowed.

## Sample Input
```
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog
```
## Sample Output
```
OK
Access denied
Access denied
OK
OK
```

# Solution
```python test.py  -r 'python test.py'
<template>
<sol>
permissions = {}
n = int(input())
for i in range(n):
    s = input().split()
    permissions[s[0]] = set(s[1:])
for i in range(int(input())):
    operation, file = input().split()
    permission = None
    if operation == 'read':
        permission = 'R'
    if operation == 'write':
        permission = 'W'
    if operation == 'execute':
        permission = 'X'
    if permission in permissions[file]:
        print('OK')
    else:
        print('Access denied')
</sol>
</template>
```

# Public Test Cases

## Input 1

```
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog
```

## Output 1

```
OK
Access denied
Access denied
OK
OK
```


## Input 2

```
1
abacaba X
3
read abacaba
write abacaba
execute abacaba
```

## Output 2

```
Access denied
Access denied
OK
```


## Input 3

```
1
tmp_909925047 W X R
7
execute tmp_909925047
read tmp_909925047
write tmp_909925047
read tmp_909925047
execute tmp_909925047
execute tmp_909925047
read tmp_909925047
```

## Output 3

```
OK
OK
OK
OK
OK
OK
OK
```


# Private Test Cases

## Input 1

```
5
tmp_1017722015 W
tmp_897110090 X W R
tmp_651548400 W X
tmp_422551574 X R W
tmp_477658548 W
1
write tmp_897110090
```

## Output 1

```
OK
```

## Input 2

```
2
tmp_584361681 R X
tmp_70361076 X
3
read tmp_70361076
write tmp_70361076
write tmp_70361076
```

## Output 2

```
Access denied
Access denied
Access denied
```

## Input 3

```
4
tmp_796487715 X R W
tmp_31144126 X R
tmp_967334538 R
tmp_264755563 R W
3
read tmp_264755563
execute tmp_796487715
execute tmp_796487715
```

## Output 3

```
OK
OK
OK
```
