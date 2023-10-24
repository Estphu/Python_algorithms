from collections import defaultdict, deque

def countMinimumUnreachableWarehouses(warehouse_nodes, warehouse_from, warehouse_to):
    # Build a directed graph using an adjacency list.
    graph = defaultdict(list)
    for i in range(len(warehouse_from)):
        graph[warehouse_from[i]].append(warehouse_to[i])

    # Initialize an array to keep track of incoming edges for each warehouse.
    incoming_edges = [0] * warehouse_nodes

    for i in range(len(warehouse_to)):
        incoming_edges[warehouse_to[i] - 1] += 1

    # Perform topological sorting to identify unreachable warehouses.
    queue = deque()
    for i in range(warehouse_nodes):
        if incoming_edges[i] == 0:
            queue.append(i + 1)

    unreachable_count = 0
    while queue:
        warehouse = queue.popleft()
        for neighbor in graph[warehouse]:
            incoming_edges[neighbor - 1] -= 1
            if incoming_edges[neighbor - 1] == 0:
                queue.append(neighbor)
        unreachable_count += 1

    return warehouse_nodes - unreachable_count

# Example usage:
warehouse_nodes = 6
warehouse_from = [1, 2, 4, 5, 4]
warehouse_to = [2, 3, 5, 6, 6]
print(countMinimumUnreachableWarehouses(warehouse_nodes, warehouse_from, warehouse_to))  # Output: 1
