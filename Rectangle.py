# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:18:06 2021

@author: fahim.ahmad
"""

from Shape import Shape

class Rectangle(Shape):
    
    def __init__(self, topLeftPointX, topLeftPointY, width, height):
        self.topLeftPointX = topLeftPointX 
        self.topLeftPointY = topLeftPointY
        self.width = width
        self.height = height
        
    def getTopLeftPointX(self):
        return self.topLeftPointX
    
    def getTopLeftPointY(self):
        return self.topLeftPointY
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        
    def setTopLeftPoint(self, topLeftPointX, topLeftPointY):
        self.topLeftPointX = topLeftPointX
        self.topLeftPointY = topLeftPointY
    
    def setWidth(self, width):
        self.width = width
        
    def setHeight(self, height):
        self.height = height
        
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.height + self.width)
        
    def contains(self, x, y):
        if x >= self.topLeftPointX and x <= self.topLeftPointX + self.getWidth() and y >= self.topLeftPointY and y <= self.topLeftPointY + self.getHeight():
            return True
        else:
            return False
        
    def centroid(self):
        xCentroid = (self.topLeftPointX + self.getWidth() ) / 2
        yCentroid = (self.topLeftPointY + self.getHeight() ) / 2
        return xCentroid, yCentroid
        
    def toString(self, text):
        return str(text)