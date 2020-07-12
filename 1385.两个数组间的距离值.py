'''
type:数组
Tips:Sort 'arr2' and use binary search to get the closest element for each 'arr1[i]',
     it gives a time complexity of O(nlogn).
time complexity:O(nlogn)
spatial complexity:O(1)
time:7-12-2020
'''


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        num = 0
        for arr in arr1:
            if self.binary_searchz(arr, arr2, d):
                num += 1
        return num

    def binary_searchz(self, arr, arr2, d):
        low = 0
        high = len(arr2)-1
        while low <= high:
            mid = (low+high)//2
            data = arr2[mid] - arr
            if data > d:
                high = mid - 1
            elif data < d and abs(data) > d:
                low = mid + 1
            else:
                return False
        return True