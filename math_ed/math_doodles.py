import math

# print the area and the perimeter and the diagonal of a rectangle

l = 5
w = 3


def rectangle_area(l, w):
    return l * w

def rectangle_perimeter(l, w):
    return 2 * (l + w)

def rectangle_diagonal(l, w):
    return math.sqrt(l**2 + w**2)

print(f"The area of a rectangle with length {l} and width {w} is {rectangle_area(l, w)}")
print(f"The perimeter of a rectangle with length {l} and width {w} is {rectangle_perimeter(l, w)}")
print(f"The diagonal of a rectangle with length {l} and width {w} is {rectangle_diagonal(l, w)}")
