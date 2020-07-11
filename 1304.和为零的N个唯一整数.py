'''
数组
'''

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lis = []
        for i in range(1, n // 2 + 1, 1):
            lis.append(i + 1)
            lis.append(-1*(i + 1))
        if n % 2 == 1:
            lis.append(0)
        return lis