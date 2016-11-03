import time
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        ret = []
        c = 0
        
        for i in range(max(len(a),len(b))):
            val = c
            if i < len(a):
                val += int(a[-1-i])
            if i < len(b):
                val += int(b[-1-i])
            c,val = val//2,val%2
            ret.append(str(val))
        if c == 1:
            ret.append("1")
        ret.reverse()
        return "".join(ret)
                
    def addBinary2(self, a, b):
        result, carry, val = "", 0, 0
        for i in xrange(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b): 
                val += int(b[-(i + 1)])
            carry, val = val / 2, val % 2
            result += str(val)
        if carry:
            result += str(carry)
        return result[::-1]


if __name__ == '__main__':
    s = ''.join(['1' for i in range(100000)])
    t1 = time.time()
    result = Solution().addBinary(s, s)
    print "%.6f" % (time.time() - t1)
    t1 = time.time()
    result = Solution().addBinary2(s, s)
    print "%.6f" % (time.time() - t1)
    # print result