from aoc import read_file, timer

@timer
def solve():
    input = read_file("01")
    return sum([int(x) for x in input])

result = solve()
print(f"Solution: {result}")
