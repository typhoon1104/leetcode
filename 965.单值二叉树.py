# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        data = root.val
        stack = [root]
        while stack:
            if root:
                stack.append(root.left)
                root = root.left
            else:
                root = stack.pop()
                if root.val != data:
                    return False
                root = root.right
        return True

    midOrder(node * t)
    {
    stack < node * > sta;
    while (t | |  !sta.empty() )
    {
    if (t != nullptr)
    {
        sta.push(t);
    t = t->left;
    }
    else
    {
        t = sta.top();
    sta.pop();
    cout << t->val << " ";
    t = t->right;
    }
    }





