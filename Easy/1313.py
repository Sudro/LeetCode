# O(n):
class Solution(object):
    def decompressRLElist(self, nums):
        d = []
        for i in range(0, len(nums)-1, 2):
            d += nums[i] * [nums[i+1]]
        return d

# O(nk):
class Solution(object):
    def decompressRLElist(self, nums):
        d = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                d.append(nums[i+1])
        return d


