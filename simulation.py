from physics import Body, gForce
import random

if __name__=='simulation':
    n_of_bodies = int(input("Enter number of bodies = "))
dt = .001
bodies = []

def objList():
    for thing in range(n_of_bodies):
        b = Body(random.randint(1, 100),
                 [random.randint(0,500), random.randint(0,500)],
                 [random.randint(-100,100), random.randint(-100,100)]
                 )
        bodies.append(b)
    return bodies

def simulate():
    for body in bodies:
        for b in bodies:
            gForce(body, b, dt)
    for body in bodies:
        body.vmove(dt)
    return bodies
     
def test():
    objList()
    simulate()
    for body in bodies:
        print(body.m, body.p, body.mom)

if __name__=='__main__':
    test()
