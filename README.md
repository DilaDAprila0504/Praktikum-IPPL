# Geometric Area Calculator

This Python script calculates the area of different geometric shapes including triangles, circles, and squares using classes, functions, and objects.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository.
3. Run the script `calculate_area.py` to see the results.

## Implementation

```python
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

class Traps(Shape):
    def __init__(self, name, base1, base2, height):
        super().__init__(name)
        self.base1 = base1
        self.base2 = base2
        self.height = height
```

By : Dila Dwi Aprila