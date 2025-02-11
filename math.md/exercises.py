#Ex1
import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Input degree: "))
print("Output radian:", round(degree_to_radian(degree), 6))



#Ex2
def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
print("Expected Output:", trapezoid_area(height, base1, base2))


#Ex3
import math

def regular_polygon_area(n, side_length):
    return (n * side_length**2) / (4 * math.tan(math.pi / n))

n = int(input())
side_length = float(input())
print(regular_polygon_area(n, side_length))


#Ex4
def parallelogram_area(base, height):
    return base * height

base = float(input())
height = float(input())
print(parallelogram_area(base, height))

