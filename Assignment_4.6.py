import random

num_of_points = int(input("Enter number of points to be generated: "))

points_incirlce = 0
i = 0

while i < num_of_points:

    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2 + y**2 < 1:
        points_incirlce += 1
    
    i += 1

pi = 4 * (points_incirlce/num_of_points)

print(f"Approximation for the value of pi is {pi}")