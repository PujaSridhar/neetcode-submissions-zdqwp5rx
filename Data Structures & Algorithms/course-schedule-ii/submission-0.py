class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create the adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # Build the graph and compute indegrees of each node
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Initialize the queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            
            # Decrease the indegree of the neighboring nodes
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If the order contains all the courses, return it
        if len(order) == numCourses:
            return order
        else:
            return []
        