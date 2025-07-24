class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)

        for i in range(h):
            j = 0
            for k in range(i,h):
                if needle[j]==haystack[k]:
                    j+=1
                else:
                    break
                if j == n:
                    return i
        return -1