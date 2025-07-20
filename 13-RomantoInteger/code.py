class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        num = 0
        n=len(s)
        i=0
        while(i<n):
            if i+1<n and roman[s[i+1]]>roman[s[i]]:
                num+=roman[s[i+1]]-roman[s[i]]
                i+=1
            else:
                num+=roman[s[i]]
            i+=1
        return num
        