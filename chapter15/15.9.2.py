'''
Exercises of the book "Think python"
15.9.2 Exercise:
'''

# Write a function called draw_rect that takes a Turtle object and 
# a Rectangle and uses the Turtle to draw the Rectangle. 
# See Chapter 4 for examples using Turtle objects.
# 
# Write a function called draw_circle that takes a Turtle and 
# a Circle and draws the Circle.
# 
# Solution: http://thinkpython2.com/code/draw.py.

import math
import turtle

class Point:
    """Represents point on the coordinate grid"""


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_between_points(self, pointA, pointB):
        """Calculate distance to another point"""

        distance = math.sqrt((pointA.x - pointB.x)**2 + (pointA.y - pointB.x)**2)
        return distance



class Circle:
    """Represents circle on the coordinate grid"""


    def __init__(self, center, radius):
        self.center = center
        self.radius = radius



class Rectangle(Point):
    """Represents rectangle on the coordinate grid"""


    def __init__(self, cornerA, cornerB, cornerC, cornerD):
        self.cornerA = cornerA
        self.cornerB = cornerB
        self.cornerC = cornerC
        self.cornerD = cornerD

        self.height = self.get_height()
        self.width = self.get_width()

    def get_height(self):
        """Calculate height of the rectangle"""

        # Calculate two possible heights 
        distance_A_B = super().get_distance_between_points(self.cornerA, self.cornerB)
        distance_A_C = super().get_distance_between_points(self.cornerA, self.cornerC)

        # Choose height
        if distance_A_B > distance_A_C:
            height = distance_A_B
        else:
            height = distance_A_C
        
        return height


    def get_width(self):
        """Calculate width of the rectangle"""

        # Calculate two possible widths 
        distance_A_B = super().get_distance_between_points(self.cornerA, self.cornerB)
        distance_A_C = super().get_distance_between_points(self.cornerA, self.cornerC)

        # Choose width
        if distance_A_B < distance_A_C:
            width = distance_A_B
        else:
            width = distance_A_C
        
        return width


    def draw_rectangle(self):
        """Draws rectangle with Turtle library"""

        # Create initial point
        rectangle = turtle.Turtle()

        # Draw rectangle
        rectangle.fd(self.height)
        rectangle.lt(90)
        rectangle.fd(self.width)
        rectangle.lt(90)
        rectangle.fd(self.height)
        rectangle.lt(90)
        rectangle.fd(self.width)
        turtle.mainloop()



rectangle = Rectangle(Point(10, 10), Point(130, 100), Point(130, 130), Point(100, 130))
rectangle.draw_rectangle()
