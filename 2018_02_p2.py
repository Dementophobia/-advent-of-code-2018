from aoc import read_file, timer
from itertools import combinations

@timer
def solve():
    boxes  = read_file("02")

    for box_a, box_b in combinations(boxes, 2):
        if sum([a != b for a, b in zip(box_a, box_b)]) == 1:
            return "".join(a for a, b in zip(box_a, box_b) if a == b)

result = solve() 
print(f"Solution: {result}")