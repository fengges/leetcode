class Solution:
    def twoSum(self, numbers, target):
        result=[]
        a=None
        for i in range(len(numbers)-1):
            if a==numbers[i]:
                continue
            a=numbers[i]
            b=None
            for j in range(i+1,len(numbers)):
                if b == numbers[j]:
                    continue
                b = numbers[j]
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                elif   numbers[i]+numbers[j]>target:
                    break

        return  result


s=Solution()
test=[
{"input": [[5,25,75],100], "output":[2,3]},
]

for t in test:
    r=s.twoSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.twoSum(t['input'][0], t['input'][1])