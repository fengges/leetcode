class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):

        self.chars=[c for c in characters]
        self.chars.sort()
        self.num=0
        self.size=combinationLength
        self.len=len(self.chars)
        self.maxSize=len(self.chars)**self.size-1

    def next(self) -> str:
        ans=''
        tmp=self.num
        for i in range(self.size):
            t=tmp%self.len
            tmp//=self.len
            ans=self.chars[t]+ans
        self.num+=1

    def hasNext(self) -> bool:
        return self.num<self.maxSize-1

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()