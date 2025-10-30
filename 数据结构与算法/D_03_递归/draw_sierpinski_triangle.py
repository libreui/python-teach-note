from turtle import *

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1])
    my_turtle.goto(points[2])
    my_turtle.goto(points[0])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

def sierpinski(points, degree, my_turtle):
    color_map = ['blue', 'green', 'red', 'yellow', 'orange', 'purple']
    draw_triangle(points, color_map[degree], my_turtle)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1, my_turtle)
        sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree - 1, my_turtle)
        sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree - 1, my_turtle)

t = Turtle()
my_win = t.getscreen()
my_points = [(-500, -250), (0, 500), (500, -250)]
sierpinski(my_points, 5, t)
my_win.exitonclick()
