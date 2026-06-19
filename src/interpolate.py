from typing import Any
from easings import Linear
class Interpolated:
    def __init__(self, start: Any, end: Any, duration: float):
        self.start = start
        self.end = end
        self.duration = duration
        self.elapsed_time = 0.0
        
    def interpolate(self, dt, easing=Linear):
        self.elapsed_time += dt
        t = max(0, min(1, self.elapsed_time / self.duration))
        return self.start + (self.end - self.start) * easing(t)
