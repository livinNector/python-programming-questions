---
title: Process Student Scores
tags: ['python', 'functions']
---
# Problem Statement
Write a function process_student_scores(students: list) -> dict that processes a list of students' scores and returns a dictionary containing the following information for each subject:

    The average score for the subject.
    The highest score for the subject.
    The lowest score for the subject.

Each student in the input list is represented as a dictionary with the following structure:
{
    'name': <string>,
    'scores': {
        'subject1': <score>,
        'subject2': <score>,
        ...
    }
}

The function should return a dictionary with the subject names as keys and another dictionary as the value containing the average, highest, and lowest scores for each subject.
Function Signature:
def process_student_scores(students: list) -> dict:
**Sample Input**
```
students = [
    {'name': 'Alice', 'scores': {'Math': 85, 'Science': 90}},
    {'name': 'Bob', 'scores': {'Math': 75, 'Science': 80}},
    {'name': 'Charlie', 'scores': {'Math': 95, 'Science': 85}}
]
process_student_scores(students)
```
**Sample Output**
```
{
    'Math': {'average': 85.0, 'highest': 95, 'lowest': 75},
    'Science': {'average': 85.0, 'highest': 90, 'lowest': 80}
}
```
# Solution
```py test.py -r 'python3 test.py'
<prefix>
def process_student_scores(students: list) -> dict:
    """
    Processes the list of student scores and returns a dictionary containing:
    - The average score for each subject.
    - The highest score for each subject.
    - The lowest score for each subject.
   
    Arguments:
    students: list of dictionaries, where each dictionary contains student name and their scores in subjects.
   
    Returns:
    dict: A dictionary where keys are subject names and values are dictionaries with 'average', 'highest', and 'lowest' scores.
    """
</prefix>
   
    # Initialize an empty dictionary to store results
    subject_stats = {}
   
   <sol>
    # Iterate through each student
    for student in students:
        # Iterate through each subject score
        for subject, score in student['scores'].items():
            # If subject is not in the subject_stats dictionary, initialize it
            if subject not in subject_stats:
                subject_stats[subject] = {'scores': [], 'average': 0, 'highest': float('-inf'), 'lowest': float('inf')}
           
            # Add the score to the list of scores for the subject
            subject_stats[subject]['scores'].append(score)
           
            # Update the highest and lowest scores for the subject
            if score > subject_stats[subject]['highest']:
                subject_stats[subject]['highest'] = score
            if score < subject_stats[subject]['lowest']:
                subject_stats[subject]['lowest'] = score
   
    # Calculate the average score for each subject
    for subject, stats in subject_stats.items():
        stats['average'] = sum(stats['scores']) / len(stats['scores'])
        # Remove the scores list as it's no longer needed
        del stats['scores']
    </sol>
   
    return subject_stats

```
# Public Test Cases
## Input 1
```
students = [
    {'name': 'Alice', 'scores': {'Math': 85, 'Science': 90}},
    {'name': 'Bob', 'scores': {'Math': 75, 'Science': 80}},
    {'name': 'Charlie', 'scores': {'Math': 95, 'Science': 85}}
]

process_student_scores(students)
```
## Output 1
```
{
    'Math': {'average': 85.0, 'highest': 95, 'lowest': 75},
    'Science': {'average': 85.0, 'highest': 90, 'lowest': 80}
}
```
## Input 2
```
students = [
    {'name': 'Alice', 'scores': {'Math': 70, 'Science': 60}},
    {'name': 'Bob', 'scores': {'Math': 80, 'Science': 70}},
    {'name': 'Charlie', 'scores': {'Math': 90, 'Science': 80}}
]

process_student_scores(students)
```
## Output 2
```
{
    'Math': {'average': 80.0, 'highest': 90, 'lowest': 70},
    'Science': {'average': 70.0, 'highest': 80, 'lowest': 60}
}
```
## Input 3
```
students = [
    {'name': 'Alice', 'scores': {'Math': 100}},
    {'name': 'Bob', 'scores': {'Math': 95}},
    {'name': 'Charlie', 'scores': {'Math': 90}}
]

process_student_scores(students)
```
## Output 3
```
{
    'Math': {'average': 95.0, 'highest': 100, 'lowest': 90}
}
```

# Private Test Cases
## Input 1
```
students = [
    {'name': 'John', 'scores': {'English': 85, 'History': 75}},
    {'name': 'Jane', 'scores': {'English': 90, 'History': 80}},
    {'name': 'Alex', 'scores': {'English': 80, 'History': 85}}
]

process_student_scores(students)
```
## Output 1
```
{
    'English': {'average': 85.0, 'highest': 90, 'lowest': 80},
    'History': {'average': 80.0, 'highest': 85, 'lowest': 75}
}
```