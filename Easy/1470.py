# O(n):
class Solution(object):
    def shuffle(self, nums, n):
        d = []
        ln = len(nums)//2
        for i in range(ln):
            d.append(nums[i])
            d.append(nums[ln+i])

        return d