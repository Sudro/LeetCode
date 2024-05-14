# O(n)
class Solution(object):
    def maxArea(self, height):
        mx = 0
        left, right = 0, len(height)-1

        while left < right:
            if height[left] <= height[right]:
                total = (right-left) * height[left]
                left += 1
            else:
                total = (right-left) * height[right]
                right -= 1
            mx = max(mx, total)
            
        return mx
