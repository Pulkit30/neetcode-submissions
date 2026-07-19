class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def robber(arr,n):
            if n==0:
                return 0
            d1=arr[0]
            if n==1:
                return d1
            d2=max(arr[0],arr[1])
            for i in range(3,n+1):
                take=arr[i-1]+d1
                skip=d2
                d1=d2
                d2=max(take,skip)
            return d2
        return max(robber(nums[:n-1],n-1),robber(nums[1:n],n-1))
