import heapq

def prim(n, adj):
    visited = [False]*n
    min_heap = [(0, 0)]
    
    mst_weight = 0
    
    while min_heap:
        w, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        mst_weight += w
        
        for v, wt in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (wt, v))
    
    return mst_weight

n = 5
adj = [[] for _ in range(n)]

edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]

for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

print(prim(n, adj))
