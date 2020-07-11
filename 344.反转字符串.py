# 双指针，字符串

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s[::] = s[::-1]
        