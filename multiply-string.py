class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                a = num1[-1-i]
                b = num2[-1-j]
                val = int(a) * int(b) + ret[-1-i-j]
                ret[-1-i-j] = val%10
                ret[-2-i-j] += val/10
        i = 0
        while i < len(ret) - 1 and ret[i] == 0:
            i += 1
        return ''.join(map(str,ret[i:]))




if __name__ == "__main__":
	str1 = "999"
	str2 = "999"
	print Solution().multiply(str1,str2)
