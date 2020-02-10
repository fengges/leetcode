class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int):
        a=tomatoSlices-2*cheeseSlices
        if a%2==0 and a>=0 and cheeseSlices-a//2>=0:

            return [a//2,cheeseSlices-a//2]
        else:
            return []