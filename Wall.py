from Selectable import *
import numpy as np
from Utils import * 

nbrWall = 0 

class Wall(Selectable):
    
    originWedge = []
    endWedge = []

    def __init__(self, origin:np.array(2, dtype=int), width = 15, length = 100, angle = 0):
        global nbrWall
        self.origin = origin
        self.width = width
        self.length = length
        self.angle = angle
        self.end = origin
        self.connectToOrigin = []
        self.connectToEnd = []
        
        Selectable.__init__(self)
        self.ID = "Wall_" + str(nbrWall)
        nbrWall += 1 

    def updatePolygon(self):
        self.polygon = np.zeros((2,5))
        if((self.end == self.origin).all()):
            print("error - origin and end are the same")
        basis = np.zeros((2,2))

        basis[:,0] = self.end - self.origin
        
        basis = Utils.normalized(basis)
        #norm = np.linalg.norm(basis[0,:])
        #basis[0,0] = basis[0,0]/norm
        #basis[1,0] = basis[1,0]/norm

        basis[0,1] = basis[1,0] * self.width/2
        basis[1,1] = -basis[0,0]* self.width/2
        self.polygon[:,0] = self.origin + basis[:,1]
        self.polygon[:,1] = self.end + basis[:,1]
        self.polygon[:,2] = self.end - basis[:,1]
        self.polygon[:,3] = self.origin - basis[:,1]
        self.polygon[:,4] = self.polygon[:,0]

    def updateWedge(self, listConnection, isOrigin):
        if(isOrigin):
            self.originWedge.clear()
        else:
            self.endWedge.clear()
        anglesBetweenWalls = []
        minWall = self
        minAngle = 360
        maxWall = self
        maxAngle = 0

        if(len(listConnection) == 1):
            wedge = Wedge(self.origin, self.end, getConnectionWall(self, listConnection[1])[3],self, listConnection[1])
            if(isOrigin):
                self.originWedge.append(wedge)
            else:
                self.endWedge.append(wedge)
        elif(len(self.connectToOrigin) > 1):
            minWall = listConnection[0]
            maxWall = listConnection[0]
        else:
            return

        for wall in listConnection:
            anglesBetweenWall = getAngleBetweenWalls(self, wall)
            if(anglesBetweenWall < minAngle):
                minWall = wall
                minAngle = anglesBetweenWall

            if(anglesBetweenWall > maxAngle):
                maxWall = wall
                maxAngle = anglesBetweenWalls

        wedgeMin = Wedge(self.origin, self.end, getConnectionWall(self, minWall)[3], self, minWall)
        wedgeMax = Wedge(self.origin, self.end, getConnectionWall(self, maxWall)[3], self, maxWall)

        if(isOrigin):
            self.originWedge.append(wedgeMin)
            self.originWedge.append(wedgeMax)
        else:
            self.endWedge.append(wedgeMin)
            self.endWedge.append(wedgeMax)
       
    


    #get the connected point between two walls, and return in this order :
    #the connected point of wall1, the other side of wall 1, the other side of wall 2
    @staticmethod
    def getConnectionWalls(wall1:Wall, wall2:Wall):
        if( wall1.origin == wall2.origin):
            return wall1.origin, wall1.end, wall2.end
        elif(wall1.origin == wall2.end):
            return wall1.origin, wall1.end, wall2.origin
        elif(wall1.end == wall2.end):
            return wall1.end, wall1.origin, wall2.origin
        elif(wall1.end == wall2.origin):
            return wall1.end, wall1.origin, wall2.end
        else:
            print("error - cannot calculate angles between to unconnected walls")
        return wall1.origin, wall1.end, wall2.end

    @staticmethod
    def getAngleBetweenWalls(wall1:Wall, wall2:Wall):
        origin, end1, end2 = getConnectionWalls(wall1,wall2)
        direction1 = end1 = origin
        direction2 = end2- origin
        Utils.normalized(direction1)
        Utils.normalized(direction2)

        return np.arccos(np.dot(direction, direction2))

class Wedge():
    def __init__(self, point1, point2, point3, wall1, wall2):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.wall1 = wall1
        self.wall2 = wall2




        
