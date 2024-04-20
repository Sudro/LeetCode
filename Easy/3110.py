# O(n):
class Solution(object):
    def scoreOfString(self, s):
        summatory = 0
        for i in range(len(s)-1):
            ordS1, ordS2 = ord(s[i]), ord(s[i+1])
            if (ordS1 - ordS2) < 0:
                summatory -= ordS1 - ordS2
            else:
                summatory += ordS1 - ordS2
        return summatory

# O(n):
class Solution(object):
    def scoreOfString(self, s):
        summatory = 0
        for i in range(len(s)-1):
            summatory += abs(ord(s[i]) - ord(s[i+1]))
        return summatory