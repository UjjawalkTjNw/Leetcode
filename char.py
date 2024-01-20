#find word containing characters
class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i,j in enumerate(words):
            for k in j:
                if k == x:
                    res.append(i)
                    break
        return res