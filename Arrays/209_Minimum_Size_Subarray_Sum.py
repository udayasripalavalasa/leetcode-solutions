class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        right=0
        total=0
        min_sum=float('inf')
        for right in range(len(nums)):
            total=total+nums[right]
            while total>=target:
                min_sum=min(min_sum,right-left+1)
                total=total-nums[left]
                left=left+1
        if min_sum==float('inf'):
            return 0
        return min_sum
        