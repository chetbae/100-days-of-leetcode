# Dijkstra's algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create a data structure better suited for finding neighbours
        graph = { u:[] for u in range(n) }
        
        # create a hashmap better suited to retrieving edge weights
        weights = {}

        # populate edges and weights, shift nodes of 1 to n into 0 to n-1
        for u, v, w in times:
            graph[u-1].append(v-1)
            weights[(u-1, v-1)] = w

        # run dijkstra's algorithm, tracking shortest time to each vertex in network
        distance = [float('inf')] * n

        # searching from vertex k, initial distance of 0
        distance[k-1] = 0

        # track visited and relaxed vertexs
        visited = [False] * n

        # runs max n times to visit each vertex
        for i in range(n):
            # first, find vertex with lowest distance
            min_distance = float('inf')
            vertex = None

            for u in range(n):
                if not visited[u] and distance[u] < min_distance:
                    min_distance, vertex = distance[u], u
            
            # if no vertex found, some vertices are unreachable i.e. distance of inf
            if vertex == None:
                return -1

            # mark vertex as visited
            visited[vertex] = True

            # then find min vertex neighbours and update distances if necessary
            for nb in graph[vertex]:

                # skip if neighbour is already visited
                if visited[nb]:
                    continue

                # check if current distance + edge weight to neighbour is shorter, relax edges
                new_distance = min_distance + weights[(vertex, nb)]
                if new_distance < distance[nb]:
                    distance[nb] = new_distance

        return max(distance)



