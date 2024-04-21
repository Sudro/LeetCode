# O(n):
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        mas = []
        max_candies = max(candies)
        for candie in candies:
            if extraCandies + candie >= max_candies:
                mas.append(True)
            else:
                mas.append(False)
        return mas