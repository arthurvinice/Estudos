# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.

class Solution:
    def mySqrt(self, x: int) -> int:
        root = x ** 0.5
        root = int(root)
        return root

solution = Solution()
x = 8
print(solution.mySqrt(x))
