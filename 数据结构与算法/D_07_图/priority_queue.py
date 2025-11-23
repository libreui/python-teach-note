from vertex import Vertex
class PriorityQueue:
    """
    基于堆实现的优先级队列（最小堆）
    每个元素是一个 (key, priority) 元组，key 是顶点的distance属性，priority 是Vertex对象
    """
