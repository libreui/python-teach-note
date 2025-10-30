from turtle import *

# 迷宫状态常量定义
PART_OF_PATH = 'O'  # 表示路径的一部分
TRIED = 'X'  # 表示已尝试过的位置
OBSTACLE = '+'  # 表示障碍物
DEAD_END = '#'  # 表示死胡同（尝试后无法通向出口的位置）
EXIT = 'E'  # 表示出口


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
                    col += 1
                rows_in_maze += 1
                self.maze_list.append(row_list)
                columns_in_maze = len(row_list)

        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = -columns_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = Turtle(shape='turtle')
        setup(width=600, height=600)
        setworldcoordinates(-(columns_in_maze - 1) / 2 - .5,
                            -(rows_in_maze - 1) / 2 - .5,
                            (columns_in_maze - 1) / 2 + .5,
                            (rows_in_maze - 1) / 2 + .5)

    def draw_maze(self):
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_center_box(x + self.x_translate,
                                         -y + self.y_translate,
                                         'tan')
        self.t.color('black', 'blue')

    def draw_center_box(self, x, y, color):
        tracer(0)
        self.t.up()
        self.t.goto(x - .5, y - .5)
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

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate,
                                         -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_breadcrumb(self, color):
        self.t.dot(color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.drop_breadcrumb(color)

    def is_exit(self, row, col):
        return (row == 0 or
                row == self.rows_in_maze - 1 or
                col == 0 or
                col == self.columns_in_maze - 1)

    def __getitem__(self, idx):
        return self.maze_list[idx]


def search_from(maze, start_row, start_column):
    maze.update_position(start_row, start_column)
    # 检查基本情况
    # 1. 遇到墙
    if maze[start_row][start_column] == OBSTACLE:
        return False
    # 2. 遇到已经走过的格子
    if maze[start_row][start_column] == TRIED:
        return False
    # 3. 找到出口
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)

    # 4. 调用4个方向递归
    found = search_from(maze, start_row - 1, start_column) or \
            search_from(maze, start_row + 1, start_column) or \
            search_from(maze, start_row, start_column - 1) or \
            search_from(maze, start_row, start_column + 1)
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found


if __name__ == '__main__':
    maze = Maze('lv_1.map')
    maze.draw_maze()
    maze.move_turtle(maze.start_col, maze.start_row)

    search_from(maze, maze.start_row, maze.start_col)
    done()
