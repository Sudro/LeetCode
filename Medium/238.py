# O(n):
# Without using the division operation!!!
class Solution(object):
    def productExceptSelf(self, nums):
        ln = len(nums)
        prefix = [1] * ln
        suffix = [1] * ln

        for i in range(1, ln):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(ln-2, 0-1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        return [prefix[i] * suffix[i] for i in range(ln)]

# O(n):
# Using the division operation!!!
class Solution(object):
    def productExceptSelf(self, nums):
        pr = 1
        c0 = 0 # counter zeros

        for elem in nums:
            if elem != 0:
                pr *= elem
            else:
                c0 += 1

        if c0 > 1:
            return [0] * len(nums) # all zeros
        
        total = []
        
        for elem in nums:
            if c0 == 1: # one 0
                if elem != 0:
                    total.append(0)
                else: # = 0
                    total.append(pr)
            else: # no zeros
                total.append(pr / elem)

        return total



# O(n):
# Using the division operation!!!
class Solution(object):
    def productExceptSelf(self, nums):
        pr = 1
        pr0 = 1
        if nums.count(0) > 1:
            return [0] * len(nums)
            
        for elem in nums:
            pr *= elem

        for elem in nums:
            if elem != 0:
                pr0 *= elem
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] = pr / nums[i]
            else:
                nums[i] = pr0

        return nums
