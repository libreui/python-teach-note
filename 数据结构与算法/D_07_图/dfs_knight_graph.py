from graph import Graph

def knight_graph(bd_size):
    kt_graph = Graph()
    for row in range(bd_size):
        for col in range(bd_size):
            node_id = post_to_node_id(row, col, bd_size)
            node_positions = gen_legal_moves(row, col, bd_size)
            for pos in node_positions:
                nid = post_to_node_id(pos[0], pos[1], bd_size)
                kt_graph.add_edge(node_id, nid)
    return kt_graph

def post_to_node_id(row, column, board_size):
    return (row * board_size) + column

def gen_legal_moves(x, y, bd_size):
    new_moves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in move_offsets:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coord(new_x, bd_size) and legal_coord(new_y, bd_size):
            new_moves.append((new_x, new_y))

    return new_moves

def legal_coord(x, bd_size):
    if 0 <= x < bd_size:
        return True
    else:
        return False


def knight_tour(n, path, u, limit):
    u.set_color('gray')
    path.append(u)
    if n < limit:
        # nbr_list = list(u.get_connections())
        nbr_list = order_by_avail(u)
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == 'white':
                done = knight_tour(n + 1, path, nbr_list[i], limit)
            i += 1
        if not done:
            path.pop()
            u.set_color('white')
    else:
        done = True
    return done


# -*- coding: utf-8 -*-

def order_by_avail(u):
    """根据Warnsdorff启发式算法，按可用移动数量对顶点进行排序
    
    Warnsdorff启发式规则：优先选择可用移动数量最少的未访问顶点
    这是解决骑士周游问题的一种优化策略，可以显著提高搜索效率
    
    Args:
        u: Vertex对象，当前所在的顶点
        
    Returns:
        list: 排序后的顶点列表，优先选择可用移动最少的顶点
    """
    # 存储(可用移动数, 顶点)元组的列表
    res_list = []
    # 遍历当前顶点u的所有相邻顶点
    for v in u.get_connections():
        # 只考虑未访问(颜色为'white')的顶点
        if v.get_color() == 'white':
            # 计算该顶点v的未访问邻居数量
            c = 0
            for w in v.get_connections():
                if w.get_color() == 'white':
                    c += 1
            # 将(可用移动数, 顶点)添加到结果列表
            res_list.append((c, v))
    # 按照可用移动数量升序排序(可用移动越少的顶点越优先)
    res_list.sort(key=lambda x: x[0])
    # 返回排序后的顶点列表(只保留顶点对象)
    return [x[1] for x in res_list]


if __name__ == '__main__':
    knight_graph = knight_graph(bd_size=8)
    print(f"knight_graph.num_vertices: {knight_graph.num_vertices}, knight_graph.num_edges: {knight_graph.num_edges}")
    # for v in knight_graph:
    #     for w in v.get_connections():
    #         print("({}, {})".format(v.get_id(), w.get_id()))

    a = knight_tour(0, [], knight_graph.get_vertex(7), 63)
    print(a)