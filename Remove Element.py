class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums!=[] and val in nums:    
            for i in range(len(nums)):
                p=nums.index(val)
                if nums[i]!=val and i>p:
                    nums[p], nums[i] = nums[i], nums[p]

            return nums.index(val)
        elif nums!=[] and val not in nums:
            return len(nums)
        else:
            return 0