class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        p1 = 0
        p2 = 1
        counter = 0
        
        for p2 in range(len(nums)):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
                counter+=1
                p2 += 1

        return counter+1