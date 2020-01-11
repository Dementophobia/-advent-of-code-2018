from aoc import read_file, timer
from collections import defaultdict

@timer
def solve():
    input     = read_file("07")
    built     = []
    steps     = defaultdict(list)
    all_steps = set()

    for line in input:
        first = line.split(" ")[1]
        after = line.split(" ")[7]
        steps[after].append(first)
        all_steps.update(first, after)

    all_steps = sorted(list(all_steps))

    while len(all_steps):
        for after in all_steps:
            if all(first_steps in built for first_steps in steps[after]):
                built.append(after)
                all_steps.remove(after)
                break

    return "".join(built)
    
result = solve() 
print(f"Solution: {result}")