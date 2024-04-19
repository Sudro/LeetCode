# O(nk)
class Solution(object):
    def groupAnagrams(self, strs):
        sl = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1

            sl[tuple(count)].append(s)
            
        return sl.values()

# O(nklogn):
class Solution(object):
    def groupAnagrams(self, strs):
        sl = {}
        for i in range(len(strs)):
            sort_str = ''.join(sorted(strs[i]))
            #print(sort_str)
            if sort_str not in sl:
                sl[sort_str] = [strs[i]]
            else:
                sl[sort_str] += [strs[i]]
        
        return sl.values()

# O(nklogn):
class Solution(object):
    def groupAnagrams(self, strs):
        sl = {}
        for i in range(len(strs)):
            sort_str = ''.join(sorted(strs[i]))
            #print(sort_str)
            if sort_str not in sl:
                sl[sort_str] = [strs[i]]
            else:
                sl[sort_str] += [strs[i]]
        
        strs = []
        for i in sl.keys():
            strs.append(sl[i])
        return strs