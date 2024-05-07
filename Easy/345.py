# O(n):
class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        start, end = 0, len(s)-1
        m = "aeiouAEIOU"

        while start < end:
            if s[start] in m and s[end] in m:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start] not in m:
                start += 1
            elif s[end] not in m:
                end -= 1
                
        return ''.join(s)


# O(n):
class Solution(object):
    def reverseVowels(self, s):
        d = []
        m = list(s)

        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                d.append(i)

        ln = len(d)
        for i in range(ln//2):
            temp = m[d[i]]
            m[d[i]] = m[d[ln-i-1]]
            m[d[ln-i-1]] = temp

        return "".join(m)
