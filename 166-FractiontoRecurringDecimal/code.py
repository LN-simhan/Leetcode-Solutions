class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"

        res=[]
        
        if (numerator<0) != (denominator<0):
            res.append("-")
        
        num,den = abs(numerator), abs(denominator)
        res.append(str(num//den))
        rem = num%den
        if rem == 0:
            return "".join(res)
        res.append(".")
        res_pos = {}
        while rem!=0:
            if rem in res_pos:
                pos = res_pos[rem]
                res.insert(pos,"(")
                res.append(")")
                break
            res_pos[rem]=len(res)
            rem*=10
            res.append(str(rem//den))
            rem%=den
        return "".join(res)

        