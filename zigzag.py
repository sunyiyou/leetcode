class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        step = 2 * numRows - 2
        ret = ""
        for i in xrange(numRows):
            for j in xrange(i,len(s),step):
                ret += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    ret += s[j + step - 2 * i]
        return ret





if __name__ == '__main__':
    ret = Solution().convert('PAYPALISHIRING',4)
    print ret
