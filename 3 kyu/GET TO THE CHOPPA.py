from collections import deque


# using tuples
def find_shortest_path_tuples(grid, start_node, end_node):
    queue = deque([start_node.position])
    node_dict = {}
    dist = {}
    parent = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            node = grid[i][j].position
            dist[node] = -1
            node_dict[node] = []
            if i > 0 and grid[i-1][j].passable:
                node_dict[node].append(grid[i-1][j].position)
            if i < len(grid)-1 and grid[i+1][j].passable:
                node_dict[node].append(grid[i+1][j].position)
            if j > 0 and grid[i][j-1].passable:
                node_dict[node].append(grid[i][j-1].position)
            if j < len(grid[i])-1 and grid[i][j+1].passable:
                node_dict[node].append(grid[i][j+1].position)

    dist[start_node.position] = 0
    parent[start_node.position] = -1

    while queue:
        for v in node_dict[queue[0]]:
            if dist[v] == -1:
                dist[v] = dist[queue[0]] + 1
                parent[v] = queue[0]
                queue.append(v)
        queue.popleft()

    node = end_node.position
    result = [end_node.position]
    while parent[node] != -1:
        result = [parent[node]] + result
        node = parent[node]
    return result


# using problem setup
def find_shortest_path(grid, start_node, end_node):
    if not grid: return []
    queue = deque([start_node])
    node_dict = {}
    dist = {}
    parent = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            node = grid[i][j]
            dist[node] = -1
            node_dict[node] = []
            if i > 0 and grid[i-1][j].passable:
                node_dict[node].append(grid[i-1][j])
            if i < len(grid)-1 and grid[i+1][j].passable:
                node_dict[node].append(grid[i+1][j])
            if j > 0 and grid[i][j-1].passable:
                node_dict[node].append(grid[i][j-1])
            if j < len(grid[i])-1 and grid[i][j+1].passable:
                node_dict[node].append(grid[i][j+1])

    dist[start_node] = 0
    parent[start_node] = -1
    print(queue)
    while queue:
        for v in node_dict[queue[0]]:
            if dist[v] == -1:
                dist[v] = dist[queue[0]] + 1
                parent[v] = queue[0]
                queue.append(v)
        queue.popleft()

    node = end_node
    result = [end_node]
    while parent[node] != -1:
        result = [parent[node]] + result
        node = parent[node]
    return result

