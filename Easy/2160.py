# O(nlogn):
class Solution(object):
    def minimumSum(self, num):
        str_num = sorted(str(num))

        s = int(str_num[0] + str_num[2]) + int(str_num[1] + str_num[3])

        return s
