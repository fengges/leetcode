import random
import bisect
class Solution:

    def __init__(self, rects):
        self.rect = rects
        self.w = [0]
        for a, b, x, y in rects:
            self.w.append(self.w[-1] + (x - a + 1) * (y - b + 1))
        self.w = self.w[1:]
        # print(self.w)

    def pick(self) :
        r = random.randint(0, self.w[-1])
        (a, b, x, y) = self.rect[bisect.bisect_left(self.w, r)]
        nx = random.randint(a, x)
        ny = random.randint(b, y)
        return [nx, ny]