import math

G = 100

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
    p2, m2 = b2.p, b1.m
    r = [p2[0]-p1[0], p2[1]-p1[1]]
    r_mag = mag(p1, p2)
    try:
        F = [((G*m1*m2)/(math.pow(r_mag, 3)))*r[0],
             ((G*m1*m2)/(math.pow(r_mag, 3)))*r[1]
            ]
    except ZeroDivisionError:
        F = [0, 0]
    b1.mom[0] = F[0]*dt+b1.mom[0]
    b1.mom[1] = F[1]*dt+b1.mom[1]
        
def test():
    pass
    

if __name__=='__main__':
    test()
