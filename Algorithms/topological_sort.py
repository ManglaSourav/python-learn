from collections import defaultdict


def topological_sort(n, relation):
    adj = defaultdict(list)

    s = set()

    for i, j in relation:
        s.add(j)
        adj[i].append(j)

    indegree = 0
    # find nodes with zero in degree
    for i in range(1, n+1):
        if i not in s:
            indegree = i
            break

    result = [indegree]
    q = [indegree]
    visited = set([indegree])

    while q:

        node = q.pop(-1)
        nodes = adj.get(node)

        for i in range(1, n+1):
            if i not in visited:
                result.append(i)
                visited.add(i)
                q.append(i)

    return result


print(topological_sort(5, [[1, 2], [2, 5], [2, 4], [1, 3], [3, 4], [4, 5]]))
