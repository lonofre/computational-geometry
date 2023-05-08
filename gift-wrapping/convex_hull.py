import sys
from jarvis_march import jarvis_march
from point import Point

def calculate_convex_hull():
    data = sys.stdin.read()
    lines = data.split(',')
    points = list(map(line_to_point, lines))
    convex_hull  = jarvis_march(points)
    result = list(map(lambda x: f'{x.id}\n', convex_hull))
    with open('solution.txt', 'w') as f:
        f.write(''.join(result))    

def line_to_point(line: str) -> Point:
    data = line.split(':')
    x = float(data[1])
    y = float(data[2])
    return Point(data[0], x, y)


if __name__ == "__main__":
    calculate_convex_hull()
