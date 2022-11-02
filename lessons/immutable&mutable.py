
from __future__ import annotations

class Point:
    """Mode a 2d point."""

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a point with x and y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies by float."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: float) -> Point:
        """Pure method that doesn't mutate the point."""
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled


p0: Point  = Point(1.0, 2.0)
p0.scale_by(2.0)
p1: Point = p0.scale_by(2.0)
print(f"P0: (({p0.x}, {p0.y})) - P1: ({p1.x}, {p1.y})")