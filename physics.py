import math

G = 1

class Body:

    def __init__(self, mass, position, momentum):
        self.m = mass
        self.p = position
        self.mom = momentum

    def pmove(self, dx, dy):
        self.p[0] = self.p[0]+dx
        self.p[1] = self.p[1]+dy

    def vmove(self, dt):
        self.p[0] = (self.mom[0]/self.m)*dt+self.p[0]
        self.p[1] = (self.mom[1]/self.m)*dt+self.p[1]


def mag(p1, p2):
    a, b = p1[0], p1[1]
    c, d = p2[0], p2[1]
    return math.pow(math.pow(a-c, 2)+math.pow(b-d, 2), .5)

def gForce(b1, b2, dt):
    p1, m1 = b1.p, b1.m
    p2, m2 = b2.p, b1.m2
    r = [p2[0]-p1[0], p2[1]-p1[1]]
    r_mag = mag(p1, p2)
    F = [((G*m1*m2)/(math.pow(r_mag, 3)))*r[0],
         ((G*m1*m2)/(math.pow(r_mag, 3)))*r[1]
        ]
    b1.mom[0] = F[0]*dt+b1.mom[0]
    b1.mom[1] = F[1]*dt+b1.mom[1]
        
def test():
    b1 = Body(20, [10, 20], [0, 0])
    b2 = Body(100, [70, -10], [0, 0])
    gForce = (b1, b2, .001)
    gForce = (b2, b1, .001)
    b1.vmove(.001)
    b2.vmove(.001)
    print(b1.p, b2.p)

if __name__=='__main__':
    test()
