# O(n):
class Solution(object):
    def leftRightDifference(self, nums):
        sumLeft = 0
        sumRight = sum(nums)
        for i, n in enumerate(nums):
            sumRight -= n
            nums[i] = abs(sumLeft - sumRight)
            sumLeft += n
        return nums

# O(n^2):
class Solution(object):
    def leftRightDifference(self, nums):
        mas = []
        for i in range(len(nums)):
            mas.append(abs(sum(nums[:i]) - abs(sum(nums[i+1:]))))

        return mas

# O(n^2):
class Solution(object):
    def leftRightDifference(self, nums):
        mas = []
        total_s = sum(nums)
        for i in range(len(nums)):
            s_left = 0
            for j in range(0, i):
                s_left += nums[j]

            s_right = total_s - s_left - nums[i]
            mas.append(abs(s_left - s_right))

        return mas