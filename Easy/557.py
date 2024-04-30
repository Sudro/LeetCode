# O(n^2):
class Solution(object):
    def reverseWords(self, s):
        return " ".join(elem[::-1] for elem in s.split())
    
# O(n^2):
class Solution(object):
    def reverseWords(self, s):
        d = s.split()
        for i in range(len(d)):
            d[i] = d[i][::-1]
        return " ".join(d)
