# O(n):
class Solution(object):
    def finalValueAfterOperations(self, operations):
        X = 0
        for elem in operations:
            if elem == "--X" or elem == "X--":
                X -= 1
            else:
                X += 1
        return X