# You are given two strings word1 and word2.

# A string x is called almost equal to y if you can change at most one character in x to make it identical to y.

# A sequence of indices seq is called valid if:

# The indices are sorted in ascending order.
# Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.
# Return an array of size word2.length representing the 
# lexicographically smallest
#  valid sequence of indices. If no such sequence of indices exists, return an empty array.

# Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

# Input: word1 = "vbcca", word2 = "abc"

# Output: [0,1,2]

class Solution:
    def validSequence(self, word1, word2):
        n1,n2=len(word1),len(word2)
        good=[-1]*(n2+1)
        good[n2]=n1

        r=n1-1
        for i in range(n2-1,-1,-1):
            while r>=0 and word1[r]!=word2[i]:
                r-=1
            good[i]=r
            if r<0:
                break
            r-=1
        res=[]
        used=False
        r=0
        for i in range(n1):
            if r>=n2:
                break
            if word1[i]==word2[r]:
                res.append(i)
                r+=1
                continue
            if not used and good[r+1]>=i+1:
                res.append(i)
                used=True
                r+=1
                continue
        if len(res)!=n2:
            return []
        return res