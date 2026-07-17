class Solution:
    def longestKSubstr(self, s, k):
        l=0
        r=0
        mpp={}
        m_le=0
        while(r<len(s)):
            if s[r] in mpp:
                mpp[s[r]]=mpp[s[r]]+1
            else:
                mpp[s[r]]=1
            if len(mpp)>k:
                mpp[s[l]]=mpp[s[l]]-1
                if mpp[s[l]]==0:
                    del mpp[s[l]]
                l=l+1
            if(len(mpp)==k):
                m_le=max(m_le,r-l+1)
            r=r+1
        if m_le==0:
            return -1
        else:
            return m_le
                