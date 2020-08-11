'''
type:二分查找，动态规划
Tips:需要判断，动态规划需要从前往后，还是从后往前：消耗求最小从后往前。
time complexity:O(n*n)
spatial complexity:O(n*n)
time:7-12-2020
'''


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        cols = len(dungeon[0])
        dp = [[10000 for _ in range(cols+1)] for _ in range(row+1)]
        dp[row-1][cols] = 1
        dp[row][cols-1] = 1
        for i in range(row-1, -1, -1):
            for j in range(cols-1, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]


a = Solution()
A = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(a.calculateMinimumHP(A))