# O(nk):
class Solution(object):
    def maximumWealth(self, accounts):
        return max(sum(i) for i in accounts)

# O(nk):
class Solution(object):
    def maximumWealth(self, accounts):
        mx = 0
        ln = len(accounts)
        for i in range(ln):
            ln2 = len(accounts[i])
            s = 0
            for j in range(ln2):
                s += accounts[i][j]
            if s > mx:
                mx = s
        return mx