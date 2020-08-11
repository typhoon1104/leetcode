class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        num_empty = numBottles
        while num_empty >= numExchange:
            temp = num_empty / numExchange
            numBottles = temp + numBottles
            num_empty = num_empty % numExchange + temp
        return