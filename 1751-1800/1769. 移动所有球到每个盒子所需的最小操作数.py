class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes2=[int(s) for s in boxes]
        ans1=[0 for i in boxes]
        ans2=[0 for i in boxes]

        size=boxes2[0]
        for i in range(1,len(boxes2)):
            ans1[i]=ans1[i-1]+size
            size+=boxes2[i]

        boxes2.reverse()

        size=boxes2[0]
        for i in range(1,len(boxes2)):
            ans2[i]=ans2[i-1]+size
            size+=boxes2[i]

        ans2.reverse()
        for i in range(len(boxes2)):
            ans1[i]+=ans2[i]
        return ans1