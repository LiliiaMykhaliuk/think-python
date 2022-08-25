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

import turtle

class Point:
    """Represents point on the coordinate grid"""


    def __init__(self, x, y):
        self.x = x
        self.y = y



class Circle:
    """Represents circle on the coordinate grid"""


    def __init__(self, center_point_x, center_point_y, radius):
        self.center = Point(center_point_x, center_point_y)
        self.radius = radius


    def draw_circle(self):
        """Draws circle with Turtle library"""

        # Create initial point
        circle_turtle = turtle.Turtle()

        # Put turtle's center into the given point
        circle_turtle.hideturtle()
        circle_turtle.penup()
        circle_turtle.goto(self.center.x, self.center.y)
        circle_turtle.showturtle()
        circle_turtle.pendown()

        # Draw a circle with given radius
        circle_turtle.circle(self.radius)

        # Clear everything and hide the turtle
        circle_turtle.clear()
        circle_turtle.hideturtle()




class Rectangle():
    """Represents rectangle on the coordinate grid"""


    def __init__(self, Ax, Ay, height, width):

        self.left_down_corner = Point(Ax, Ay)
        self.height = height
        self.width = width

        # Set other corners
        self.right_down_corner = Point(Ax + height, Ay)
        self.left_up_corner = Point(Ax, Ay + width)
        self.right_up_corner = Point(Ax + height, Ay + width)



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

        # Clear everything and hide the turtle
        rectangle.clear()
        rectangle.hideturtle()


# Draw rectangle
rectangle_1 = Rectangle(10, 10, 50, 30)
rectangle_1.draw_rectangle()

# Draw circle
circle_1 = Circle(30, 30, 49)
circle_1.draw_circle()
