class Solution:
    def generateParenthesis(self, n: int) :
        ans=[]
        def func(tmp,size,left):
            if size==n :
                if left==0:
                    ans.append(tmp)
                else:
                    func(tmp+')',size,left-1)
            else:
                if  size<n:
                    func(tmp+'(',size+1,left+1)

                if left>0:
                    func(tmp+')',size,left-1)

        func("",0,0)
        return ans
    
