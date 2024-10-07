from bisect import bisect_left
#time O(nlogn)
#space O(n)

class Solution:
    def lengthOfLIS(self, nums):
        LIS=[]
        def lis(i):
            pos=bisect_left(LIS,nums[i])
            if pos<len(LIS):
                LIS[pos]=nums[i]
            else:
                LIS.append(nums[i])
        for i in range(len(nums)):
            lis(i)
        return len(LIS)