from point import direction, Point

def extreme_segments(points: list) -> list:
    """
    Given a sets of points, returns its convex hull
    with extreme segments algorithm. 
    """
    n = len(points)
    convex_hull = set() 
    for i in range(0, n):
        for j in range(i + 1, n):
            p = points[i]
            q = points[j]
            if is_extreme_segment(p, q, points):
                convex_hull.add(p)
                convex_hull.add(q)
    
    return list(convex_hull)


def is_extreme_segment(p: Point, q: Point, points: list) -> bool:
    """
    Given two points, p and q, returns if the segment pq is
    extreme.
    """
    initial_orientation = None
    for r in points:
        if r == p or r == q:
            continue
    
        if not initial_orientation:
            initial_orientation = direction(p, q, r)
        else:
            new_orientation = direction(p, q, r)
            if not new_orientation == initial_orientation:
                return False        
    
    return True
