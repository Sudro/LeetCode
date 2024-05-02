# First solution
class Solution(object):
    def cellsInRange(self, s):
        total = []
        s0, s1, s3, s4 = ord(s[0]), int(s[1]), ord(s[3])+1, int(s[4])+1
        for i in range(s0, s3):
            for j in range(s1, s4):
                total.append(chr(i) + str(j))
        return total

# Second solution (Three line)
class Solution(object):
    def cellsInRange(self, s):
        return [chr(elem1) + str(elem2) for elem1 in range(ord(s[0]), ord(s[3])+1) for elem2 in range(int(s[1]), int(s[4])+1)]
