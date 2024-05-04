# O(n):
class Solution(object):
    def restoreString(self, s, indices):
        ln = len(s)
        total = [""] * ln
        for i in range(ln):
            total[indices[i]] = s[i]

        return "".join(total)
