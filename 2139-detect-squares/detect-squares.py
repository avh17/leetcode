class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)]+=1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(px-x)!=abs(py-y)) or x==px or y==py:
                continue
            res += (self.ptsCount[(x, py)])*(self.ptsCount[(px, y)])

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)