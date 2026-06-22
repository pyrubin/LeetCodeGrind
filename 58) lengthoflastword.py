class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split() ## .split(" ") counts white spaces also so just .split() doest count " "
        last = words[-1]
        length = len(last)
        return length
