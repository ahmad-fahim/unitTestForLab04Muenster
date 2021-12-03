# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:31:03 2021

@author: fahim.ahmad
"""

class Shape():
    def __init__(self, strokeWidth, strokeColor, fillColor):
        self.strokeWidth = strokeWidth
        self.strokeColor = strokeColor
        self.fillColor = fillColor
        
    def setStrokeWidth(self, strokeWidth):
        self.strokeWidth = strokeWidth
    
    def setStrokeColor(self, strokeColor):
        self.strokeColor = strokeColor
        
    def setFillColor(self, fillColor):
        self.fillColor = fillColor
        
    def getStrokeWidth(self):
        return self.strokeWidth
    
    def getStrokeColor(self):
        return self.strokeColor
        
    def getFillColor(self):
        return self.fillColor