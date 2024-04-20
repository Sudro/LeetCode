# O(n):
class Solution(object):
    def differenceOfSums(self, n, m):
        return sum(i for i in range(1, n+1) if i % m != 0) - sum(i for i in range(1, n+1) if i % m == 0)

# O(1):
class Solution(object):
    def differenceOfSums(self, n, m):
        s = (n+1) * n/2 # сумма всех чисел
        k = n / m # количество чисел, которые делятся на m
        mul = (k+1) * k/2 * m * 2 # сумма чисел, делящихся на 3
        return s - mul