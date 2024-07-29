import heapq 

class Dijikstras: 
    def __init__(self) -> None:
        pass
 
    def Dijkstras(graph, source): 
        n = len(graph)
        d = [float('inf')] * n
        d[source] = 0 
        s = set()
        p = [-1] * n  
        minHeap = [(0, source)] 
        while minHeap: 
            dist, u = heapq.heappop(minHeap) 
            s.add(u)
            for v, w in graph[u]: 
                if v not in s and d[u] + w < d[v]: 
                    d[v] = d[u] + w
                    heapq.heappush((d[v], v))
                    p[v] = u
        return d, p
    
    def main(): 
        pass 

    if __name__ == "__main__": 
        main()
