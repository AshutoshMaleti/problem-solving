class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        d=int(''.join([str(i) for i in d]))+1
        return list(map(int, str(d)))