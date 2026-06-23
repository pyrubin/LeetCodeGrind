class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = "".join(str(i) for i in digits)
        temp = int(a)+1
        digits[:] = []
        for i in str(temp):
            digits.append(int(i))
        return digits
