# O(n):
class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0

        while i < len(t):
            if j < len(s) and s[j] == t[i]:
                j += 1
            i += 1
            
        return j == len(s)
