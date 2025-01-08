---
title: Decode the Artifact Enigma
---

# Problem Statement

At an ancient archaeological dig site, researchers uncovered a vault containing encrypted artifact records. Each record is a single string that encodes an artifact name, hidden integers, and a special checksum. Your mission is to decode these records and determine which artifacts are authentic based on their checksum values.

The rules of authenticity are as follows:
- Each record contains an artifact name, followed by embedded integers, and ends with a checksum in square brackets (e.g., `[123]`).
- To validate authenticity, the sum of the extracted integers must match the checksum.
- Only valid records should be included in the output.

Write a program that reads artifact records from standard input and processes them. The program should:
- Validate each record by comparing the sum of its integers to its checksum.
- For valid records, calculate the total sum of integers and group artifacts by their first letter (case-insensitive).
- Sort groups alphabetically by their letter, and within each group, sort artifact names by their total integer sum in descending order.
- Print the groups along with artifact names and their summed integers in the specified format.

**Input Format**
```
Each line contains one artifact record as a string.
```

**Output Format**
```
Group A:
  artifact_name_1: total_sum_1
  artifact_name_2: total_sum_2
Group B:
  artifact_name_1: total_sum_1
...
```

**Example Input**
```
Ruby124Stone45[169]
Emerald20Crystal99[119]
Diamond30Gem[30]
Ruby100Fake20[150]
```

**Example Output**
```
Group D:
  Diamond30Gem: 30
Group E:
  Emerald20Crystal99: 119
Group R:
  Ruby124Stone45: 169
```

# Solution

```py3 solution.py -r 'python solution.py'
<template>
if __name__ == "__main__":
    data = []
    while True:
        try:
            line = input().strip()
            if line:
                data.append(line)
        except EOFError:
            break

    valid_records = {}

    for line in data:
        if '[' not in line or ']' not in line:
            continue

        artifact, checksum = line.rsplit('[', 1)
        checksum = checksum.rstrip(']')
        if not checksum.isdigit():
            continue

        checksum_value = int(checksum)
        artifact_name = ''.join([ch for ch in artifact if ch.isalpha()])
        total_sum = 0
        temp_num = ''

        for ch in artifact:
            if ch.isdigit():
                temp_num += ch
            else:
                if temp_num:
                    total_sum += int(temp_num)
                    temp_num = ''
        if temp_num:
            total_sum += int(temp_num)

        if total_sum == checksum_value:
            first_letter = artifact_name[0].upper()
            if first_letter not in valid_records:
                valid_records[first_letter] = []
            valid_records[first_letter].append((artifact_name, total_sum))

    for group in sorted(valid_records.keys()):
        print(f"Group {group}:")
        for name, total in sorted(valid_records[group], key=lambda x: x[1], reverse=True):
            print(f"  {name}: {total}")
</template>
```

# Public Test Cases

## Input 1
```
Golden24Mask56[80]
Silver90Crown33[123]
Bronze12Medal78[90]
InvalidEntry99[100]
```

## Output 1
```
Group B:
  Bronze12Medal78: 90
Group G:
  Golden24Mask56: 80
Group S:
  Silver90Crown33: 123
```

## Input 2
```
Iron10Shield20[30]
Steel15Sword25[40]
Obsidian40Dagger[39]
InvalidArtifact50[60]
```

## Output 2
```
Group I:
  Iron10Shield20: 30
Group S:
  Steel15Sword25: 40
```

# Private Test Cases

## Input 1
```
Artifact100Rare200[300]
Relic300Ancient99[399]
Treasure400Hidden10[410]
FakeArtifact123[124]
```

## Output 1
```
Group A:
  Artifact100Rare200: 300
Group R:
  Relic300Ancient99: 399
Group T:
  Treasure400Hidden10: 410
```

## Input 2
```
Object42Unknown12[54]
Mystery10Thing5[15]
Enigma7Shape2[9]
FalseEntry77[88]
```

## Output 2
```
Group E:
  Enigma7Shape2: 9
Group M:
  Mystery10Thing5: 15
Group O:
  Object42Unknown12: 54
```
