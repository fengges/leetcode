class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        size=len(bits)
        if size==2 or size==0:
            return bits==[0,0]
        if size==1 :
            return  bits==[0]

        if bits[0]==0:
            return self.isOneBitCharacter([ bits[i] for i in range(1,size)])
        else:
            return self.isOneBitCharacter([ bits[i] for i in range(2,size)])
