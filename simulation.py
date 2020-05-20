from physics import Body, gForce
import random

n_of_bodies = 10
dt = .00001
bodies = []

for thing in range(n_of_bodies):
    b = Body(random.randint(1, 100),
             [random.randint(-100,100), random.randint(-100,100)],
             [random.randint(-100,100), random.randint(-100,100)]
             )
    bodies.append(b)

while True:
    for body in bodies:
        b_i = bodies.index(body)
        bodies_2 = bodies[b_i+1:n_of_bodies-1]
        for b in bodies_2:
            gForce(body, b, dt)
    for body in bodies:
        body.vmove(dt)

    print(bodies[0].p)
        
