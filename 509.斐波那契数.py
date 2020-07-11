class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        data = 1
        if N > 2:
            t = 1
            for i in range(3, N+1, 1):
                data, t = t, data
                data += t
        elif N==0:
            return 0
        return data