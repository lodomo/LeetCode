class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        This is NOT my solution. I copied it from LeetCode.
        I need to learn what this all even means. 
        I do not have a grasp of bitwise operations.
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == -2**31 and divisor == 1:
            return -2**31

        negative = (dividend < 0) ^ (divisor < 0)

        absDividend, absDivisor = abs(dividend), abs(divisor)

        quotient = 0

        while absDividend >= absDivisor:
            tempDivisor, multiple = absDivisor, 1
            while absDividend >= (tempDivisor << 1):
                tempDivisor <<= 1
                multiple <<= 1
            absDividend -= tempDivisor
            quotient += multiple

        return -quotient if negative else quotient
