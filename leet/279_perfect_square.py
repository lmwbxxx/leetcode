import numpy as np

class Solution:
    """DP

    keeping a private class member is important, so that we avoid
    recalculate from 1 to n every time, we just extend from len(_dp) to n.
    """
    _dp = {1: 1}

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        for i in range(len(dp), n + 1):
            root = int(np.sqrt(i))
            if root ** 2 == i:
                dp[i] = 1
                continue
            min = i
            for j in range(root, 0, -1):
                if j ** 2 * min < i:
                    break
                res = i - j ** 2
                if dp[res] < min:
                    min = dp[res]
            dp[i] = min + 1
        return dp[n]

class Solution2(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
