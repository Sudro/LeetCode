# O(n):
class Solution(object):
    def truncateSentence(self, s, k):
        return " ".join(s.split()[:k])
