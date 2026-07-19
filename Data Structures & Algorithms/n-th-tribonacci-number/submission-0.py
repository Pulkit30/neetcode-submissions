class Solution:
    def tribonacci(self, n: int) -> int:
        d1=0
        if n==0:
            return d1
        d2=1
        if n==1:
            return d2
        d3=1
        for i in range(3,n+1):
            temp1=d1
            d1=d2
            d2=d3
            d3=temp1+d1+d2
        return d3