class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX =  2147483647
        sign = x > 0 and 1 or -1
        x = abs(x)
        result = 0
        while x != 0:
            a = x % 10
            x = x / 10
            if result  > (INT_MAX - a) / 10:
                return 0
            result = result * 10 + a
        return sign * result

if __name__ == "__main__":
    print Solution().reverse(1000000003)
