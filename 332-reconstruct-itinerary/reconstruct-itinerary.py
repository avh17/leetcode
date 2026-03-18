class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for source, dest in tickets:
            graph[source].append(dest)

        # smallest last, but smallest will be first when we pop
        for source in graph:
            graph[source].sort(reverse=True)

        res = []
        def dfs(node):
            # while the source has destinations
            while graph[node]:
                dfs(graph[node].pop()) # recursively pop and append the smallest destinations
            res.append(node)

        dfs("JFK")
        return res[::-1]