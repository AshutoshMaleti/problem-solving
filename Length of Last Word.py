class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lofs=s.strip(' ').split()
        return len(lofs[-1])