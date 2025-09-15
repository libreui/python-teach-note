from turtle import *
class Maze:
    def __init__(self, maze_file_name):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []

        with open(maze_file_name, 'r') as maze_file:
            for line in maze_file:
                row_list = []
                col = 0
                for ch in line[:-1]:
                    row_list.append(ch)
                    if ch == 'S':
                        self.start_row = rows_in_maze
                        self.start_col = col
                rows_in_maze += 1
                self.maze_list.append(row_list)
                columns_in_maze = len(row_list)

        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = -columns_in_maze / 2
        self.y_translate = -rows_in_maze / 2
        self.t = Turtle(shape='turtle')
        setup(width=600, height=600)
        setworldcoordinates(-(columns_in_maze - 1) / 2-.5,
                            -(rows_in_maze - 1) / 2-.5,
                            (columns_in_maze - 1) / 2-.5,
                            (rows_in_maze - 1) / 2-.5)

    # def draw_maze(self):
    #     for x in range(self.rows_in_maze):
    #         for y in range(self.columns_in_maze):

    def draw_center_box(self, x, y, color):
        tracer(0)
        self.t.up()
        self.t.goto(x-.5, y-.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.fd(1)
            self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)




if __name__ == '__main__':
    maze = Maze('lv_1.map')
    maze.draw_center_box(100, 100, 'black')

