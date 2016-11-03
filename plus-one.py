import time
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c = 1
        for i in xrange(0,len(digits)):
             val = digits[-1-i] + c
             c = val / 10
             digits[-1-i] = val % 10
        if c == 1:
            return [1] + digits
        return digits

    def plusOne2(self, digits):
        carry = 1
        for i in reversed(xrange(len(digits))):
            digits[i] += carry
            carry = digits[i] / 10
            digits[i] %= 10
        
        if carry:
            digits = [1] + digits
        
        return digits

if __name__ == "__main__":
    l = range(0,100000)
    t1 = time.time()
    Solution().plusOne2(l)
    print "%.6f" % (time.time() - t1)
    t1 = time.time()
    Solution().plusOne(l)
    print "%.6f" % (time.time() - t1)