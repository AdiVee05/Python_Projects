# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jack Gutacker
#               Cameron Jackson
#               Alan Ngo
#               Aditya Veeramony
# Section:      19
# Assignment:   lab 2.8
# Date:         27 8 2024




"""def no_three_in_line(n):
    points = []
    pointy = [0]
    # Strategy: Place points in a staggered fashion
    points.append((1,0))
    for i in range(n):
        # Use modulo to stagger points on even and odd rows
        if i == 0:
            continue
        for j in range(1,3):
            if i == 1 and j == 1:
                continue
            x = i
            y = (2 * (i*j)) % n
            pointy.append(int(y))
            if pointy.count(int(y)) <=2 :
                points.append((x, int(y)))
    
    return points

# Example usage:
n = 4
points = no_three_in_line(n)
print(points)
"""

import random

def generate_points(n):
    """Generates n random points on an n x n grid."""
    points = []
    while len(points) < n:
        x, y = random.randint(0, n - 1), random.randint(0, n - 1)
        if (x, y) not in points:
            points.append((x, y))
    return points

def is_collinear(p1, p2, p3):
    """Checks if three points are collinear."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

def no_three_in_line(n, max_attempts=1000):
    """Finds n points on an n x n grid with no three in a line."""
    for attempt in range(max_attempts):
        points = generate_points(n)
        collinear = False
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if is_collinear(points[i], points[j], points[k]):
                        collinear = True
                        break
                if collinear:
                    break
            if collinear:
                break
        if not collinear:
            return points
    return None

n = 4
points = no_three_in_line(n)
print(points)
if points:
    print("Points with no three in a line:")
    for point in points:
        print(point)
