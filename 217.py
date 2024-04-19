#O(n):
class Solution(object):
    def containsDuplicate(self, nums):
        hashmap = set()
        for elem in nums:
            if elem in hashmap:
                return True
            hashmap.add(elem)
        return False

#O(nlogn):
class Solution(object):
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False