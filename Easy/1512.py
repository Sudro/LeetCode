# O(n^2):
class Solution(object):
    def numIdenticalPairs(self, nums):
        c = 0
        #ln = len(nums)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if i < j and nums[i] == nums[j]:
                    c += 1
        return c