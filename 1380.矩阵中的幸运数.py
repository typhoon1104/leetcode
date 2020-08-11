class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        max_list = []
        min_list = []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            min_list.append(min(matrix[i]))
        for j in range(m):
            max_ = 0
            for i in range(n):
                max_ = max(matrix[i][j], max_)
            max_list.append(max_)

        return list(set(max_list) & set(min_list))