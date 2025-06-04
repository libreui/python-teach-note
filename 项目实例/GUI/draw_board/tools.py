import math

import pygame


def scale_image(image, new_width, new_height):
    """
    按指定的宽度和高度缩放加载的图片。

    :param image: 使用 pygame.image.load 加载的图片 Surface 对象
    :param new_width: 缩放后的图片宽度
    :param new_height: 缩放后的图片高度
    :return: 缩放后的图片 Surface 对象
    """
    # 使用 smoothscale 进行平滑缩放，能得到更好的视觉效果
    scaled_image = pygame.transform.smoothscale(image, (new_width, new_height))
    return scaled_image


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.brush = None
        self.colors = [
            (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),
            (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),
            (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),
            (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),
            (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),
            (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),
            (0xc0, 0xc0, 0xc0), (0x00, 0x00, 0x00),
            (0x80, 0x80, 0x80), (0x00, 0xc0, 0x80)
        ]
        self.eraser_color = (0xff, 0xff, 0xff)
        # 计算每个色块在画板中的坐标，便于绘制
        self.colors_rect = []
        for i, rgb in enumerate(self.colors):
            rect = pygame.Rect(10 + i % 2 * 32, 254 + i / 2 * 32, 32, 32)
            self.colors_rect.append(rect)
        self.pens = [
            scale_image(pygame.image.load(f"img/pencil.png").convert_alpha(), 32, 32)
        ]
        self.erasers = [
            scale_image(pygame.image.load(f"img/erase.png").convert_alpha(), 32, 32)
        ]
        self.erasers_rect = []
        for i, eraser in enumerate(self.erasers):
            rect = pygame.Rect(10, 10 + (i + 1) * 64, 64, 64)
            self.erasers_rect.append(rect)
        self.pens_rect = []
        for i, pen in enumerate(self.pens):
            rect = pygame.Rect(10, 10 + i * 64, 64, 64)
            self.pens_rect.append(rect)
        self.sizes = [
            scale_image(pygame.image.load(f"img/plus.png").convert_alpha(), 32, 32),
            scale_image(pygame.image.load(f"img/minus.png").convert_alpha(), 32, 32)
        ]
        self.sizes_rect = []
        for i, size in enumerate(self.sizes):
            rect = pygame.Rect(10 + i * 32, 138, 32, 32)
            self.sizes_rect.append(rect)


    def set_brush(self, brush):
        self.brush = brush

    def draw(self):
        # 绘制画笔样式按钮
        for i, pen in enumerate(self.pens):
            self.screen.blit(pen, self.pens_rect[i].topleft)

        # 绘制橡皮按钮
        for i, eraser in enumerate(self.erasers):
            self.screen.blit(eraser, self.erasers_rect[i].topleft)

        # 绘制“+”，“-”按钮
        for i, size in enumerate(self.sizes):
            self.screen.blit(size, self.sizes_rect[i].topleft)

        # 绘制用于实时展示画笔的小窗口
        self.screen.fill((255, 255, 255), (10, 180, 64, 64))
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 180, 64, 64), 1)
        size = self.brush.get_size()
        x = 10 + 32
        y = 180 + 32
        # 在窗口中展示画笔
        pygame.draw.circle(self.screen, self.brush.get_color(), (x, y), int(size))
        # 绘制色块
        for i, color in enumerate(self.colors):
            pygame.draw.rect(self.screen, color, self.colors_rect[i])


    def click_button(self, pos):
        """点击按钮事件"""
        # 点击加减号事件
        for i, rect in enumerate(self.sizes_rect):
            if rect.collidepoint(pos):
                if i == 0:
                    self.brush.set_size(self.brush.get_size() + 0.5)
                else:
                    self.brush.set_size(self.brush.get_size() - 0.5)
                return True

        # 点击颜色按钮事件
        for i, rect in enumerate(self.colors_rect):
            if rect.collidepoint(pos):
                self.brush.set_color(self.colors[i])
                return True

        # 点击橡皮事件
        for i, rect in enumerate(self.erasers_rect):
            if rect.collidepoint(pos):
                self.brush.set_color(self.eraser_color)
                return True

        return False



class Brush:
    def __init__(self, screen):
        self.screen = screen
        self.color = (0, 0, 0)
        self.size = 1
        self.drawing = False
        self.last_pos = None
        self.space = 1
        self.brush = scale_image(pygame.image.load(f"img/pencil.png").convert_alpha(), 32, 32)
        self.brush_now = self.brush.subsurface((0, 0), (1, 1))


    def start_draw(self, pos):
        self.drawing = True
        self.last_pos = pos


    def end_draw(self):
        self.drawing = False

    def get_current_brush(self):
        return self.brush_now

    def set_size(self, size):
        if size < 0.5:
            size = 0.5
        elif size > 24:
            size = 24
        self.size = size
        self.brush_now = self.brush.subsurface((0, 0), (size * 2, size * 2))


    def set_color(self, color):
        self.color = color
        # 获取 brush_now 的宽度和高度
        width, height = self.brush_now.get_size()
        for i in range(width):
            for j in range(height):
                if i < self.brush.get_width() and j < self.brush.get_height():
                    # 保留原有的透明度
                    alpha = self.brush_now.get_at((i, j)).a
                    self.brush.set_at((i, j), color + (alpha,))



    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def _get_points(self, pos):
        """
        计算两点之间的所有点。
        """
        points = [(self.last_pos[0], self.last_pos[1])]
        len_x = pos[0] - self.last_pos[0]
        len_y = pos[1] - self.last_pos[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)
        step_x = len_x / length
        step_y = len_y / length
        for i in range(int(length)):
            points.append((points[-1][0]+step_x, points[-1][1]+step_y))
        # 对points中的点进行四舍五入取整
        points = map(lambda x: (int(0.5 + x[0]), int(0.5 + x[1])), points)
        return list(set(points))

    def draw(self, pos):
        if self.drawing:
            for p in self._get_points(pos):
                pygame.draw.circle(self.screen, self.color, p, int(self.size))
            self.last_pos = pos # 更新最后一个点的位置


class Paint:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.brush = Brush(self.screen) # 初始化画笔
        self.menu = Menu(self.screen) # 初始化菜单
        self.menu.set_brush(self.brush) # 设置画笔

    def clear_screen(self):
        self.screen.fill((255, 255, 255))


    def run(self):
        self.clear_screen()
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 处理鼠标点击事件
                    if event.pos[0] <= 74 and self.menu.click_button(event.pos):
                        pass
                    else:
                        self.brush.start_draw(event.pos)
                elif event.type == pygame.MOUSEMOTION:
                    # 处理鼠标移动事件
                    self.brush.draw(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    # 处理鼠标松开事件
                    self.brush.end_draw()
            self.menu.draw()
            pygame.display.update()
