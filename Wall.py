from Selectable import *
import numpy as np

class Wall(Selectable):
    def __init__(self, origin:np.array(2, dtype=int), width = 15, length = 100, angle = 0):
        self.origin = origin
        self.width = width
        self.length = length
        self.angle = angle
        self.end = origin
        Selectable.__init__(self)
        

    def updatePolygon(self):
        self.polygon = np.zeros((2,4))
        if(self.end == self.origin):
            print("error - origin and end are the same")
        basis = np.array((2,2))
        basis[:,0] = self.end - self.origin
        
        x = np.linalg.norm(basis[0,:])
        basis[0,0] = basis[0,0]/norm
        basis[1,0] = basis[1,0]/norm

        basis[0,1] = basis[0,0] * self.width
        basis[1,1] = -basis[1,0]* self.width
        self.polygon[:,0] = self.origin + basis[:,1]
        self.polygon[:,1] = self.end + basis[:,1]
        self.polygon[:,2] = self.end - basis[:,1]
        self.polygon[:,3] = self.origin - basis[:,1]


        
