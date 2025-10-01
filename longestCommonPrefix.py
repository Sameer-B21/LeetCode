class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        s = min(strs, key=len)
        
        for n in range(len(s)):
            for i in strs:
                if s[n] != i[n]:
                    return s[0:n]
        return s
