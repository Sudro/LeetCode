# O(nlogn):
class Solution(object):
    def countPairs(self, nums, target):
        nums = sorted(nums)

        left = 0
        right = len(nums) - 1
        c = 0

        while left < right:
            if nums[left] + nums[right] < target:
                c += right - left
                left += 1
            else:
                right -= 1

        return c


# O(n ^ 2):
class Solution(object):
    def countPairs(self, nums, target):
        nums = sorted(nums)
        count_pair = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count_pair += 1
                else:
                    break
        return count_pair