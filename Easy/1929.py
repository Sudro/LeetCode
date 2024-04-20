# O(n):
class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums

# O(n):
class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        nums = nums + [0]*n
        for i in range(n):
            nums[i+n] = nums[i]
        return nums