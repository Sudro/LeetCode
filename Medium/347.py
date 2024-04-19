# O(n+klogk)
class Solution(object):
    def topKFrequent(self, nums, k):
        sl = {}
        for i in range(len(nums)):
            if nums[i] not in sl:
                sl[nums[i]] = 1
            else:
                sl[nums[i]] += 1
        nums = sorted(sl.items(), key=lambda x:x[1])

        d = []
        for i in range(k):
            d.append(nums[len(nums)-i-1][0])
        return d