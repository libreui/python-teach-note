from graph import Graph
from vertex import Vertex


class TopologicalSort:
    """拓扑排序算法实现类
    提供基于DFS的拓扑排序方法
    """

    @staticmethod
    def dfs_topological_sort(graph):
        """使用深度优先搜索实现拓扑排序
        
        算法思路：
        1. 对图中每个未访问的顶点进行DFS
        2. 在DFS过程中，将顶点标记为正在访问
        3. 递归访问所有未访问的邻接顶点
        4. 当顶点的所有邻接顶点都被访问后，将该顶点标记为已访问并加入栈中
        5. 最后将栈中的顶点按顺序弹出，得到拓扑排序结果
        6. 如果在DFS过程中发现回边（即遇到正在访问的顶点），则说明图中存在环
        
        Args:
            graph: 要进行拓扑排序的图对象
            
        Returns:
            list: 拓扑排序结果的顶点ID列表，如果图有环则返回空列表
        """
        # 顶点状态：0=未访问，1=正在访问，2=已访问
        visited = {vertex.get_id(): 0 for vertex in graph}
        result_stack = []
        has_cycle = [False]  # 使用列表作为可变对象传递

        def dfs(vertex_id):
            # 如果顶点正在被访问，说明存在环
            if visited[vertex_id] == 1:
                has_cycle[0] = True
                return

            # 如果顶点已访问，直接返回
            if visited[vertex_id] == 2:
                return

            # 标记顶点为正在访问
            visited[vertex_id] = 1

            # 递归访问所有邻接顶点
            current_vertex = graph.get_vertex(vertex_id)
            for neighbor in current_vertex.get_connections():
                dfs(neighbor.get_id())
                if has_cycle[0]:
                    return  # 如果发现环，立即返回

            # 标记顶点为已访问并加入结果栈
            visited[vertex_id] = 2
            result_stack.append(vertex_id)

        # 对每个未访问的顶点进行DFS
        for vertex_id in visited.keys():
            if visited[vertex_id] == 0:
                dfs(vertex_id)
                if has_cycle[0]:
                    return []  # 存在环，无法完成拓扑排序

        # 反转栈得到拓扑排序结果
        return result_stack[::-1]


# 测试代码
if __name__ == '__main__':
    # 创建一个有向无环图(DAG)
    def create_sample_dag():
        """创建一个示例有向无环图
        图结构:
        0 --> 1 --> 3
        |     |
        v     v
        2     4
        """
        g = Graph()

        # 添加顶点
        for i in range(5):
            g.add_vertex(i)

        # 添加边
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)

        return g


    # 创建一个有环图
    def create_cyclic_graph():
        """创建一个有环图
        图结构:
        0 --> 1 --> 2
        ^           |
        |           v
        +-----------3
        """
        g = Graph()

        # 添加顶点
        for i in range(4):
            g.add_vertex(i)

        # 添加边，形成环
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)

        return g


    # 测试DAG的拓扑排序
    print("测试有向无环图(DAG)的拓扑排序:")
    dag = create_sample_dag()

    # 使用DFS算法
    dfs_result = TopologicalSort.dfs_topological_sort(dag)
    print(f"DFS算法结果: {dfs_result}")

    # 测试有环图
    print("\n测试有环图的拓扑排序:")
    cyclic_graph = create_cyclic_graph()

    # 使用DFS算法
    dfs_cyclic_result = TopologicalSort.dfs_topological_sort(cyclic_graph)
    print(f"DFS算法结果: {dfs_cyclic_result}")

    # 测试更复杂的DAG
    print("\n测试更复杂的有向无环图(DAG)的拓扑排序:")
    complex_dag = Graph()

    # 添加顶点（课程）
    courses = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for course in courses:
        complex_dag.add_vertex(course)

    # 添加边（先修关系）
    complex_dag.add_edge('A', 'B')
    complex_dag.add_edge('A', 'C')
    complex_dag.add_edge('B', 'D')
    complex_dag.add_edge('C', 'D')
    complex_dag.add_edge('D', 'E')
    complex_dag.add_edge('D', 'F')
    complex_dag.add_edge('E', 'G')
    complex_dag.add_edge('F', 'G')

    dfs_complex_result = TopologicalSort.dfs_topological_sort(complex_dag)
    print(f"课程学习顺序(DFS算法): {dfs_complex_result}")