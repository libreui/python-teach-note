import pygame
import sys
import math

class GraphVisualizer:
    """有向图可视化工具类，支持从Graph对象直接生成可视化"""
    def __init__(self, graph=None, width=800, height=600, title="有向图可视化"):
        """初始化可视化环境
        
        Args:
            graph: Graph对象，包含顶点和边的数据
            width: 窗口宽度，默认800
            height: 窗口高度，默认600
            title: 窗口标题，默认"有向图可视化"
        """
        # 初始化pygame
        pygame.init()
        # 设置窗口尺寸和标题
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        # 设置颜色
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        # 顶点和边的数据
        self.vertices = {}
        self.edges = []
        # 顶点的默认样式
        self.vertex_radius = 30
        self.font = pygame.font.SysFont("SimHei", 20)
        # 边的默认样式
        self.edge_width = 2
        # 时钟对象，用于控制帧率
        self.clock = pygame.time.Clock()
        self.running = True
        
        # 如果提供了Graph对象，解析它的数据
        if graph is not None:
            self.load_graph(graph)
    
    def load_graph(self, graph):
        """从Graph对象中加载顶点和边的数据
        
        Args:
            graph: Graph对象
        """
        # 自动布局顶点
        self._auto_layout_vertices(graph)
        
        # 提取边的数据
        self.edges = []
        for vertex in graph:
            for neighbor in vertex.get_connections():
                self.edges.append((vertex.get_id(), neighbor.get_id()))
    
    def _auto_layout_vertices(self, graph):
        """自动布局顶点，使它们均匀分布在屏幕上
        
        Args:
            graph: Graph对象
        """
        vertices = list(graph.get_vertices())
        num_vertices = len(vertices)
        
        # 如果顶点数量为0，直接返回
        if num_vertices == 0:
            return
        
        # 计算顶点的位置，将顶点均匀分布在一个圆上
        center_x = self.width // 2
        center_y = self.height // 2
        radius = min(center_x, center_y) - 100  # 留出边距
        
        for i, vertex_id in enumerate(vertices):
            # 计算角度
            angle = 2 * math.pi * i / num_vertices
            # 计算坐标
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            # 存储顶点数据
            self.vertices[vertex_id] = (x, y, str(vertex_id))
    
    def set_vertices(self, vertices):
        """设置顶点数据
        
        Args:
            vertices: 字典，键为顶点ID，值为(坐标x, 坐标y, 标签)的元组或列表
        """
        self.vertices = vertices
    
    def set_edges(self, edges):
        """设置边数据
        
        Args:
            edges: 列表，元素为(起点ID, 终点ID)的元组或列表
        """
        self.edges = edges
    
    def draw_vertex(self, pos, label):
        """绘制单个顶点
        
        Args:
            pos: 顶点的坐标(x, y)
            label: 顶点的标签
        """
        # 绘制顶点的圆形，背景为白色
        pygame.draw.circle(self.screen, self.WHITE, pos, self.vertex_radius)
        pygame.draw.circle(self.screen, self.BLACK, pos, self.vertex_radius, 2)  # 边框
        # 绘制顶点标签
        text = self.font.render(str(label), True, self.BLACK)
        text_rect = text.get_rect(center=pos)
        self.screen.blit(text, text_rect)
    
    def draw_edge(self, start_pos, end_pos):
        """绘制带箭头的有向边
        
        Args:
            start_pos: 起始点坐标(x, y)
            end_pos: 终点坐标(x, y)
        """
        # 计算从起点到终点的向量
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        # 计算向量的长度
        length = math.sqrt(dx **2 + dy **2)
        # 归一化向量
        if length > 0:
            dx_normalized = dx / length
            dy_normalized = dy / length
        else:
            dx_normalized, dy_normalized = 0, 0
        
        # 计算实际的线条终点（考虑顶点的半径）
        actual_end_x = end_pos[0] - dx_normalized * self.vertex_radius
        actual_end_y = end_pos[1] - dy_normalized * self.vertex_radius
        actual_end_pos = (actual_end_x, actual_end_y)
        
        # 绘制线条
        pygame.draw.line(self.screen, self.BLACK, start_pos, actual_end_pos, self.edge_width)
        
        # 绘制箭头
        self.draw_arrow_head(actual_end_pos, dx_normalized, dy_normalized)
    
    def draw_arrow_head(self, pos, dx, dy):
        """绘制箭头头部
        
        Args:
            pos: 箭头位置
            dx: x方向的归一化向量
            dy: y方向的归一化向量
        """
        arrow_size = 10
        # 计算箭头的两个点
        angle1 = math.pi / 6  # 30度
        angle2 = -math.pi / 6  # -30度
        
        # 计算箭头的两个点
        x1 = pos[0] - arrow_size * (dx * math.cos(angle1) - dy * math.sin(angle1))
        y1 = pos[1] - arrow_size * (dx * math.sin(angle1) + dy * math.cos(angle1))
        x2 = pos[0] - arrow_size * (dx * math.cos(angle2) - dy * math.sin(angle2))
        y2 = pos[1] - arrow_size * (dx * math.sin(angle2) + dy * math.cos(angle2))
        
        # 绘制箭头
        pygame.draw.polygon(self.screen, self.BLACK, [pos, (x1, y1), (x2, y2)])
    
    def draw(self):
        """绘制整个图"""
        # 填充背景色
        self.screen.fill(self.WHITE)
        
        # 先绘制边（这样顶点会在边的上面）
        for edge in self.edges:
            start_id, end_id = edge
            if start_id in self.vertices and end_id in self.vertices:
                start_pos = self.vertices[start_id][:2]  # 获取起点坐标
                end_pos = self.vertices[end_id][:2]  # 获取终点坐标
                self.draw_edge(start_pos, end_pos)
        
        # 再绘制顶点
        for vertex_id, data in self.vertices.items():
            pos = data[:2]  # 获取坐标
            label = data[2] if len(data) > 2 else str(vertex_id)  # 获取标签，如果没有则使用顶点ID
            self.draw_vertex(pos, label)
        
        # 更新显示
        pygame.display.flip()
    
    def run(self):
        """运行可视化主循环"""
        while self.running:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # 绘制图
            self.draw()
            
            # 控制帧率
            self.clock.tick(60)
        
        # 退出pygame
        pygame.quit()
        sys.exit()

# 示例用法，展示如何使用Graph对象
if __name__ == "__main__":
    # 导入Graph类
    from graph import Graph
    
    # 创建Graph对象并添加顶点和边
    g = Graph()
    # 添加顶点和边
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    
    # 创建可视化器实例，并传入Graph对象
    visualizer = GraphVisualizer(g, title="基于Graph对象的有向图可视化")
    
    # 运行可视化
    visualizer.run()