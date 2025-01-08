---
title:Cryptographic Shift Decoder
---

# Problem Statement

You are tasked with building a cryptographic decoder that deciphers a string encoded with a shift cipher. In a shift cipher, each letter in the plaintext is shifted by a fixed number of positions in the alphabet. For example, with a shift of 3, A becomes D, B becomes E, and so on. The decryption reverses this process.

Your task is to:

->Identify the most common letter in the encoded text (assuming this corresponds to E in plaintext, as it is the most frequent letter in English).
->Deduce the shift value based on this information.
->Decode the entire string using the deduced shift value.

# Functions to Implement

**find_most_frequent_letter(encoded: str) -> str**

Input: Encoded string containing uppercase English letters and spaces.
Output: The most frequent letter in the string.
**deduce_shift(most_frequent: str) -> int**

Input: Most frequent letter from the encoded text.
Output: The shift value used to encode the text.

**decrypt(encoded: str, shift: int) -> str**
Input: Encoded string and the deduced shift value.
Output: Decoded plaintext string.


**Example**
```
Input: encoded = "KHOOR ZRUOG"

```
Output : HELLO WORLD


# Solution

```py3 test.py -r 'python test.py'
<template>
from collections import Counter

def find_most_frequent_letter(encoded: str) -> str:
    """
    Identify the most frequent letter in the encoded text.
    Ignore spaces.
    """
    freq = Counter([char for char in encoded if char.isalpha()])
    return freq.most_common(1)[0][0]

def deduce_shift(most_frequent: str) -> int:
    """
    Deduce the shift value based on the most frequent letter.
    Assuming the most frequent letter corresponds to 'E'.
    """
    return (ord(most_frequent) - ord('E')) % 26

def decrypt(encoded: str, shift: int) -> str:
    """
    Decrypt the encoded text using the deduced shift value.
    """
    decoded = []
    for char in encoded:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decoded.append(shifted_char)
        else:
            decoded.append(char)
    return ''.join(decoded)

# Input handling (for testing purposes only)
if __name__ == "__main__":
    encoded = input("Enter encoded text: ").strip().upper()
    most_frequent = find_most_frequent_letter(encoded)
    shift = deduce_shift(most_frequent)
    print("Decoded Text:", decrypt(encoded, shift))
</template>

```

# Public Test Cases

## Input 1

```
encoded = "XLMW MW XLI SRHITXMSR"

```

## Output 1

```
Decoded Text: THIS IS THE ENCRYPTION

```

## Input 2

```
encoded = "GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT"
```

## Output 2

```
Decoded Text: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

```

## Input 3

```
encoded = "WKH FDW LV RQ WKH URRI"

```

## Output 3

```
Decoded Text: THE CAT IS ON THE ROOF

```

# Private Test Cases

## Input 1

```
encoded = "ZHOFRPH WR WKH FUBSWRJUDSKB FKDOOHQJH"

```

## Output 1

```
Decoded Text: WELCOME TO THE CRYPTOGRAPHY CHALLENGE

```
