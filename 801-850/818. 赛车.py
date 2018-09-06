class Solution:
    def racecar(self, target):
        position=0
        speed=1
        r=[0]
        for t in target:
            position += speed
            r.append(position)
            if t=="A":
                speed *= 2
            elif speed>0:
                speed=1
            else:
                speed=-1
        return r

