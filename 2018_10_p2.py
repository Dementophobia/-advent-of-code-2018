from aoc import get_ints, read_file, timer

@timer
def solve():
    points = [get_ints(line) for line in read_file("10")]

    result, found, size = 0, 0, 200

    while found < len(points):
        found = 0
        for point in points:
            point[0] += point[2]
            point[1] += point[3]
            if point[0] >= 0 and \
               point[0] < size and \
               point[1] >= 0 and \
               point[1] < size:
                found += 1
        result += 1
    
    return result

result = solve() 
print(f"Solution: {result}")