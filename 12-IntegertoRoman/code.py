class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]]
        inp = num
        res =""
        
        for val,sym in roman:
            count = inp//val
            if count>0:
                res+=(sym*count)
                inp = inp%val
        return res
            
        