class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer=1
        old_val=nums[0]
        for reader in range(1,len(nums)):
            if nums[reader]!=old_val:
                nums[writer]=nums[reader]
                old_val=nums[reader]
                writer+=1
        return writer

        