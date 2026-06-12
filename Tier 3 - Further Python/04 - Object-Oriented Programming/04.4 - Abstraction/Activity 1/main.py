from shapey import Circle, Rectangle, Square

def test_shape(shape, shape_name):
    print(f"\nTesting {shape_name}:")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print(f"Area: {shape.area():.2f}")
    print(f"Volume: {shape.volume():.2f}")

def main():
    # Test Circle
    circle = Circle(5)
    test_shape(circle, "Circle (radius=5)")
    
    # Test Rectangle
    rectangle = Rectangle(4, 6, 3)
    test_shape(rectangle, "Rectangle (4x6x3)")
    
    # Test Square
    square = Square(5, 2)
    test_shape(square, "Square (5x5x2)")

if __name__ == "__main__":
    main()