# O(n^2):
class Solution(object):
    def mostWordsFound(self, sentences):
        return max(len(sentence.split()) for sentence in sentences)
