class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for i in range(last,-1,-1):
            jumps = nums[i]
            if i+jumps>=last:
                last = i

        if last==0:
            return True
        else:
            return False
        