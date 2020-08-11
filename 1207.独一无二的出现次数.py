

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict_frequency = {}
        for data in arr:
            if data not in dict_frequency.keys():
                dict_frequency[data] = 0
            dict_frequency[data] += 1
        if len(set(dict_frequency.values())) == len(dict_frequency.values()):
            return True
        else:
            return False
