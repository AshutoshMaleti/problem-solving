class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>0 else -1
        num = str(abs(x))
        reverse = int(num[::-1])*sign
        
        if -2**31 <= reverse <= 2**31 - 1:
            return reverse
        
        return 0