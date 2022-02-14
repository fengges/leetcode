class Solution:
    def rand10(self):
        a=rand7()
        b=rand7()
        while a==7:
            a=rand7()
        while b>5:
            b=rand7()

        return (0 if a&1 else 5)+b