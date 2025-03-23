class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tmp=str(x)
        rev=tmp[::-1]
        return tmp==rev