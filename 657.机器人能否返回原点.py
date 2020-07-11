'''
字符串
'''


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up_down = 0
        right_left = 0
        l = len(moves)
        for i in range(l):
            move = moves[l]
            if move == 'R':
                right_left += 1
            elif move == 'L':
                right_left -= 1
            elif move == 'U':
                up_down += 1
            elif move == 'D':
                up_down -= 1
            else:
                pass
        if up_down == 0 and right_left == 0:
            return True
        else:
            return False
