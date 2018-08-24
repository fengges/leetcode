class Solution(object):
    def lemonadeChange(self, bills):
        dic={5:0,10:0,20:0}
        for b in bills:
            if b==5:
                dic[5]+=1
            elif b==10:
                dic[10]+=1
                if dic[5]>0:
                    dic[5]-=1
                else:
                    return False
            else:
                dic[20]+=1
                if dic[10]>0 and dic[5]>0:
                    dic[10]-=1
                    dic[5]-=1
                elif dic[5]>2:
                    dic[5]-=3
                else:
                    return False
        return True