import math

class Body:

    def __init__(self, mass, position, velocity):
        self.m = mass
        self.p = position
        self.v = velocity

    def pmove(self, dx, dy):
        self.p[0] = self.p[0]+dx
        self.p[1] = self.p[1]+dy

    def vmove(self, dt):
        self.p[0] = self.v[0]*dt+self.p[0]
        self.p[1] = self.v[1]*dt+self.p[1]


obj_1 = Body(20,[5,6],[2,5])
obj_1.pmove(2,2)
obj_1.vmove(2)

print(obj_1.m,obj_1.p,obj_1.v)
