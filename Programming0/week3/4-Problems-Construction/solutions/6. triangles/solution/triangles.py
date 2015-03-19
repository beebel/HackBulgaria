from triangles_test_data import generate_triangle_test
from random import randint
import math

def is_triangle(triangle):
    result = False
    if triangle[0] < triangle[1] + triangle[2]:
        if triangle[0] > abs(triangle[1] - triangle[2]):
            if triangle[0] > abs(triangle[2] - triangle[1]):
                result = True

    return result

def area(triangle):
    p = sum(triangle) / 2
    area = math.sqrt(p*(p - triangle[0])*(p - triangle[1])*(p - triangle[2]))

    return area

def is_pythagorean(triangle):
    if pow(triangle[0], 2) == pow(triangle[1], 2) + pow(triangle[2], 2):
        return True
    elif pow(triangle[1], 2) == pow(triangle[0], 2) + pow(triangle[2], 2):
        return True
    elif pow(triangle[2], 2) == pow(triangle[0], 2) + pow(triangle[1], 2):
        return True
    else:
        return False

def generate_triangles(maxTriangles):
    result = []
    i = 0
    while i < randint(2, maxTriangles):
        triangle = generate_triangle_test(10)
        if is_triangle(triangle):
            result.append(triangle)
            i += 1

    return result

def biggest_area(triangles):
    biggest = 0
    indexBiggestTriangle = 0
    for i in range(len(triangles)):
        if area(triangles[i]) > biggest:
            biggest = area(triangles[i])
            indexBiggestTriangle = i

    return triangles[indexBiggestTriangle]
    
def main():
    triangle = generate_triangle_test(10)
    print(triangle)
    print()
    isTriangle = is_triangle(triangle)
    print("is triangle: " + str(isTriangle))
    if isTriangle:
        print("area: " + str(area(triangle)))
        print("is pythagorean: " + str(is_pythagorean(triangle)))
    print()
    triangles = generate_triangles(5)
    print("triangles: " + str(triangles))
    print()
    print("max area triangles: " + str(biggest_area(triangles)))
    
    

if __name__ == "__main__":
    main()
