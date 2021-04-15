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

    @staticmethod
    def createRoomFromWalls(originWall:Wall):
        room = Room([originWall])
        room.listWalls.clear()
        path = np.zeros((2,1),dtype=int)
        ''' path is defined as follow :
        - the first row : are the current path choose for example for i we choose connectWall.connectToEnd[i]
        - the second row : are the total path available len(connectWall.connectToEnd[i])
        '''
        path[0,0] =  0

        path[1,0] = len(originWall.connectToEnd) - 1
        room.listWalls.append(originWall)
        nbrIter = 0
        nbrIterMax = 100
        connectWall = originWall
        while nbrIter < nbrIterMax:
            nbrIter+=1
            addPath = np.zeros((2,1), dtype=int)
            addPath[0,0] =  0
            addPath[1,0] = len(connectWall.connectToEnd) - 1 
            path = np.concatenate((path, addPath), axis = 1)
            
            connectWall = connectWall.connectToEnd[path[0,-1]]

            if(connectWall.ID == originWall.ID):
                break

            for wall in room.listWalls:

                if wall.ID == connectWall.ID and wall.ID :
                    for i in range(np.shape(path)[1]):
                        deleteAfterIndex = np.shape(path)[1]+1
                        if path[0,i] < path[1,i]:
                            path[0,i] += 1
                            deleteAfterIndex = i+1
                        if(i >= deleteAfterIndex):
                            path = np.delete(path, i ,axis=1)
                            room.listWalls.pop(i)
            
            
            room.listWalls.append(connectWall)
            
        room.updatePolygon()
        return room

        
