# O(n):
class Solution(object):
    def numberOfSteps(self, num):
        step = 0
        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            step += 1
        return step
