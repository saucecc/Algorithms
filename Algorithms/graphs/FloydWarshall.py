
class FloydWarshall:
    
    """
    Floyd-Warshall: all pairs shortest path (APSP) algorithm 
        - Main advantage over Dijkstra's on every vertex is the ability to handle negative edge weights 

    - Time Complexity: O(n^3) 
    - Space Complexity: O(n^2)

    Idea: 
        dp[i][j] = shortest path from i to j routing through {0, 1, ..., k-1, k}

    Proof Sketch: 


    """
    
    def __init__(self): 
        self.graph = None 
        self.next = None 
        self.solution = None 


    def handleNegativeCycles(self, dp, n): 
        """ 
         negative cycles: if we can still improve any "shortest path",
         set optimal dist to -inf, as any edge this is true for must be part of a negative cycle
        """
        for k in range(n): 
            for i in range(n): 
                for j in range(n): 
                    if dp[i][k] + dp[k][j] < dp[i][j]: 
                        dp[i][j] = float('-inf')
                        next[i][j] = -1 

        pass

    def reconstructSP(self, s, g):
        path = [] 
        if self.solution[s][g] == float('inf'): 
            return path
        
        at = s 
        while at != g: 
            if at == -1: 
                return None 
            path.append(at) 
        if self.next[at][g] == -1: 
            return None 
        path.append(g)
        return path 
    
    def setup(self, graph, dp, next, n): 
        """
        deep copy input matrix into dp 
        setup next matrix: if edge (i, j) exists, next node to go to from i is j 
        """
        for i in range(n): 
            for j in range(n): 
                dp[i][j] = graph[i][j]
                if graph[i][j] != float('inf'): 
                    next[i][j] = j

    
    def floydWarshall(self, graph, negCycles=False): 
        """ main function """
        n = len(graph)
        dp = [[float('inf')] * n for _ in range(n)]  # init dp matrix 
        next = [[-1] * n for _ in range(n)]      # matrix used to reconstruct actual shortest paths 

        self.setup(graph, dp, next, n)

        for k in range(n):  # building up best solutions for paths going through k = 0, ..., k - 1
            for i in range(n):  # examine all (i, j) pairs 
                for j in range(n): 
                    if dp[i][j] > dp[i][k] + dp[k][j]: 
                        dp[i][j] = dp[i][k] + dp[k][j]
                        next[i][j] = next[i][k]

        if negCycles: 
            self.handleNegativeCycles(dp, n)

        self.graph = graph 
        self.next = next 
        self.solution = dp 

        return dp 
    

    def main(): 
        """main function for testing"""
        g = [
            []
        ]

    if __name__ == "__main__": 
        main()
