class Solution:
    def removeComments(self, source):
        r=[]
        si=False
        for t in source:
            index1=t.find("/*")
            index2 = t.rfind("*/")
            index3 = t.find("//")
            if index2>=0 and si:
                r[-1]+=t[index2+2:]
                si=False
                continue
            elif si:
                continue
            elif index3>=0:
                r.append(t[0:index3])
            elif index1>=0 and index2>=0 and index2>index1 :
                r.append(t[0:index1]+t[index2+2:])
            elif index1>=0:
                r.append(t[0:index1])
                si=True
            else:
                r.append(t)
        r=[i for i in r if len(i)!=0]
        return r

s=Solution()

test=[
{"input": ["a//*b//*c","blank","d/*/e*//f"],"output": ["a","blank","d/f"]},
{"input": ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"],"output":
["struct Node{","    ","    int size;","    int val;","};"]},
{"input": ["a/*comment", "line", "more_comment*/b"],"output": ["ab"]},

{"input": ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"],"output": ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]},

]
for t in test:
    r=s.removeComments(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))