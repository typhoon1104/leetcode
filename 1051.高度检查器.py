class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h = sorted(heights)
        num = 0
        for i in range(len(heights)):
            if heights[i] != h[i]:
                num += 1
        return num