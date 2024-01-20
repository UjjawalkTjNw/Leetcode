class Solution(object):
    def smallestEvenMultiple(self, n):
        ans =0
        if(n%2==0):
            ans =n
            return ans 
        elif(n%2 != 0):
            ans = n*2
            return ans 