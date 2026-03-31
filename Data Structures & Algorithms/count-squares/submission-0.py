from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))  # points[y][x] = count

    def add(self, point: list[int]) -> None:
        x, y = point
        self.points[y][x] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        res = 0
        if y not in self.points:
            return 0

        for ny in self.points:  # iterate all y's to find square height
            if ny == y:
                continue
            d = ny - y  # side length

            # Two directions: right and left
            for dx in [d, -d]:
                x1 = x
                x2 = x + dx

                cnt1 = self.points[y][x2]        # base point on same row
                cnt2 = self.points[ny][x]        # vertical edge
                cnt3 = self.points[ny][x2]       # diagonal corner

                if cnt1 and cnt2 and cnt3:
                    res += cnt1 * cnt2 * cnt3

        return res
