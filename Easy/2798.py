# O(n):
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return len([elem for elem in hours if elem >= target])