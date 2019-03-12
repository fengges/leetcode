class Solution:
    def validateStackSequences(self, pushed, popped):
        if len(pushed)==0:
            return True
        if pushed[0] in popped:
            index =  popped.index(pushed[0])
            left = index
            return self.validateStackSequences(pushed[1:1 + left], popped[0:index]) and self.validateStackSequences(pushed[1 + left:],popped[index + 1:])

        else:
            return False
