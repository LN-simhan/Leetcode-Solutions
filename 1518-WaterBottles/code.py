class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numExchange>numBottles:
            return numBottles
        empty = numBottles
        drink = numBottles
        full = 0
        while empty>=numExchange:
            full = empty//numExchange
            empty = empty%numExchange
            drink+=full
            empty+=full
        return drink