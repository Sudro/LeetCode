# O(n):
class Solution(object):
    def mergeAlternately(self, word1, word2):
        s = ""
        ln1, ln2 = len(word1), len(word2)
        mn = min(ln1, ln2)

        for i in range(mn):
            s += word1[i]
            s += word2[i]

        if ln1 < ln2:
            s += word2[ln1:]
        else: 
            s += word1[ln2:]

        return s

# O(n):
class Solution(object):
    def mergeAlternately(self, word1, word2):
        s = ""
        ln1, ln2 = len(word1), len(word2)

        if ln1 == ln2:
            for i in range(ln1):
                s += word1[i]
                s += word2[i]
        elif ln1 < ln2:
            for i in range(ln1):
                s += word1[i]
                s += word2[i]
            s += word2[ln1:]
        else: # ln2 < ln1
            for i in range(ln2):
                s += word1[i]
                s += word2[i]
            s += word1[ln2:]

        return s
