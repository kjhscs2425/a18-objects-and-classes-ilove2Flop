# -*- coding: utf-8 -*-
import turtle
turtle.penup()
turtle.hideturtle()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        turtle.goto(self.x, self.y)
        turtle.dot(5, "black")  # Draw a small dot at the point
        turtle.write(str(self), align="left", font=("Arial", 10, "normal"))

# Create 4 point objects
p1 = Point(0, 0)
p2 = Point(100, 0)
p3 = Point(100, 100)
p4 = Point(0, 100)

# Print points
print(p1)
print(p2)
print(p3)
print(p4)

# Draw points
p1.draw()
p2.draw()
p3.draw()
p4.draw()

turtle.exitonclick()
