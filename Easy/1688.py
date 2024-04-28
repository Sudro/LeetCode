# O(1):
class Solution(object):
    def numberOfMatches(self, n):
        return n-1

# O(n):
class Solution(object):
    def numberOfMatches(self, n):
        c = 0
        while n != 1:
            rev = n // 2
            c += rev
            n -= rev
        return c
