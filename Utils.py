import numpy as np
import tkinter as tk
import math

class Utils:
    @staticmethod
    def isInsidePolygon(point, polygon):
        
        segment = np.array([[point[0], point[0]],[point[1]+1e5, point[1]]])
        nbrIntersection = 0
        for i in range(polygon.shape[1] -1):

            intersection = Utils.segIntersect(segment[:,0],segment[:,1],polygon[:,i],polygon[:,i+1])
            if((intersection != np.array([None, None])).any()):
                nbrIntersection+=1

        if(nbrIntersection%2 ==1):
            print(nbrIntersection, "is inside")
            return True
        else:
            return False

    @staticmethod
    def polygonArea(polygon):
        n = polygon.shape[1] 
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += polygon[i,0] * polygon[j,1]
            area -= polygon[j,0] * polygon[i,1]
            area = abs(area) / 2.0
            return area

    @staticmethod
    def perp(a) :
        b = np.empty_like(a)
        b[0] = -a[1]
        b[1] = a[0]
        return b

    
    #find the intersection point between (A1B1)
    #and (A2B2), and return it if it's in [A2B2]
    #and [A1B1] else return [None,None]
    @staticmethod
    def segIntersect(A1,B1,A2,B2):
        NoneA = np.array([None, None])
        A1B1Vertical=False
        A2B2Vertical=False
        if(B1[0]-A1[0]!=0):
            a1=(B1[1]-A1[1])/(B1[0]-A1[0])
        else:
            a1=0
            A1B1Vertical=True
        if(B2[0]-A2[0]!=0):
            a2=(B2[1]-A2[1])/(B2[0]-A2[0])
        else:
            a2=0
            A2B2Vertical=True
    
        if(A1B1Vertical==True and A2B2Vertical==True):
            if(A1[0]!=A2[0] or B1[0]!=B2[0]):
                print("pas d'intersection")
                return NoneA;
            else:
                print("Il y a une infinité d'intersection")
                return NoneA;

        b1=B1[1]-a1*B1[0]
        b2=B2[1]-a2*B2[0]

        intersection=np.zeros(2)
        if(A1B1Vertical==True):
            intersection[0]=A1[0]
            intersection[1]=a2*A1[0]+b2

        if(A2B2Vertical==True):
            intersection[0]=A2[0]
            intersection[1]=a1*A2[0]+b1

        if(A2B2Vertical==False and A1B1Vertical==False):
            if(a1-a2!=0):
                intersection[0]=(b2-b1)/(a1-a2)
            else:
                print("no intersection return the first argument of the function")
                return NoneA;
            intersection[1]=a1*intersection[0]+b1

        if(Utils.pointInSegment(A2,B2,intersection) and Utils.pointInSegment(A1,B1,intersection)):
            return intersection
        else:
            return NoneA


    #return true if C is in [OM]
    @staticmethod
    def pointInSegment(O,M,C):
        vecOM=np.zeros(2)
        vecOM[:]=M[:]-O[:]
        vecOC=np.zeros(2)
        vecOC[:]=C[:]-O[:]
        prodOM=vecOM@vecOM
        prodOC=vecOM@vecOC
        if prodOC<0:
            return False
        if prodOC>prodOM:
            return False
        return True

    @staticmethod
    def create_point(canvas:tk.Canvas,x,y,size, color):
        canvas.create_oval(x-size, y-size, x+size, y+size,fill=color)