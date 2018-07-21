class Solution:
    def judgeCircle(self, moves):
        w,h=0,0
        for s in moves:
            if s=="R":
                w+=1
            elif s=="L":
                w-=1
            elif s=="U":
                h+=1
            else:
                h-=1
        if w==0 and h==0:
            return True
        return False