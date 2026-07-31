class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def fun(nums,goal):
            if(goal<0):
                return 0
            left=0
            right=0
            total=0
            count=0
            for right in range(len(nums)):
                total=total+nums[right]
                while(total>goal):
                    total=total-nums[left]
                    left=left+1
                count=count+(right-left+1)
            return count
        return fun(nums,goal)-fun(nums,goal-1)

