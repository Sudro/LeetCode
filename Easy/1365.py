# O(nlogn):
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        s = sorted(nums)
        sl = {}
        for i in range(len(nums)):
            if s[i] not in sl:
                sl[s[i]] = i

        mass = []
        for elem in nums:
            mass.append(sl[elem])
        return mass


# O(n ^ 2):
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = []
        for i in range(len(nums)):
            k = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    k += 1
            arr.append(k)
        return arr