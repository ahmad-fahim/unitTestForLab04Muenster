# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:25:47 2021

@author: fahim.ahmad
"""

from Shape import Shape
import math


class Point(Shape):
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def setPosition(self, x, y):
        self.x = x 
        self.y = y
    
    def toString(self):
        return "Point ( " + str(self.x) + ", " + str(self.y) + " )"
    
    def distance(self, x , y):
        dist = round(math.sqrt( pow(x - self.x, 2) + pow(y - self.y, 2)),1)
        return dist
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y
        
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y