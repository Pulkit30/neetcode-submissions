class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        d1=cost[0]
        d2=cost[1]
        for i in range(2,n):
            temp=d1
            d1=d2
            d2=cost[i]+min(temp,d1)
        return min(d1,d2)
        