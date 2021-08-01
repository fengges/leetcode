class Solution:
    def angleClock(self, hour, minutes):
        # if hour==12:
        #     hour=0
        minutes_ans=360/60*minutes
        hour_ans=360/12*(hour)+minutes_ans/12
        ang=abs(hour_ans-minutes_ans)
        return min(ang,360-ang)
s=Solution()
null=None
test=[
    {"input":[3,30],"output":75},
]
for t in test:
    r=s.angleClock(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))