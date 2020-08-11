'''
树，动态规划
Tips:
假设n个节点存在二叉排序树的个数是G(n)，1为根节点，2为根节点，...，n为根节点，
当1为根节点时，其左子树节点个数为0，右子树节点个数为n-1，同理当2为根节点时，其左子树节点个数为1，
右子树节点为n-2，所以可得G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)

time complexity:O(n*n)
spatial complexity:O(1)
time:7-25-2020
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
