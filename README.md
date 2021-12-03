# unitTestForLab04Muenster
In this repository, I am uploading all the classes and the unit testcases for the class Shape, Point, Rectangle and Circle class.

Brief Description of this project:
  This project is created to create different shape objects like point, circle and rectangle and their properties. 
  
Description of the files:

  Shape.py: In this files, I have created a class named Shape that describes the basic property of any kind of shapes like width of the stroke, color of the stroke and fill color of the shape. There are getter and setter methods for each property.
  
  Point.py: This file creates another class named Point that inherites the class Shape. There are few property of a shape like X and Y coordinate of the point. This property is described here. There is another method named distance that calculates the distance of a given coordinate from the point object. All the getter and setter methods are there.
  
  Rectangle.py: In this file there is a class named Rectangle that defines all the property of a rectangle like top Left Point and the width and height of the rectangle. There are also methods for calculating area, perimeter and centroid of the rectangle. There is a method named contains that determines whether the given point is inside or outside of the rectangle.
  
  Circle.py: In this file there is a class named Circle that defines all the property of a circle like center point and the radius of the circle. There are also methods for calculating area and perimeter of the circle. There is a method named contains that determines whether the given point is inside or outside of the circle.
  
  Lab4Ex1a.py and Lab4Ex1b.py: This files are the very initial stage of testing a point. Here it is checking whether the getX() method is correctly returning the X coordinate of the point object.
  
  Lab4Ex1c.py: This file is created to test all the properties of the created shapes. There are 3 classes(TestPoint, TestRectangle, TestCircle) to test the characteristics of the methods defined in the classes(Point, Recrangle and Circle). In every method of the test classes in this files, an object is created of the class and after that an expected input is given to the different assert functions. The assert functions test the output from the class method with the expected result.
  
