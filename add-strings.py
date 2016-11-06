class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = []
        c = 0
        for i in range(max(len(num1),len(num2))):
            val = c
            if(i < len(num1)):
                val += int(num1[-1-i])
            if(i < len(num2)):
                val += int(num2[-1-i])
            ret.append(str(val%10))
            c = val / 10

        if c == 1:
            ret.append("1")
        ret.reverse()
        return "".join(ret)
