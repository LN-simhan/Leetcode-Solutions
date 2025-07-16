class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count = 1 if nums[0]%2==0 else 0
        odd_count = 1 if nums[0]%2==1 else 0
        expect_even = True if odd_count else False
        length=1

        for i in range(1,len(nums)):
            if (nums[i]%2==0 and expect_even==True) or (nums[i]%2==1 and expect_even==False):
                expect_even= not expect_even
                length+=1
            if nums[i]%2==0:
                even_count+=1
            else:
                odd_count+=1        
        return max(length,odd_count,even_count)


        