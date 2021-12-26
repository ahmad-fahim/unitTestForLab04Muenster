# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:42:53 2021

@author: fahim.ahmad
"""
from Shape import Shape

class Circle(Shape):
    
    pi = 3.1416
    
    def __init__(self, centerPoint, radius):
        self.centerPoint = centerPoint 
        self.radius = radius 
        
    def getCenterPointX(self):
        return self.centerPoint.x
    
    def getCenterPointY(self):
        return self.centerPoint.y
    
    def getRadius(self):
        return self.radius 
        
    def setCenterPoint(self, centerPointX, centerPointY):
        self.centerPoint.x = centerPointX
        self.centerPoint.y = centerPointY
        return True
    
    def setRadius(self, radius):
        self.radius = radius
        return True
        
    def area(self):
        return self.pi * self.radius * self.radius
        
    def perimeter(self):
        return 2 * self.pi * self.radius
        
    def contains(self, x, y):
        if (x - self.centerPoint.x)**2 + (y-self.centerPoint.y)**2 <= self.radius**2:
            return True
        else:
            return False
        
    def toString(self):
        return "Circle [centerPoint = " + self.centerPoint.toString() + ") , radius = " + str(self.radius) + "]"
    
    