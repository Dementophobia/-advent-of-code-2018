from aoc import get_ints, read_file, timer

@timer
def solve():
    input  = read_file("06")
    points = [tuple(get_ints(line)) for line in input]
    
    x_coords, y_coords = list(zip(*points))
    top, left, bottom, right = min(y_coords), min(x_coords), max(y_coords), max(x_coords)

    return sum(sum(abs(point[0]-x) + abs(point[1]-y) for point in points) < 10000 for x in range(left, right+1) for y in range(top, bottom+1))
    
result = solve() 
print(f"Solution: {result}")