# O(n):
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        sl = {"type": 0, "color": 1, "name": 2}
        return sum(1 for elem in items if elem[sl[ruleKey]] == ruleValue)

# O(n):
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        k = 0
        for i in range(len(items)):
            if ruleKey == "type":
                if ruleValue == items[i][0]:
                    k += 1
            elif ruleKey == "color":
                if ruleValue == items[i][1]:
                    k += 1
            else:
                if ruleValue == items[i][2]:
                    k += 1
        return k
