# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:18:06 2021

@author: fahim.ahmad
"""

from Shape import Shape


class Rectangle(Shape):
    
    def __init__(self, topLeftPoint, width, height):
        self.topLeftPoint = topLeftPoint
        self.width = width
        self.height = height
        
    def getTopLeftPointX(self):
        return self.topLeftPoint.x
    
    def getTopLeftPointY(self):
        return self.topLeftPoint.y
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        
    def setTopLeftPoint(self, topLeftPointX, topLeftPointY):
        self.topLeftPoint.x = topLeftPointX
        self.topLeftPoint.y = topLeftPointY
    
    def setWidth(self, width):
        self.width = width
        
    def setHeight(self, height):
        self.height = height
        
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.height + self.width)
        
    def contains(self, x, y):
        if x >= self.topLeftPoint.x and x <= self.topLeftPoint.x + self.getWidth() and y >= self.topLeftPoint.y and y <= self.topLeftPoint.y + self.getHeight():
            return True
        else:
            return False
        
    def centroid(self):
        xCentroid = (self.topLeftPoint.x + self.getWidth() ) / 2
        yCentroid = (self.topLeftPoint.x + self.getHeight() ) / 2
        return xCentroid, yCentroid
        
    def toString(self):
        return "Rectangle [topLeftPoint = " + self.topLeftPoint.toString() + ") , Width = " + str(self.getWidth()) + ", Height = " + str(self.getHeight()) + "]"
    
    