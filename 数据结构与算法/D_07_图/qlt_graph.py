from graph import Graph
from dfs_graph import DFSGraph
from show import GraphVisualizer


# 添加转置函数
def transpose(graph):
    """获取图的转置图（将所有边的方向反转）
    
    算法思路：
    1. 创建一个新的图作为转置图
    2. 复制原图中的所有顶点到转置图
    3. 遍历原图中的所有边，将每条边的方向反转后添加到转置图中
    
    Args:
        graph: 要转置的图对象
        
    Returns:
        DFSGraph: 转置后的图对象
    """
    # 创建一个新的DFSGraph作为转置图
    transposed_graph = DFSGraph()

    # 首先添加所有顶点到转置图
    for vertex in graph:
        transposed_graph.add_vertex(vertex.get_id())
        transposed_graph.vert_list[vertex.get_id()].set_finish(vertex.get_finish())

    # 遍历原图中的所有边，将边的方向反转后添加到转置图
    for vertex in graph:
        for neighbor in vertex.get_connections():
            # 反转边的方向：原图中u->v变为转置图中的v->u
            transposed_graph.add_edge(neighbor.get_id(), vertex.get_id(), vertex.get_weight(neighbor))

    return transposed_graph


# 原有的图创建和测试代码

# 创建图
print("创建原始图...")
graph = DFSGraph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('B', 'E')
graph.add_edge('C', 'C')  # 自环边
graph.add_edge('C', 'F')
graph.add_edge('D', 'B')
graph.add_edge('D', 'G')
graph.add_edge('E', 'A')
graph.add_edge('E', 'D')
graph.add_edge('F', 'H')
graph.add_edge('G', 'E')
graph.add_edge('H', 'I')
graph.add_edge('I', 'F')

# 打印图的所有顶点和边的数量
print(f"顶点数量: {graph.num_vertices}, 边数量: {graph.num_edges}")

# 执行深度优先搜索
print("\n执行深度优先搜索...")
graph.dfs()

# 显示DFS搜索结果
print("\nDFS搜索结果 (顶点ID: 发现时间/完成时间, 前驱节点):")
for v in graph:
    pred_id = v.get_predecessor().get_id() if v.get_predecessor() != -1 and v.get_predecessor() is not None else -1
    print(f"顶点 {v.get_id()}: {v.get_discovery()}/{v.get_finish()}, 前驱: {pred_id}")

# 使用转置函数获取转置图
print("\n创建转置图...")
graph_t = transpose(graph)
graph_t.dfs_t()

for v in graph_t:
    pred_id = v.get_predecessor().get_id() if v.get_predecessor() != -1 and v.get_predecessor() is not None else -1
    print(f"顶点 {v.get_id()}: {v.get_discovery()}/{v.get_finish()}, 前驱: {pred_id}")
