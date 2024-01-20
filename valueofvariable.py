#Find value of variable after performing operations
class Solution(object):
    def finalValueAfterOperations(self, operations):
        val = 0
        res = 0 
        for i in operations:
            if i=="X++" or i=="++X":
                val = 1
                res+=val
            elif i=="X--" or i=="--X":
                val =-1
                res+=val
        return res