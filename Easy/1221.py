# O(n):
class Solution(object):
    def balancedStringSplit(self, s):
        c, k = 0, 0
        for elem in s:
            if elem == "L": c += 1
            else: c -= 1
            if c == 0: k += 1
        return k

# O(n):
class Solution(object):
    def balancedStringSplit(self, s):
        k_l, k_r = 0, 0
        c = 0
        for elem in s:
            if elem == "L":
                k_l += 1
            else:
                k_r += 1

            if k_l == k_r:
                c += 1
        return c
