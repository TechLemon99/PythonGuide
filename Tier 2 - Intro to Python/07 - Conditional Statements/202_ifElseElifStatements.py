# This program will use if-elif-else statements to determine the type of a triangle
a = 5
b = 5
c = 5
if a == b == c:
  print("Equilateral triangle")
elif a == b or a == c or b == c:
  print("Isosceles triangle")
else:
  print("Scalene triangle")
