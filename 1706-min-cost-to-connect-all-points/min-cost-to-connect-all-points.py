class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjList = defaultdict(list)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])

        visit = set()
        minHeap = [[0,0]]
        total_cost = 0
        while len(visit)<N:
            cur_cost, cur_point = heapq.heappop(minHeap)
            if cur_point in visit:
                continue
            visit.add(cur_point)
            total_cost += cur_cost
            for neiCost, nei in adjList[cur_point]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])

        return total_cost