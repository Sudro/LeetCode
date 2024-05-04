# O(nlogn):
class Solution(object):
    def numberGame(self, nums):
        arr = []
        s = sorted(nums)
        for i in range(0, len(nums)-1, 2):
            arr.append(s[i+1])
            arr.append(s[i])
        return arr
