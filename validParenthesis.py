class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dic = {'(':')', '{':'}', '[':']'}
        op = dic.keys()
        stack = []
        for i in s:
            if i in op:
                stack.append(i)
            elif len(stack) == 0 and i not in op:
                return False
            elif i != dic[stack.pop()]:
                return False
        if len(stack) != 0:
            return False
        return True


        