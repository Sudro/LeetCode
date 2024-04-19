# O(n):
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        hashmap1, hashmap2 = {}, {}
        for elem in s:
            if elem not in hashmap1:
                hashmap1[elem] = 1
            else:
                hashmap1[elem] += 1
        
        for elem in t:
            if elem not in hashmap2:
                hashmap2[elem] = 1
            else:
                hashmap2[elem] += 1
        
        for elem in hashmap1:
            if elem in hashmap2:
                if hashmap1[elem] != hashmap2[elem]:
                    return False
            else:
                return False
        return True

# O(nlogn):
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)