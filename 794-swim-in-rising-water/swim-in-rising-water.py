class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()
        visit.add((0, 0))

        while minHeap:
            t, i, j = heapq.heappop(minHeap)

            if i==N-1 and j==N-1:
                return t
            
            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if (0<=r<N and 0<=c<N and (r,c) not in visit):
                    visit.add((r, c))
                    heapq.heappush(minHeap, [max(t, grid[r][c]), r, c])
