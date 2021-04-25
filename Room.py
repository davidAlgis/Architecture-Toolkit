from Selectable import *
from Wall import *
import numpy as np
from Utils import * 

nbrRoom = 0

class Room(Selectable):
    def __init__(self, listWalls:[Wall]):
        global nbrRoom
        if(listWalls == []):
            print("Error - Can't create an room with no walls")
        self.listWalls = listWalls

        Selectable.__init__(self)
        self.ID = "Room_" + str(nbrRoom)
        nbrRoom += 1

    def updatePolygon(self):
        self.polygon = np.zeros((2,len(self.listWalls) + 1))
        self.polygon[:,0] = self.listWalls[0].origin
        for i in range(1, len(self.listWalls)):
            if self.listWalls[i].origin[0] != self.polygon[0,i] and self.listWalls[i].origin[1] != self.polygon[1,i]:
                self.polygon[:,i] = self.listWalls[i].origin
            else:
                self.polygon[:,i] = self.listWalls[i].end
        self.polygon[:,-1] = self.listWalls[0].origin

    #create a room from a wall and the wall connected to him
    @staticmethod
    def createRoomFromWalls(originWall:Wall):
        #the wedge have to be updated
        for wedge in originWall.originWedge:
            print("computation on wall")    

        
