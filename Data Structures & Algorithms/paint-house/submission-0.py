class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        l=len(costs)
        dp=[[-1]*(3+1) for i in range(l+1) ]
        def cost(l,i):
            if l<0:
                return 0
            if dp[l][i]!=-1:
                return dp[l][i]
            mini=float('inf')
            for k in range(3):
                if i!=k:
                    mini=min(mini,costs[l][k]+cost(l-1,k))
            dp[l][i]=mini
            return dp[l][i]
        return cost(l-1,-1)






