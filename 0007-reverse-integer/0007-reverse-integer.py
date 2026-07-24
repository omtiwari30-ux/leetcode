class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        s = str(x)
        if s[0] == '-':
            rev = int('-' + s[:0:-1])
        else:
            rev = int(s[::-1])
        
        if rev < -2147483648 or rev > 2147483647:
            return 0
            
        return rev

