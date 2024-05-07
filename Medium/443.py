# O(n):
class Solution(object):
    def compress(self, chars):
        ans = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            k = 0

            while i < len(chars) and chars[i] == letter:
                k += 1
                i += 1

            chars[ans] = letter
            ans += 1
            if k > 1:
                for c in str(k):
                    chars[ans] = c
                    ans += 1
        return ans


# The solution is correct, but does not pass the tests on the leetcode:
# O(n):
class Solution(object):
    def compress(self, chars):
        sl = {}
        for i in range(len(chars)): 
            if chars[i] not in sl:
                sl[str(chars[i])] = 1
            else:
                sl[str(chars[i])] += 1
        
        arr = []
        for elem in sl.keys(): 
            arr.append(elem)
            if sl[elem] != 1:
                st = str(sl[elem])
                for digit in st: 
                    arr.append(digit)

        for i in range(len(arr)):
            chars[i] = arr[i]
        return len(chars)
