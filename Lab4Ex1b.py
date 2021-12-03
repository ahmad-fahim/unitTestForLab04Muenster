# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:11:18 2021

@author: fahim.ahmad
"""

import unittest
import Point


class TestPoint(unittest.TestCase):


    def test_get_X(self):
        test_point  =  Point.Point(15, 35)
        print(self.assertEqual(15, test_point.getX()))
        
if __name__ == '__main__': 
     unittest.main()