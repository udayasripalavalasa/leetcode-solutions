class Solution(object):
    def checkInclusion(self, s1, s2):
        for right in range(len(s2)-len(s1)+1):
            window = s2[right:right+len(s1)]
            
            if sorted(window) == sorted(s1):
                return True
        
        return False