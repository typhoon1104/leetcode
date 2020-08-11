'''
数组，动态规划
Tips:
time complexity:O(n*n)
spatial complexity:O(1)
time:7-14-2020
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

a = Solution()
b = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(a.minimumTotal(b))