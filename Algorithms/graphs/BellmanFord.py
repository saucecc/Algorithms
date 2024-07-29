class BellmanFord:
    
    """ 
    Bellman Ford Algorithm: Single source shortest path (SSSP) algorithm 
        - can handle negative edge weights and cycles

    Time Complexity: O(m*n)

    Idea: Relax each edge so many times that we know we must have the right answer by the end 
        - the reason we relax every edge (n - 1) times is because in some next iteration we may 
        find a shorter path from s -> u, which could result in a shorter path from s -> v 

        - assuming we make some distance optimization for every vertex on each iteration, we see we would 
        have relaxed every single vertex (excluding s as this is trivial) to its shortest distance 
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

     
    def bellmanFord(self, s, graph): 
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

        # check for negative weight cycles, update accordingly 
        for i in range(n - 1): 
            updated = False
            for u, v, w in edges: 
                if d[u] + w < d[v]: 
                    updated = True 
                    d[v] = float('-inf')
                if not updated: 
                    break 

        self.distances = d 
        self.parents = p 
        self.source = s
        return d 

                
