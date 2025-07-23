class Solution:
    def reverseWords(self, s: str) -> str:
        new_string = " ".join(s.strip().split(" ")[::-1])
        ret=[]
        for i,val in enumerate(new_string):
            if i<len(new_string)-1 and new_string[i]==new_string[i+1]==" ":
                i+=1
            else:
                ret.append(val)
                i+=1
        return "".join(ret)


        