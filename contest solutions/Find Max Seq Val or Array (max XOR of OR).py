# Sometimes Brute force is the answer

#__________________________________________________________________________________________________

# You are given an integer array nums and a positive integer k.

# The value of a sequence seq of size 2 * x is defined as:

# (seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1]).
# Return the maximum value of any subsequence of nums having size 2 * k


class Solution:
    def maxValue(self, nums,k):
        # nums[i] <^7 => max 7 bits
        n=len(nums)

        def generate_combinations(nums):
            t1={(0,0)}
            d={}
            for ind,num in enumerate(nums):
                t2=set()
                for taken,value in t1:
                    if taken<k:
                        t2.add((taken+1,value|num))
                        if taken+1==k and value|num not in d:
                            d[value|num]=ind+1
                t1.update(t2)
            return d
        
        a=generate_combinations(nums)
        b=generate_combinations(nums[::-1])

        res=float('-inf')
        for v1,x1 in a.items():
            for v2,x2 in b.items():
                if x1+x2<=n:
                    res=max(res,v1^v2)
        return res