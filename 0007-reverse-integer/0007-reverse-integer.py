class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
    
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

        result = rev * sign
        
        if result < MIN_INT or result > MAX_INT:
            return 0
            
        return result
