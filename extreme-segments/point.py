from dataclasses import dataclass
from enum import Enum

@dataclass
class Point:
    """
    Represents a 2D point.
    """
    id: str
    x: float
    y: float
    
    def __hash__(self):
        return hash(self.id)

class Direction(Enum):
    """
    The direction between three to points.
    """
    COLLINEAR = 1
    CLOCKWISE = 2
    COUNTERCLOCKWISE = 3
    

def direction(p: Point, q: Point, r: Point):
    """
    Gives the direction of a given point r with respect
    to pq segment
    """
    result = (r.y - p.y)*(q.x - p.x) - (q.y - p.y)*(r.x - p.x)
    if result == 0:
        return Direction.COLLINEAR
    elif result > 0:
        return Direction.COUNTERCLOCKWISE
    else:
        return Direction.CLOCKWISE

