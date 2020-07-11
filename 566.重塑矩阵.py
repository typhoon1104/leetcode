class Solution(object):
    def matrixReshape(self, nums, r, c):
        size = len(nums)*len(nums[0])
        if r*c == size:
            flatten = [i for row in nums for i in row]
            return zip(*[iter(flatten)]*c)
        else:
            return nums