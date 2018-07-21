class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        dq = collections.deque()
        ans = collections.deque()
        S= S.upper()
        j = [i for i in S if i!="-"]
        # j = j[::-1]
        i=len(j)-1
        while i>=0:
            dq.appendleft(j[i])
            if(len(dq)==K):
                ans.appendleft(''.join([i for i in dq]))
                ans.appendleft("-")
                dq = collections.deque()
            i-=1
        if len(dq)!= 0:
            return ''.join([i for i in dq])+ ''.join([i for i in ans])
        return ''.join([i for i in ans])[1:]
