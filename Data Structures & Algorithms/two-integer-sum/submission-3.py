class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = target - nums[i]

            if j in nums[i+1:]:
                id2 = nums[i+1:].index(j)
                
                return [i, i+id2+1]
        