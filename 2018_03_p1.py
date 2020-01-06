from aoc import read_file, timer
from re import findall

@timer
def solve():
    input = [[int(x) for x in findall(r'\d+', line)] for line in read_file("03")]
    field = [[0 for x in range(1000)] for y in range(1000)]

    for line in input:
        c_x, c_y, l_x, l_y = line[1:]
 
        for x_pos in range(l_x):
            for y_pos in range(l_y):
                field[x_pos + c_x][y_pos + c_y] += 1
 
    return sum(field[y][x] > 1 for y in range(1000) for x in range(1000))

result = solve() 
print(f"Solution: {result}")