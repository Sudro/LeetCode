# O(nk), но память O(1):
class Solution(object):
    def findWordsContaining(self, words, x):
        return [elem for elem in range(len(words)) if x in words[elem]]

# O(nk), но память O(1):
class Solution(object):
    def findWordsContaining(self, words, x):
        return [i for i,y in enumerate(words) if x in y]

# O(nk):
class Solution(object):
    def findWordsContaining(self, words, x):
        mas = []
        for i in range(len(words)):
            s = set(words[i])
            if x in s:
                mas.append(i)
        return mas

# O(nk):
class Solution(object):
    def findWordsContaining(self, words, x):
        mas = []
        for i in range(len(words)):
            s = set(words[i])
            for sElem in s:
                if sElem == x:
                    mas.append(i)
                    break
        return mas