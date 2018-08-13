class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        sum=0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1]>=duration+timeSeries[i]:
                sum+=duration
            else:
                sum +=timeSeries[i+1]-timeSeries[i]
        if len(timeSeries)>0:
            sum+=duration
        return sum
