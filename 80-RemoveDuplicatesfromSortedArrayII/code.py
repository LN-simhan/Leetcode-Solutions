class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        oldval=nums[0]
        freq=1
        writer=1

        for reader in range(1,len(nums)):
            if nums[reader] == oldval and freq!=2:
                freq+=1
                nums[writer]=nums[reader]
                writer+=1
                pass
            elif nums[reader] == oldval and freq==2:
                pass
            elif nums[reader]!=oldval:
                nums[writer]=nums[reader]
                writer+=1
                oldval=nums[reader]
                freq=1
        return writer

        