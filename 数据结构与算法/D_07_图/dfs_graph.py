from graph import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for a_vertex in self:
            a_vertex.set_color('white')
            a_vertex.set_predecessor(-1)
        for a_vertex in self:
            if a_vertex.get_color() == 'white':
                self.dfs_visit(a_vertex)  # 修复了这里，之前没有调用dfs_visit

    def dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discovery(self.time)
        # 修复了遍历方式，应该遍历当前顶点的邻接顶点，而不是整个图
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == 'white':
                next_vertex.set_predecessor(start_vertex)
                self.dfs_visit(next_vertex)
        start_vertex.set_color('black')
        self.time += 1
        start_vertex.set_finish(self.time)


if __name__ == '__main__':
    # 生成类的测试代码
    # 创建DFSGraph实例
    dfs_graph = DFSGraph()
    
    # 添加顶点
    print("添加顶点...")
    for i in range(6):
        dfs_graph.add_vertex(i)
    
    # 添加边，构建一个有向图
    print("添加边...")
    dfs_graph.add_edge(0, 1)
    dfs_graph.add_edge(0, 2)
    dfs_graph.add_edge(1, 3)
    dfs_graph.add_edge(2, 3)
    dfs_graph.add_edge(2, 4)
    dfs_graph.add_edge(3, 5)
    dfs_graph.add_edge(4, 5)
    
    # 显示图的初始结构
    print("图的初始结构:")
    for v in dfs_graph:
        for w in v.get_connections():
            print(f"边: {v.get_id()} -> {w.get_id()}")
    
    # 执行深度优先搜索
    print("\n执行深度优先搜索...")
    dfs_graph.dfs()
    
    # 显示DFS搜索结果
    print("\nDFS搜索结果 (顶点ID: 发现时间/完成时间, 前驱节点):")
    for v in dfs_graph:
        pred_id = v.get_predecessor().get_id() if v.get_predecessor() != -1 and v.get_predecessor() is not None else -1
        print(f"顶点 {v.get_id()}: {v.get_discovery()}/{v.get_finish()}, 前驱: {pred_id}")
    
    # 验证顶点颜色（所有顶点应为黑色，表示已访问）
    print("\n验证顶点颜色:")
    all_black = all(v.get_color() == 'black' for v in dfs_graph)
    print(f"所有顶点已访问: {all_black}")
    
    # 验证发现时间和完成时间的正确性
    print("\n验证时间戳属性:")
    for v in dfs_graph:
        if v.get_discovery() >= v.get_finish():
            print(f"错误: 顶点 {v.get_id()} 的发现时间({v.get_discovery()})大于等于完成时间({v.get_finish()})")
    
    print("\nDFS图测试完成!")