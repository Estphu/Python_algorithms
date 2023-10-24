def bestSumDownwardTreePath(parent, values):
    def dfs(node):
        # Initialize the maximum sum for the subtree rooted at this node.
        max_sum = values[node]

        # Initialize the maximum child sum for this node.
        max_child_sum = 0

        for child in tree[node]:
            if child == parent[node]:
                continue  # Skip the parent node.

            child_sum = dfs(child)

            # Update the maximum child sum if the child's sum is larger.
            max_child_sum = max(max_child_sum, child_sum)

        # Calculate the maximum sum for this node.
        max_sum = max(max_sum, max_sum + max_child_sum)

        return max_sum

    n = len(parent)
    tree = [[] for _ in range(n)]

    # Build an adjacency list to represent the tree.
    for i in range(n):
        if i != 0:
            tree[parent[i]].append(i)

    # Start the DFS from the root (node 0).
    return dfs(0)

# Example usage:
parent = [-1, 0, 1, 2, 2]
values = [1, 2, 3, 4, 5]
print(bestSumDownwardTreePath(parent, values))  # Output: 12
