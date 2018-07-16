"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

from numpy.random import random

'''
area of a circle = pi*r^2
area of square with circle inside (side lengths = d = 2r) = (2r)^2 = 4*r^2

ratio (area of circle)/(area of square) = pi*r^2/4*r^2 = pi/4
pi = 4(area of circle)/(area of square)

randomly pick points within square, see how frequently it lands inside the circle (check using x^2+y^2=r^2)
stop program at the iteration where it correctly approximates the first 3 decimals of pi
'''

pi = 3.141  # first 3 decimals
r = 1
r_sq = r**2
inside_circle = 0
inside_square = 0

while True:
    sample_x = random()
    if random() >= 0.5:
        sample_x *= -1
    sample_y = random()
    if random() >= 0.5:
        sample_y *= -1

    inside_square += 1
    if sample_x**2 + sample_y**2 <= r_sq:
        inside_circle += 1

    if inside_square == 0:
        continue

    pi_approx = round(4*inside_circle/inside_square, 3)

    if pi_approx == pi:
        break

print('Iterations required to approximate pi to 3 decimals:', inside_circle+inside_square)