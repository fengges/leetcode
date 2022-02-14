class Solution:
    def equationsPossible(self, equations) -> bool:
        ans=[]
        def fund(ch):
            for i,a in enumerate(ans):
                if ch in a:
                    return i
            return -1

        for e in equations:
            a,b=e[0],e[-1]
            eq=e[1:3]
            index1,index2=fund(a),fund(b)
            if eq=='==':
                if index1==-1 and index2==-1:
                    ans.append({a,b})
                elif index1==-1 and index2!=-1:
                    ans[index2].add(a)
                elif index1!=-1 and index2==-1:
                    ans[index1].add(b)
                elif index1!=index2:
                    ans[index1]=ans[index1]|ans[index2]
                    ans.pop(index2)
        for e in equations:
            a,b=e[0],e[-1]
            eq=e[1:3]
            index1,index2=fund(a),fund(b)
            if eq=='!=':
                if a==b:
                    return False
                elif index1!=-1 and index2==index1:
                    return False
                elif index1==-1 :
                    ans.append({a})
                elif index2==-1:
                    ans.append({b})

        return True

s=Solution()

test=[

    {"input": [  ["c==c","f!=a","f==b","b==c"]],"output":True},
    {"input": [ ["a==b","b==c","a==c"]],"output":True},
    {"input": [ ["a==b","b!=c","c==a"]],"output":False},
    {"input": [ ["b==a","a==b"]],"output":True},
    {"input": [["a==b","b!=a"]],"output":False},

]
for t in test:
    r=s.equationsPossible(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
