class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        if len(s)==0:
            return True
        j = 0 
        lens = len(s)
        for i in range(len(t)):
            if s[j] == t[i] and j<lens:
                j+=1
            if j>=lens:
                return True
        return False
            
        