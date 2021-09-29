class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        for i in range(len(n)-1):
            for j in range(i+1,len(n)):
                if n[i]+n[j]==t:
                    return [i,j]


'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i, num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num],i]
            elif num not in seen:
                seen[num]=i'''