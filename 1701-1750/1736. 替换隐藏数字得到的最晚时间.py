class Solution:
    def maximumTime(self, time):
        tmp=time.split(':')
        hh,mm=tmp[0],tmp[1]
        arr=[t for t in time]

        if hh[0]=='?' :
            if hh[1]=='?' or hh[1]<'4':
                arr[0]='2'
            else:
                arr[0]='1'
        if hh[1]=='?':
            arr[1]='9' if arr[0]!='2' else '3'
        if mm[0]=='?':
            arr[3]='5'
        if mm[1]=='?':
            arr[4]='9'
        return ''.join(arr)



s=Solution()
null=None
test=[
    {"input": "2?:?0","output":'23:50'},
    {"input":"0?:3?","output":'09:39'},
    {"input":"1?:22","output":'19:22'},
    {"input":"?4:03","output":'14:03'},
]
for t in test:
    r=s.maximumTime(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

