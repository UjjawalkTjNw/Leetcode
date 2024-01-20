class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in jewels:
           # print(i)
            for j in stones:
                if i == j:
                    count+=1
        return count