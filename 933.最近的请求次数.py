'''
type:队列
time complexity:O(n)
spatial complexity:O(1)
time:7-12-2020
'''

class RecentCounter(object):

    def __init__(self):
        self.time_list = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.time_list.append(t)
        while True:
            time = self.time_list[0]
            if time < t-3000:
                self.time_list.remove(time)
            else:
                break
        return len(self.time_list)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)