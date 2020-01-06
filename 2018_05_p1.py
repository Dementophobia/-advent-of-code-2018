from aoc import read_file, timer
from collections import deque
 
def react(polymer):
    polymer = deque(list(polymer) + ["."])
 
    while polymer[1] != ".":
        if polymer[0] != polymer[1] and \
           polymer[0].upper() == polymer[1].upper():
            polymer.popleft(), polymer.popleft()
            polymer.rotate()
        else:
            polymer.rotate(-1)
    
    polymer.rotate(-1)
    polymer.popleft()
    
    return polymer

@timer
def solve():
    input = read_file("05")
    return len(react(input))

result = solve() 
print(f"Solution: {result}")