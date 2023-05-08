from point import direction, Direction, compare_y_coordinate, Point

def jarvis_march(points: list) -> list:
    """
    Calculates the convex hull of a given list of points
    using jarvis march algorithm
    """
    convex_hull = set()
    min_index = min_point_index(points)
    current_index = min_index
    convex_hull.add(points[current_index])
    n = len(points)

    while True:
        next_index = (current_index + 1) % n
        for i in range(0, n):
            if i == current_index or i == next_index:
                continue
            p = points[current_index]
            q = points[i]
            r = points[next_index]
            current_orientation = direction(p, q, r)
            if current_orientation == Direction.COUNTERCLOCKWISE:
                next_index = i
        
        current_index = next_index
        if current_index == min_index:
            break
        convex_hull.add(points[current_index])
    
    return list(convex_hull)

def min_point_index(points: list) -> Point:
    """
    Returns the index of the point with the smallest
    y coordinate
    """
    min_index = 0
    for i in range(0, len(points)):
        p = points[min_index]
        q = points[i]
        if not compare_y_coordinate(p, q):
            min_index = i
    
    return min_index