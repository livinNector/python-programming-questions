---
title: Frequency Analysis
---

# Problem Statement

Given a number n, followed by n lines of text, create a function that prints all words encountered in the text, one per line. The words should be sorted in descending order according to their number of occurrences in the text, and all words with the same frequency should be printed in lexicographical order.

**Input Format:** An integer `n` in the first line followed by n lines of text.

**Output Format:** The sequence of words encountered in the text, one per line, sorted first by their frequencies and then lexicographically.

**Sample Input**
```
9
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
```
**Sample Output**
```
damme
is
name
van
bond
claude
hi
my
james
jean
what
your
```

**Hint:** After you create a dictionary of the words and their frequencies, you would like to sort it according to the frequencies. This can be achieved if you create a list whose elements are tuples of two elements: the frequency of occurrence of a word and the word itself. For example, [(2, 'hi'), (1, 'what'), (3, 'is')]. Then the standard list sort will sort a list of tuples, with the tuples compared by the first element, and if these are equal, by the second element. This is nearly what is required in the problem.

# Solution
```python test.py  -r 'python test.py'
<prefix>
def frequency_analysis() -> None:
    '''
    Print the sequence of words encountered in the text, 
    one per line, sorted first by their frequencies
    and then lexicographically.
    '''
</prefix>
<template>
<sol>
    n = int(input())
    frequency = {}
    for i in range(n):
        for word in input().split():
            if word not in frequency:
                frequency[word] = 1
            else:
                frequency[word] += 1
    frequency_tuple = [(-1 * v,k) for k,v in frequency.items()]
    frequency_tuple.sort()
    for v,k in frequency_tuple:
       print(k)
</sol>
</template>
<suffix>
frequency_analysis()
</suffix>
```

# Public Test Cases

## Input 1

```
9
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
```

## Output 1

```
damme
is
name
van
bond
claude
hi
my
james
jean
what
your
```


## Input 2

```
1
ai ai ai ai ai ai ai ai ai ai
```

## Output 2

```
ai
```


## Input 3

```
2
iovjxotfvt h h iovjxotfvt h iovjxotfvt iovjxotfvt h
h iovjxotfvt
```

## Output 3

```
h
iovjxotfvt
```


# Private Test Cases

## Input 1

```
4
eqlbahbovv pzpumhz mlcgtbbnfr
axsjbontg emojwajtfi
basdu nzyh wpyirkmz xxkmrr blnlqwcpur eqlbahbovv nzyh mlcgtbbnfr
mlcgtbbnfr axsjbontg mlcgtbbnfr mlcgtbbnfr mlcgtbbnfr blnlqwcpur mlcgtbbnfr
```

## Output 1

```
mlcgtbbnfr
axsjbontg
blnlqwcpur
eqlbahbovv
nzyh
basdu
emojwajtfi
pzpumhz
wpyirkmz
xxkmrr
```

## Input 2

```
14
That thou hast her it is not all my grief,
And yet it may be said I loved her dearly,
That she hath thee is of my wailing chief,
A loss in love that touches me more nearly.
Loving offenders thus I will excuse ye,
Thou dost love her, because thou know'st I love her,
And for my sake even so doth she abuse me,
Suff'ring my friend for my sake to approve her.
If I lose thee, my loss is my love's gain,
And losing her, my friend hath found that loss,
Both find each other, and I lose both twain,
And both for my sake lay on me this cross,
But here's the joy, my friend and I are one,
Sweet flattery, then she loves but me alone.
```

## Output 2

```
my
I
And
for
friend
her,
is
love
me
sake
she
That
and
both
hath
her
it
lose
loss
that
thou
A
Both
But
If
Loving
Suff'ring
Sweet
Thou
abuse
all
alone.
approve
are
be
because
but
chief,
cross,
dearly,
dost
doth
each
even
excuse
find
flattery,
found
gain,
grief,
hast
her.
here's
in
joy,
know'st
lay
losing
loss,
love's
loved
loves
may
me,
more
nearly.
not
of
offenders
on
one,
other,
said
so
the
thee
thee,
then
this
thus
to
touches
twain,
wailing
will
ye,
yet
```
