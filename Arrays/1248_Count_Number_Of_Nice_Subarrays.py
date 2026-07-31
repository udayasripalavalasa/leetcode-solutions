class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def fun(nums,k):
            if k<0:
                return 0
            left=0
            right=0
            odd=0
            count=0
            for right in range(len(nums)):
                odd=odd+nums[right]%2
                while(odd>k):
                    odd=odd-nums[left]%2
                    left=left+1
                count=count+(right-left+1)
            return count
        return fun(nums,k)-fun(nums,k-1)
        