---
title : Most searched movies from log File
---
#Problem Statement
Netflix logs movie search in a text file, with each line representing a movie search. Your task is to process this file to determine the most searched movie(s). If two or more movies are tied, return all tied movies sorted alphabetically, along with their search counts.

Additionally, a seperate file contain the list of valid movies. Only movies from this list should be considered for the result. Movies not in the list of valid movies should be ignored.
    
*Example*

Given the following files:
`movies.txt`(valid movies)
'''
kabhi khusi kabhi gam
Heropanti
Do lafjon ki kahani
Jumanji

'''
`search_log.txt`(movies which search by the user):
'''
Jumanji kabhi kushi kabhi gam
Heropanti 
Jumanji kabhi kushi kabhi gam
Unknown movie
'''

#result
{
    "Jumanji" : 3
} 

'''
Jumanji is the most searched movies in a single day. So, it have 3 occurence due to that the result will be jumanji
'''

#Solution

```py3 test.py -r 'python test.py'
<prefix>
# some prefix
</prefix>
<template>
def most_search_movies(movies_file: str , search_log_file: str) -> dict:
    """
    Determine the most searched movie(s) from the given log file, considering only valid movies.

    Arguments:
    movies_file: str - Path to the file containing the list of valid movies(one par line).
    search_log_file: str - Path to the file containing movie searches(space-separated per line).

    Returns:
    dict - A dictionary where keys are the most searched movies(sorted alphabetically)
    and values are their respective search counts.
    """
    <los>...</los>
    <sol>
    with open(movies_file , 'r') as mf:
        valid_movies = set(mf.read().splitlines())

    movie_count = {}
    with open(search_log_file , 'r') as slf:
        for line in slf:
            for movie in line.split():
                if movie in valid_movies:
                    movie_count[movie] = movie_count.get(movie , 0) + 1
    max_count = max(movie_count.values(), default=0)
    most_searched = {
        movie: count for movie , count in sorted(movie_count.items()) if count == max_count
    }
    return most_searched
    </sol>
    test = <los>...</los><sol>'test'</sol> #tests
</template>
<suffix>
#some suffix
</suffix>
<suffix_invisble>
{% include '../function_type_and_most_searched_movies_suffix.py.jinja'%}
</suffix_invisble>
```

# Public Test Cases

## Input 1
`movies.txt`
"""
Avatar
Inception
Titanic
Frozen
"""
`search_log.txt`
"""
Avatar Titanic Titanic
Inception Avatar
Frozen Avatar
Avatar Titanic
"""
is_equal(
    most_search_movies('movies.txt' , 'search_log.txt'),
    {"Avatar" : 4 , "Titanic" : 3}
)

#Output 1
{
    "Avatar" : 4 , "Titanic" : 3
}

## Input 2
`movies.txt`
"""
HarryPotter
SpiderMan
IronMan
Superman
"""
`search_log.txt`
"""
SpiderMan SpiderMan HarryPotter
SuperMan SuperMan SuperMan Incredibles
IronMan SpiderMan SuperMan
"""
is_equal(
    most_search_movies('movies.txt' , 'search_log.txt'),
    {"SuperMan" : 4}
)

#Output 2
{"SuperMan" : 4}


# Input 3
`movies.txt`
"""
Intersteller
TheDarkKnight
ShutterIsland
"""
`search_log.txt`
"""
Interstellar ShutterIsland TheDarkKnight
TheDarkKnight ShutterIsland
Interstellar Interstellar
UnknownMovie
"""
is_equal(
    most_search_movies('movies.txt' , 'search_log.txt'),
    {"Interstellar" : 3}
)

#output 3
{
    "Interstellar" : 3
}
# Private Test Cases

# Input 1
`movies.txt`
x
y
z

`search_log.txt`
x x y
z z 
y

is_equal(
    most_search_movies('movies.txt' , 'search_log.txt'),
    {"x" : 2 , "y" : 2 }
)

```

## Output 1
```
{"x":2,"y":2}
```


## Input 2
`movies.txt`
"""
M1
M2
M3
M4
"""
`search_log.txt`
"""
M1 M1 M2
M3 M4 M4 M4
M1 M3 
M4 M2
M5
"""
```
is_equal(
   most_search_movies('movies.txt','search_log.txt'),
   {"M4" : 4}
```

```
## Output 2
{"M4" : 4}
```





















