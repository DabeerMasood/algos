class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t = collections.Counter(t)
        s = collections.Counter(s)
        for key in t:
            if (key in s and t[key] != s[key]) or (key not in s):
                return key
        
        
