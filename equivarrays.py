#check if two string arrays are equivalent
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        
        str1= ''
        str2=''
        for i in word1:
            str1 = str1+i
        for j in word2:
            str2 = str2+j
        #now we have to compare element by element for each string
        if(len(str1)!=len(str2)):
            return False
        for i , j in zip(str1,str2):
            if i!=j:
                return False
        return True