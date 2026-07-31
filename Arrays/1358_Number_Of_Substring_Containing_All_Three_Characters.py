class Solution(object):
    def numberOfSubstrings(self, s):
        last_seen=[-1,-1,-1]
        count=0
        for i in range(len(s)):
            if s[i]=='a':
                last_seen[0]=i
            elif s[i]=='b':
                last_seen[1]=i
            elif s[i]=='c':
                last_seen[2]=i
            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                count=count+min(last_seen)+1
        return count