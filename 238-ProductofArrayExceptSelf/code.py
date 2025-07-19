class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        n = len(nums)
        left_arr = [0]*n
        for i in range(n):
            left_arr[i]= left
            left=left*nums[i]
        right=1
        for j in range(n-1,-1,-1):
            left_arr[j]*=right
            right*=nums[j]
        return left_arr