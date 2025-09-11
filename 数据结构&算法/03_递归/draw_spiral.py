# 递归可视化，使用turtle模块绘制螺旋线
from turtle import Turtle
my_turtle = Turtle()
my_win = my_turtle.getscreen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)
draw_spiral(my_turtle, 100)
my_win.exitonclick()
