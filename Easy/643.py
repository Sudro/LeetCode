# O(n)
class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums) == 1:
            return nums[0] / float(k)

        left = 0
        right = k
        s = sum(nums[:k])

        mx = s

        while right < len(nums):
            s -= nums[left]
            s += nums[right]
            mx = max(mx, s)
            left += 1
            right += 1

        return mx / float(k)

# O(n)
class Solution(object):
    def findMaxAverage(self, nums, k):
        s = sum(nums[:k])
        mx = s

        for left in range(len(nums)-k):
            s -= nums[left]
            s += nums[left+k]
            mx = max(mx, s)

        return mx / float(k)
