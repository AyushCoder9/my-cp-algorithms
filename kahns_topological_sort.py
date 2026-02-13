from collections import deque

def findOrder(n, A):
    adjList = [[] for _ in range(n)]
    indegree = [0] * n
    
    for a, b in A:
        adjList[b].append(a)
        indegree[a] += 1

    dq = deque([])
    for i in range(len(indegree)):
        if indegree[i] == 0:
            dq.append(i)

    res = []
    while dq:
        node = dq.popleft()
        res.append(node)
        
        for nei in adjList[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                dq.append(nei)
    
    return res

num_tasks = 4

dependencies = [
    [1, 0],  
    [2, 0],  
    [3, 1],  
    [3, 2]   
]

order = findOrder(num_tasks, dependencies)

print(f"Nodes: {num_tasks}")
print(f"Edges (Dependencies): {dependencies}")
print(f"Topological Sort Order: {order}")