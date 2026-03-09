class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED]*numCourses

        def dfs(i):
            if states[i] == VISITED:
                return True
            elif states[i] == VISITING:
                return False

            states[i] = VISITING

            for nei in graph[i]:
                if not dfs(nei):
                    return False

            states[i] = VISITED
            res.append(i)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
                
        return res