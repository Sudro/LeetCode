# O(1):
class Solution(object):
    def pivotInteger(self, n):
        sr_ar = n * (n + 1) // 2
        pivot = int(sqrt(sr_ar))
        if pivot * pivot == sr_ar:
            return pivot
        return -1

# O(n):
class Solution(object):
    def pivotInteger(self, n):
        s_l = 0
        s = n*(n+1)//2
        for i in range(1, n+1):
            s_l += i-1
            s_r = s - s_l - i
            if s_l == s_r:
                return i
        return -1
