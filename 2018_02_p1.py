from aoc import read_file, timer
from collections import defaultdict

def update(box, doub, trip):
    cont = defaultdict(int)
 
    for char in box:
        cont[char] += 1

    doub += min(1, list(cont.values()).count(2))
    trip += min(1, list(cont.values()).count(3))

    return doub, trip

@timer
def solve():
    boxes = read_file("02")
    doub, trip = 0, 0

    for box in boxes:
        doub, trip = update(box, doub, trip)
  
    return doub * trip
 
result = solve() 
print(f"Solution: {result}")