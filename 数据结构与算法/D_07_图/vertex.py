class Vertex:
    """图中顶点的实现类
    用于表示图中的一个顶点，包含顶点标识符及其连接关系
    """

    def __init__(self, key):
        """初始化顶点对象
        
        Args:
            key: 顶点的唯一标识符
        """
        self.id = key  # 顶点的唯一标识符
        self.connected_to = {}  # 存储与当前顶点相邻的顶点及其权重的字典
        self.distance = 0 # 起始顶点到当前顶点的距离，初始化为0
        self.predecessor = None
        self.color = 'white'
        self.discovery = 0  # 顶点被发现的时间戳
        self.finish = 0  # 顶点完成探索的时间戳

    def add_neighbor(self, nbr, weight=0):
        """添加一个相邻顶点及其连接权重
        
        Args:
            nbr: 相邻顶点对象
            weight: 边的权重，默认为0
        """
        self.connected_to[nbr] = weight

    def __str__(self):
        """返回顶点的字符串表示，包含顶点ID及其所有连接的顶点ID
        
        Returns:
            str: 顶点及其连接关系的字符串表示
        """
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        """获取当前顶点连接的所有顶点
        
        Returns:
            dict_keys: 所有相邻顶点对象的集合
        """
        return self.connected_to.keys()

    def get_id(self):
        """获取顶点的唯一标识符
        
        Returns:
            顶点的ID值
        """
        return self.id

    def get_weight(self, nbr):
        """获取当前顶点到指定相邻顶点的边权重
        
        Args:
            nbr: 相邻顶点对象
        
        Returns:
            int/float: 边的权重值
        """
        return self.connected_to[nbr]

    # distance 属性的 getter 和 setter
    def get_distance(self):
        """获取顶点的距离值
        
        Returns:
            int: 顶点的距离值
        """
        return self.distance

    def set_distance(self, distance):
        """设置顶点的距离值
        
        Args:
            distance: 要设置的距离值
        """
        self.distance = distance

    # predecessor 属性的 getter 和 setter
    def get_predecessor(self):
        """获取顶点的前驱顶点
        
        Returns:
            Vertex or None: 前驱顶点对象，如果没有则为None
        """
        return self.predecessor

    def set_predecessor(self, predecessor):
        """设置顶点的前驱顶点
        
        Args:
            predecessor: 前驱顶点对象
        """
        self.predecessor = predecessor

    # discovery 属性的 getter 和 setter
    def get_discovery(self):
        """获取顶点被发现的时间戳
        
        Returns:
            int: 顶点被发现的时间戳
        """
        return self.discovery

    def set_discovery(self, discovery):
        """设置顶点被发现的时间戳
        
        Args:
            discovery: 要设置的发现时间戳
        """
        self.discovery = discovery

    # finish 属性的 getter 和 setter
    def get_finish(self):
        """获取顶点完成探索的时间戳
        
        Returns:
            int: 顶点完成探索的时间戳
        """
        return self.finish

    def set_finish(self, finish):
        """设置顶点完成探索的时间戳
        
        Args:
            finish: 要设置的完成探索时间戳
        """
        self.finish = finish

    # color 属性的 getter 和 setter
    def get_color(self):
        """获取顶点的颜色标记
        
        Returns:
            str: 顶点的颜色标记
        """
        return self.color

    def set_color(self, color):
        """设置顶点的颜色标记
        
        Args:
            color: 要设置的颜色标记（通常为'white'、'gray'或'black'）
        """
        self.color = color
