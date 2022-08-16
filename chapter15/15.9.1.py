'''
Exercises of the book "Think python"
15.9.1 Exercise:
'''

# Write a definition for a class named Circle with attributes center and radius, 
# where center is a Point object and radius is a number.
# 
# Instantiate a Circle object that represents a circle with its center at 
# (150, 100) and radius 75.
# 
# Write a function named point_in_circle that takes a Circle and a Point and 
# returns True if the Point lies in or on the boundary of the circle.
# 
# Write a function named rect_in_circle that takes a Circle and a Rectangle and 
# returns True if the Rectangle lies entirely in or on the boundary of the circle.
# 
# Write a function named rect_circle_overlap that takes a Circle and a Rectangle and 
# returns True if any of the corners of the Rectangle fall inside the Circle. Or as a 
# more challenging version, return True if any part of the Rectangle falls inside the Circle.
# 
# Solution: http://thinkpython2.com/code/Circle.py.

import math


class Point:
    """Represents point on the coordinate grid"""


    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    """Represents circle on the coordinate grid"""


    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


    def get_distance_from_center(self, point):
        """Counts distance from the point to the circle center"""

        distance = math.sqrt((self.center.x - point.x)**2 + (self.center.y - point.y)**2)
        return distance


    def point_in_circle(self, point):
        """Checks if the point is in the circle"""

        # Count distance between center and point
        distance_to_center = self.get_distance_from_center(point)

        # Check if the point is inside the circle
        if distance_to_center <= self.radius:
            return True
        return False


    def rect_in_circle(self, points_list):
        """Checks if rectangle is in the circle"""

        # Check if all rectangle corners are inside circle
        for corner_point in points_list:
            if not self.point_in_circle(corner_point):
                return False
        return True


    def rect_circle_overlap(self, points_list):
        """Checks if any rectangle corner falls inside the circle"""

        for corner_point in points_list:
            if self.point_in_circle(corner_point):
                return True
        return False


# Create center of the circle
center_Point = Point(150, 100)

# Create new circle
new_circle = Circle(center_Point, 75)

# Check if point is in the circle
new_point = Point(157, 90)
print(new_circle.point_in_circle(new_point))

# Check if rectangle is in the circle
rectangle = [Point(100, 100), Point(130, 100), Point(130, 130), Point(100, 130)]
print(new_circle.rect_circle_overlap(rectangle))

# Check if any corner of rectangle is in the circle
rectangle2 = [Point(110, 110), Point(170, 110), Point(170, 170), Point(110, 170)]
print(new_circle.rect_in_circle(rectangle2))
