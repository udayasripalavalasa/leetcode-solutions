class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def fun(k):
            if k<0:
                return 0
            left=0
            right=0
            count=0
            mpp={}
            for right in range(len(nums)):
                if nums[right] in mpp:
                    mpp[nums[right]]+=1
                else:
                    mpp[nums[right]]=1
                while len(mpp)>k:
                    mpp[nums[left]]-=1
                    if(mpp[nums[left]]==0):
                        del mpp[nums[left]]
                    left=left+1
                count=count+(right-left+1)
            return count
        return fun(k)-fun(k-1)
