class Solution(object):
    def frequencySort(self, s): 
        h_map={}
        for num in s:
            if num in h_map:
                h_map[num]=h_map[num]+1
            else:
                h_map[num]=1
        s1=sorted(h_map.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for ch,fr in s1:
            ans=ans+ch*fr
        return ans
        