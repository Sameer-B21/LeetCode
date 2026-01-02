class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # runtime = O(n)
        r, l = 0, 0
        total = 0
        dup = {}
        while r < len(s):
            if s[r] in dup:
                l = max(l, dup[s[r]] + 1)
            total = max(total, r-l+1)
            dup[s[r]] = r
            r+=1
        return total
    


        # runtime = O(n^2)
        # que = []
        # total = 0
        # dup = set()
        # for i in s:
        #     if i not in dup:
        #         que.append(i)
        #         dup.add(i)
        #     elif i in dup: 
        #         total = max(total, len(que))
        #         idx = que.index(i)
        #         for x in que[:idx+1]:
        #             dup.remove(x)
        #         que = que[idx+1:]
        #         que.append(i)
        #         dup.add(i)
        # return max(total, len(que))


        
            
