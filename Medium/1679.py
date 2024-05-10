# O(n):
class Solution(object):
    def maxOperations(self, nums, k):
        sl = {}
        for num in nums:
            if num not in sl:
                sl[num] = 1
            else:
                sl[num] += 1
        
        counter = 0
        for elem in sl:
            if k-elem in sl:
                counter += min(sl[elem], sl[k-elem])

        return counter // 2

# O(n):
# With Counter (from collections import Counter)
class Solution(object):
    def maxOperations(self, nums, k):
        c = Counter(nums)
        return sum(min(c[num], c[k-num]) for num in c) // 2

# O(nlogn):
class Solution(object):
    def maxOperations(self, nums, k):
        nums = sorted(nums)
        left, right = 0, len(nums)-1
        counter = 0

        while left < right:
            if nums[left] + nums[right] == k:
                counter += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else: # nums[left] + nums[right] > k
                right -= 1

        return counter

# O(nk):
class Solution(object):
    def maxOperations(self, nums, k):
        sl = {}
        for elem in nums:
            if elem not in sl:
                sl[elem] = 1
            else:
                sl[elem] += 1

        c = 0
        for elem in sl:
            if k - elem in sl and sl[k - elem] > 0 and sl[elem] > 0:
                mn = min(sl[k - elem], sl[elem])
                for i in range(mn):
                    if k - elem == elem and sl[elem] == 1:
                        continue
                    if k - elem in sl and sl[k - elem] > 0 and sl[elem] > 0:
                        sl[k-elem] -= 1
                        sl[elem] -= 1
                        c += 1
    
        return c
