class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            mul = -1
        else:
            mul = 1

        s = str(abs(x))
        s = int(s[::-1])
        if x<0:
            s = -1 * s
        if -2**31 < s < 2**31:
            return s
        else:
            return 0

        