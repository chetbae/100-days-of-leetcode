class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # make a hashmap to track indegrees in our graph
        indegrees = {node:0 for node in range(numCourses)}

        # make a graph better suited to searching for neighbours
        graph = {node:[] for node in range(numCourses)}

        # populate graph and increment indegrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
        
        # run topological sort
        order = []

        # exactly n nodes should be added to the order in n iterations
        for i in range(numCourses):

            # find node with indegrees of 0
            for node in range(numCourses):

                if indegrees[node] == 0:
                    
                    # once found, add to order
                    order.append(node)

                    # decrement neighbours
                    for nb in graph[node]:
                        indegrees[nb] -= 1
                    
                    # remove node from consideration
                    indegrees[node] = -1

                    break
            
            # if no nodes with 0 indegrees was found, cycle
            if len(order) != i+1:
                return []
                    
        return order
