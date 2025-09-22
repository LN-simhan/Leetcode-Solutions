class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        counter = defaultdict(int)
        for num in nums:
            counter[num]+=1
        max_frequency = max(counter.values())
        total =0 
        for i in counter.keys():
            if counter[i]==max_frequency:
                total+=max_frequency
        return total