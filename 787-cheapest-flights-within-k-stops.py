class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float('inf')] * n
        distance[src] = 0

        for i in range(k+1):
            new_distance = distance.copy()

            for u, v, w in flights:
                if distance[u] != float('inf') and distance[u] + w < new_distance[v]:
                    new_distance[v] = distance[u] + w
            
            distance = new_distance
        
        return -1 if distance[dst] == float('inf') else distance[dst]
    
