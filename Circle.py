# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:42:53 2021

@author: fahim.ahmad
"""
from Shape import Shape

class Circle(Shape):
    
    pi = 3.1416
    
    def __init__(self, centerPointX, centerPointY, radius):
        self.centerPointX = centerPointX
        self.centerPointY = centerPointY
        self.radius = radius 
        
    def getCenterPointX(self):
        return self.centerPointX
    
    def getCenterPointY(self):
        return self.centerPointY
    
    def getRadius(self):
        return self.radius 
        
    def setCenterPoint(self, centerPointX, centerPointY):
        self.centerPointX = centerPointX
        self.centerPointY = centerPointY
    
    def setRadius(self, radius):
        self.radius = radius
        
    def area(self):
        return self.pi * self.radius * self.radius
        
    def perimeter(self):
        return 2 * self.pi * self.radius
        
    def contains(self, x, y):
        if (x - self.centerPointX)**2 + (y-self.centerPointY)**2 <= self.radius**2:
            return True
        else:
            return False
        
    def toString(self, text):
        return str(text)