class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "1234567890qwertyuiopasdfghjklzxcvbnm"
        l = [i.lower() for i in s if i.lower() in valid]
        first=0
        last=len(l)-1
        while(first<=last):
            if l[first]==l[last]:
                first+=1
                last-=1
            else:
                return False
        return True
        