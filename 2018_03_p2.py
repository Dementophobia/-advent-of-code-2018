from aoc import get_ints, read_file, timer
from collections import defaultdict

@timer
def solve():
    input = [get_ints(line) for line in read_file("03")]
    field = defaultdict(int)

    for line in input:
        c_x, c_y, l_x, l_y = line[1:]
 
        for x_pos in range(l_x):
            for y_pos in range(l_y):
                field[(x_pos + c_x, y_pos + c_y)] += 1
 
    for line in input:
        c_num, c_x, c_y, l_x, l_y = line
 
        if not sum(field[(x_pos + c_x, y_pos + c_y)] > 1 for x_pos in range(l_x) for y_pos in range(l_y)):
            return c_num

result = solve() 
print(f"Solution: {result}")