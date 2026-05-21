from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Usage
c = Circle(5)
print(c.area())

# Key points:

# Abstract classes cannot be instantiated directly.
# Forces subclasses to implement abstract methods.