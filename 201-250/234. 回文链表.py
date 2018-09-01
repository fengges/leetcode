class Solution:
    def isPalindrome(self, head):
        r=[]
        while head:
            r.append(head.val)
            head=head.next
        for i in range(int(len(r)/2)):
            if r[i]!=r[len(r)-1-i]:
                return False
        return True