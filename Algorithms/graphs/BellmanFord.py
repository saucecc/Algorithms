class BellmanFord:
    
    """
    
    """
    
    def __init__(self) -> None: 
        self.distances = None 
        self.parents = None 
        self.source = None 

    def recreatePathTo(self, g): 
        res = [] 
        fr = g 
        while fr != -1 and fr != self.source:
            res.append(fr) 
            fr = self.parents[fr]
        if fr == self.source: 
            res.append(self.source)
        res.reverse() 
        return res 

     
    def getShortestPaths(self, s, graph): 
        n = len(graph)
        d = [float('inf')] * n
        p = [-1] * n 
        edges = []

        # create edge list 
        for u in range(n): 
            for v, w in graph[u]: 
                edges.append((u, v, w))

        d[s] = 0 
        for _ in range(n - 1): 
            updated = False
            for u, v, w in edges: # make all possible edge relaxations 
                if d[v] > d[u] + w: 
                    updated = True 
                    d[v] = d[u] + w
                    p[v] = u
            if not updated: # no edge relaxations left, stop 
                break 

        # check for negative weight cycles 
        for u, v, w in edges:
            if d[u] != float('inf') and d[v] > d[u] + w:
                print("Graph contains a negative-weight cycle")
                return None

        self.distances = d 
        self.parents = p 
        self.source = s
        return d 

                
