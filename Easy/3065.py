# O(n):
class Solution(object):
    def minOperations(self, nums, k):
        return sum(i < k for i in nums)

# O(n):
class Solution(object):
    def minOperations(self, nums, k):
        return len([i for i in nums if i < k])
