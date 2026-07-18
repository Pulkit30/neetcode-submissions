class Solution:
    def climbStairs(self, n: int) -> int:
        d1=1
        if n==1:
            return d1
        d2=2
        for i in range(3,n+1):
            temp=d1
            d1=d2
            d2=temp+d1
        return d2