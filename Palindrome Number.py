class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        s=str(x)
        length=len(s)
        mid=length//2
        
        if length%2!=0 and s[0:mid]==s[length:mid:-1]:
            return True
        elif s[0:mid]==s[length:mid-1:-1]:
            return True
        return False