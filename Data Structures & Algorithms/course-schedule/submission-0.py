class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create the adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # States: 0 = UNVISITED, 1 = VISITING, 2 = VISITED
        state = [0] * numCourses
        
        def dfs(course):
            if state[course] == 1:  # Found a cycle
                return False
            if state[course] == 2:  # Already visited
                return True
            
            # Mark the node as visiting
            state[course] = 1
            
            # Visit all the neighbors
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            # Mark the node as visited
            state[course] = 2
            return True
        
        # Check each course
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True        