# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:11:18 2021

@author: fahim.ahmad
"""

import unittest
import Point
import Rectangle
import Circle

class TestPoint(unittest.TestCase):
    
    def test_get_StrokeWidth(self):
        test_point = Point.Point(10,10)
        test_point.setStrokeWidth(3) 
        
        self.assertEqual(3, test_point.getStrokeWidth())
        self.assertNotEqual(4, test_point.getStrokeWidth())
        
    def test_get_StrokeColor(self):
        test_point = Point.Point(10,10)
        test_point.setStrokeColor("golden") 
        
        self.assertEqual("golden", test_point.getStrokeColor())
        self.assertNotEqual("fff", test_point.getStrokeColor())
        
    def test_get_FillColor(self):
        test_point = Point.Point(10,10)
        test_point.setFillColor("red") 
        
        self.assertEqual("red", test_point.getFillColor())
        self.assertNotEqual("dfak", test_point.getFillColor())
        

    def test_get_X(self):
        test_point  =  Point.Point(15, 35)
                
        self.assertEqual(15, test_point.getX())
        self.assertIs(15, test_point.getX())
        self.assertIsNot(153, test_point.getX())
        
    def test_get_Y(self):        
        test_point  =  Point.Point(15, 35)
        
        self.assertEqual(35, test_point.getY())
        self.assertNotEqual(5, test_point.getY())
        
    def test_distance(self):
        test_point = Point.Point(0, 0)
        
        self.assertEqual(5, test_point.distance(4, 3))
        self.assertNotEqual(3, test_point.distance(4, 0)) 
        
        
        
class TestRectangle(unittest.TestCase):
    
    
    def test_get_StrokeWidth(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
        test_rectangle.setStrokeWidth(3) 
        
        self.assertEqual(3, test_rectangle.getStrokeWidth())
        self.assertNotEqual(4, test_rectangle.getStrokeWidth())
  
    def test_get_StrokeColor(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
        test_rectangle.setStrokeColor("golden") 
        
        self.assertEqual("golden", test_rectangle.getStrokeColor())
        self.assertNotEqual("fff", test_rectangle.getStrokeColor())
        
    def test_get_FillColor(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
        test_rectangle.setFillColor("red") 
        
        self.assertEqual("red", test_rectangle.getFillColor())
        self.assertNotEqual("dfak", test_rectangle.getFillColor())
    
    
    def test_get_TopLeftPointX(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
                
        self.assertEqual(4, test_rectangle.getTopLeftPointX())
        self.assertIs(4, test_rectangle.getTopLeftPointX())
        self.assertIsNot(153, test_rectangle.getTopLeftPointX())
        
    def test_get_TopLeftPointY(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
                
        self.assertEqual(6, test_rectangle.getTopLeftPointY())
        self.assertIs(6, test_rectangle.getTopLeftPointY())
        self.assertIsNot(153, test_rectangle.getTopLeftPointY())
        
        
    def test_get_Width(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
                
        self.assertEqual(100, test_rectangle.getWidth())
        self.assertIs(100, test_rectangle.getWidth())
        self.assertIsNot(200, test_rectangle.getWidth())
        
    def test_get_Height(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
                
        self.assertEqual(200, test_rectangle.getHeight())
        self.assertIs(200, test_rectangle.getHeight())
        self.assertIsNot(500, test_rectangle.getHeight())
    
    def test_area(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
        
        self.assertEqual(20000, test_rectangle.area())
        self.assertIsNot(200000, test_rectangle.area())
        
    def test_perimeter(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
        
        self.assertEqual(600, test_rectangle.perimeter())
        self.assertIsNot(40000, test_rectangle.perimeter())
        
    def test_contains(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
        
        self.assertIs(True, test_rectangle.contains(10, 50))
        self.assertIsNot(True, test_rectangle.contains(500, 500))
        
        self.assertTrue(test_rectangle.contains(10, 50))
        self.assertFalse(test_rectangle.contains(500, 500))
        
    def test_centroid(self):
        rectangle_top_left_point = Point.Point(4, 6)
        test_rectangle  =  Rectangle.Rectangle(rectangle_top_left_point, 100, 200)
        
        self.assertEqual((52, 102), test_rectangle.centroid())
        self.assertNotEqual((52, 203), test_rectangle.centroid())
        
class TestCircle(unittest.TestCase):
    
    
    def test_get_StrokeWidth(self):
        circle_center = Point.Point(30, 50)
        test_circle = Circle.Circle(circle_center, 20)
        test_circle.setStrokeWidth(3) 
        
        self.assertEqual(3, test_circle.getStrokeWidth())
        self.assertNotEqual(4, test_circle.getStrokeWidth())
        
    def test_get_StrokeColor(self):
        circle_center = Point.Point(30, 50)
        test_circle = Circle.Circle(circle_center, 20)
        test_circle.setStrokeColor("golden") 
        
        self.assertEqual("golden", test_circle.getStrokeColor())
        self.assertNotEqual("fff", test_circle.getStrokeColor())
        
    def test_get_FillColor(self):
        circle_center = Point.Point(30, 50)
        test_circle = Circle.Circle(circle_center, 20)
        test_circle.setFillColor("red") 
        
        self.assertEqual("red", test_circle.getFillColor())
        self.assertNotEqual("dfak", test_circle.getFillColor())
    
    
    def test_getCenterPointX(self):
        circle_center = Point.Point(30, 50)
        test_circle = Circle.Circle(circle_center, 20)
        
        self.assertEqual(30, test_circle.getCenterPointX())
        self.assertNotEqual(300, test_circle.getCenterPointX())
        
    def test_getCenterPointY(self):
        circle_center = Point.Point(30, 50)
        test_circle = Circle.Circle(circle_center, 20)
        
        self.assertEqual(50, test_circle.getCenterPointY())
        self.assertNotEqual(300, test_circle.getCenterPointY())
        
    def test_getRadius(self):
        circle_center = Point.Point(30, 50)
        test_circle = Circle.Circle(circle_center, 20)
        
        self.assertEqual(20, test_circle.getRadius())
        self.assertNotEqual(10, test_circle.getRadius())
        
    def test_area(self):
        circle_center = Point.Point(30, 50)
        test_circle = Circle.Circle(circle_center, 20)
        
        self.assertEqual(1256.64, test_circle.area())
        self.assertNotEqual(1236.64, test_circle.area())
    
    def test_perimeter(self):
        circle_center = Point.Point(30, 50)
        test_circle = Circle.Circle(circle_center, 20)
        
        self.assertEqual(125.664, test_circle.perimeter())
        self.assertNotEqual(1205.664, test_circle.perimeter())
        
    def test_contains(self):
        circle_center = Point.Point(30, 50)
        test_circle = Circle.Circle(circle_center, 20)
        
        self.assertIs(True, test_circle.contains(10, 50))
        self.assertIsNot(True, test_circle.contains(500, 500))
        
        self.assertTrue(test_circle.contains(10, 50))
        self.assertFalse(test_circle.contains(500, 500))

        
        
if __name__ == '__main__': 
     unittest.main()