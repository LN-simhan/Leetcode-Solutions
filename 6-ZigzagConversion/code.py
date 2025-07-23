class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows =[""]*numRows
        rows[0]+=s[0]
        i=1
        n=len(s)
        if n<numRows or numRows==1:
            return s
        while(i<n):
            print("i->",i,"rows->",rows)
            for j in range(1,numRows):
                if i<n:
                    rows[j]+=s[i]
                    i+=1
            for k in range(numRows-2,-1,-1):
                if i<n:
                    rows[k]+=s[i]
                    i+=1 
        return "".join(rows)
        