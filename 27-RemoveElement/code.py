class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total_len=len(nums)
        writer = 0

        for reader in range(len(nums)):
            if nums[reader]!=val:
                nums[writer]=nums[reader]
                writer+=1
        return writer