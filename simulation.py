from physics import Body, gForce
import random

n_of_bodies = 10
bodies = []

for thing in range(n_of_bodies):
    b = Body(random.randint(1, 100),
             [random.randint(-100,100), random.randint(-100,100)],
             [random.randint(-100,100), random.randint(-100,100)]
             )
    bodies.append(b)
