class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        rows, cols = len(grid), len(grid[0])

        q = deque()
        num_fresh = 0
        num_minutes = -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == FRESH:
                    num_fresh += 1
                elif grid[i][j] == ROTTEN:
                    q.append((i, j))

        if num_fresh == 0:
            return 0

        while q:
            qLen = len(q)
            num_minutes += 1
            for _ in range(qLen):
                i, j = q.popleft()
                for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if (0<=r<rows and 0<=c<cols and grid[r][c] == FRESH):
                        grid[r][c] = ROTTEN
                        num_fresh -= 1
                        q.append((r,c))

        if num_fresh == 0:
            return num_minutes
        else:
            return -1