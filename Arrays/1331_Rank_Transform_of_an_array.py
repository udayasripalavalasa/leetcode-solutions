class Solution(object):
    def arrayRankTransform(self, arr):
        u_numbers=sorted(set(arr))
        h_map={}
        c_rank=1
        for num in u_numbers:
            h_map[num]=c_rank
            c_rank=c_rank+1
        ans=[]
        for i in arr:
            ans.append(h_map[i])
        return ans
