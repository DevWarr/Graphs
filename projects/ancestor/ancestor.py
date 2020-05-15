
def earliest_ancestor(ancestors, starting_node):
    # CRUDE version:
    # Loop through nodes,
    #     finding all nodes with the start as a child.
    #     Store the parent node.
    # Loop through nodes again,
    #     using the parent nodes from above as the 'starting node'.
    #     Store those parent nodes.
    # Keep looping until the longest path from the child is found.
    #
    # ↑ This version requires looking through the graph several times.
    # We could make it faster by creating a lookup table first,
    #     and then using it for our loops.
    # Still O(n) because we need to make the lookup table from our nodes,
    #     but still faster.

    lookup_table = {}

    for node in ancestors:
        if node[1] not in lookup_table:
            lookup_table[node[1]] = [node[0]]
        else:
            lookup_table[node[1]].append(node[0])

    # stack, vertex, farthest, parent
    f = (starting_node, 0)
    s = [(starting_node, 0)]
    while len(s):
        v = s.pop()
        if v[0] in lookup_table:
            [s.append((p, v[1]+1)) for p in lookup_table[v[0]]]
        else:
            if v[1] > len(lookup_table) // 2:
                # If our distance from start to end is longer than 
                # half of the lookup table, we know there's no other
                # path that's longer.
                return v[0]
            if v[1] > f[1] or v[1] == f[1] and v[0] < f[0]:
                f = v

    if f[0] == starting_node:
        return -1
    else:
        return f[0]