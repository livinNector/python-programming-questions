---
title: Build the Treasure Hunt System
---

# Problem Statement

You are tasked with building a treasure hunt management system for a local adventure game. Participants in the game must follow a series of hints and complete tasks to discover treasures hidden in various locations. Your task is to implement the core functionality of the system.

The system must manage the following:
1. **Clue Chains**: Each treasure has a chain of clues associated with it. Clues must be revealed one at a time, in the correct order, as participants progress.
2. **Participant Progress**: The system must track each participant’s current progress and ensure they cannot skip any clues.
3. **Treasure Discovery**: When a participant solves the final clue in the chain, they discover the treasure.

You must implement the following functions:

### Function Signatures
```python
def add_treasure(treasure_name: str, clues: list[str]) -> None:
    pass

def reveal_clue(participant: str, treasure_name: str) -> str:
    pass

def solve_clue(participant: str, treasure_name: str) -> str:
    pass

def participant_summary(participant: str) -> dict:
    pass
```

### Function Descriptions
- `add_treasure(treasure_name: str, clues: list[str])`: Adds a treasure and its chain of clues to the system.
- `reveal_clue(participant: str, treasure_name: str) -> str`: Reveals the next clue for a participant attempting a specific treasure. If all clues are solved, returns a message indicating the treasure has already been discovered.
- `solve_clue(participant: str, treasure_name: str) -> str`: Marks the current clue as solved for the participant and prepares the next clue. If it is the final clue, marks the treasure as discovered.
- `participant_summary(participant: str) -> dict`: Returns a summary of all treasures attempted by the participant, including their progress and whether each treasure has been discovered.

### Example
```python
add_treasure("Golden Crown", ["Find the key", "Unlock the chest", "Retrieve the crown"])
add_treasure("Emerald Gem", ["Solve the riddle", "Navigate the maze", "Find the emerald"])

reveal_clue("Alice", "Golden Crown")  # Output: "Find the key"
solve_clue("Alice", "Golden Crown")   # Output: "Clue solved. Next clue: Unlock the chest"
solve_clue("Alice", "Golden Crown")   # Output: "Clue solved. Next clue: Retrieve the crown"
solve_clue("Alice", "Golden Crown")   # Output: "Congratulations! You discovered the Golden Crown."
participant_summary("Alice")           # Output: {"Golden Crown": {"progress": 3, "discovered": True}}
```

# Solution

```py3 solution.py -r 'python solution.py'
<template>
class TreasureHunt:
    def __init__(self):
        self.treasures = {}
        self.participants = {}

    def add_treasure(self, treasure_name: str, clues: list[str]) -> None:
        self.treasures[treasure_name] = clues

    def reveal_clue(self, participant: str, treasure_name: str) -> str:
        if participant not in self.participants:
            self.participants[participant] = {}

        if treasure_name not in self.participants[participant]:
            self.participants[participant][treasure_name] = 0

        progress = self.participants[participant][treasure_name]
        if progress >= len(self.treasures[treasure_name]):
            return f"Treasure already discovered: {treasure_name}"
        return self.treasures[treasure_name][progress]

    def solve_clue(self, participant: str, treasure_name: str) -> str:
        if participant not in self.participants or treasure_name not in self.participants[participant]:
            return "No clue revealed yet."

        progress = self.participants[participant][treasure_name]
        if progress >= len(self.treasures[treasure_name]):
            return f"Treasure already discovered: {treasure_name}"

        self.participants[participant][treasure_name] += 1
        progress += 1

        if progress == len(self.treasures[treasure_name]):
            return f"Congratulations! You discovered the {treasure_name}."
        return f"Clue solved. Next clue: {self.treasures[treasure_name][progress]}"

    def participant_summary(self, participant: str) -> dict:
        if participant not in self.participants:
            return {}

        summary = {}
        for treasure, progress in self.participants[participant].items():
            summary[treasure] = {
                "progress": progress,
                "discovered": progress >= len(self.treasures[treasure])
            }
        return summary

if __name__ == "__main__":
    hunt = TreasureHunt()
    # Example usage can be added here
</template>
```

# Public Test Cases

## Input 1
```
add_treasure("Golden Crown", ["Find the key", "Unlock the chest", "Retrieve the crown"])
add_treasure("Silver Ring", ["Locate the cave", "Explore the chamber", "Uncover the ring"])
reveal_clue("Bob", "Golden Crown")
solve_clue("Bob", "Golden Crown")
reveal_clue("Bob", "Golden Crown")
solve_clue("Bob", "Golden Crown")
solve_clue("Bob", "Golden Crown")
participant_summary("Bob")
```

## Output 1
```
Find the key
Clue solved. Next clue: Unlock the chest
Unlock the chest
Clue solved. Next clue: Retrieve the crown
Congratulations! You discovered the Golden Crown.
{"Golden Crown": {"progress": 3, "discovered": True}}
```

## Input 2
```
add_treasure("Emerald Gem", ["Solve the riddle", "Navigate the maze", "Find the emerald"])
reveal_clue("Alice", "Emerald Gem")
solve_clue("Alice", "Emerald Gem")
solve_clue("Alice", "Emerald Gem")
participant_summary("Alice")
```

## Output 2
```
Solve the riddle
Clue solved. Next clue: Navigate the maze
Clue solved. Next clue: Find the emerald
{"Emerald Gem": {"progress": 2, "discovered": False}}
```

# Private Test Cases

## Input 1
```
add_treasure("Ruby Treasure", ["Find the map", "Follow the trail", "Dig for the treasure"])
add_treasure("Sapphire Quest", ["Find the journal", "Decode the message", "Locate the sapphire"])
reveal_clue("Charlie", "Ruby Treasure")
solve_clue("Charlie", "Ruby Treasure")
solve_clue("Charlie", "Ruby Treasure")
solve_clue("Charlie", "Ruby Treasure")
participant_summary("Charlie")
```

## Output 1
```
Find the map
Clue solved. Next clue: Follow the trail
Clue solved. Next clue: Dig for the treasure
Congratulations! You discovered the Ruby Treasure.
{"Ruby Treasure": {"progress": 3, "discovered": True}}
```

## Input 2
```
add_treasure("Diamond Heist", ["Plan the strategy", "Bypass the security", "Steal the diamond"])
add_treasure("Amethyst Adventure", ["Gather the tools", "Navigate the cave", "Find the amethyst"])
reveal_clue("Dana", "Diamond Heist")
solve_clue("Dana", "Diamond Heist")
reveal_clue("Dana", "Amethyst Adventure")
solve_clue("Dana", "Amethyst Adventure")
solve_clue("Dana", "Amethyst Adventure")
participant_summary("Dana")
```

## Output 2
```
Plan the strategy
Clue solved. Next clue: Bypass the security
Gather the tools
Clue solved. Next clue: Navigate the cave
Clue solved. Next clue: Find the amethyst
{"Diamond Heist": {"progress": 1, "discovered": False}, "Amethyst Adventure": {"progress": 2, "discovered": False}}
```
