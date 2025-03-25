class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        prev = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for char in reversed(s):
            curr = dic[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total