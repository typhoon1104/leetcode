'''
type:数组，哈希表，二分查找，动态规划
Tips:Use dynamic programming. dp[i][j] will be the answer for inputs A[i:], B[j:].
time complexity:O(n*n)
spatial complexity:O(n*n)
time:7-12-2020
'''


class Solution(object):

    # 动态规划
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        row = len(A)
        cols = len(B)

        # 增加一行一列，避免处理跨界判断
        dp = [[0 for _ in range(cols+1)] for _ in range(row+1)]
        max_ = 0
        for i in range(row - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    max_ = max(dp[i][j], max_)
        return max_


a = Solution()
A = [0, 0, 0, 0, 1]
B = [1, 0, 0, 0, 0]

print(a.findLength(A, B))