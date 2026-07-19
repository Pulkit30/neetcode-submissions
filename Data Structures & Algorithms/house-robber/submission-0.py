class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        d1=nums[0]
        if n==1:
            return d1
        d2=max(nums[0],nums[1])
        for i in range(3,n+1):
            take=nums[i-1]+d1
            skip=d2
            d1=d2
            d2=max(take,skip)
        return d2
