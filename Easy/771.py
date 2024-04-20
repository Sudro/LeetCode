# O(nk):
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        newJewels = set(jewels)
        c = 0
        for i in range(len(newJewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    c += 1
        return c

# O(nk):
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        newJewels = set()
        for elem in jewels:
            newJewels.add(elem)

        c = 0
        for jewel in newJewels:
            for stone in stones:
                if jewel == stone:
                    c += 1
        return c