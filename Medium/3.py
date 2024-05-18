# O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        left = 0
        mx_length = 0
        unique_set = set()
        
        for right in range(len(s)):
            while s[right] in unique_set:
                unique_set.remove(s[left])
                left += 1
            unique_set.add(s[right])
            mx_length = max(mx_length, right-left+1)

        return mx_length
