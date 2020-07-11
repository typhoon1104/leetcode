class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr2 += sorted(set(arr1) - set(arr2))
        arr1.sort(key=arr2.index)
        return arr1