'''
贪心算法
'''

class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_list = sum(nums)*1.0 / 2
        nums.sort(reverse=True)
        for i in range(1, len(nums), 1):
            if sum(nums[:i]) > sum_list:
                return nums[:i]