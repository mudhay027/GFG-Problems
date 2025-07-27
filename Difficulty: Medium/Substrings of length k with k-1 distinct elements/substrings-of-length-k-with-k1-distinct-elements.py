from collections import defaultdict
class Solution:
    def substrCount(self, s, k):
        dic = defaultdict(int)
        count = 0
        for i in range(len(s)):
            if i >= k:
                dic[s[i-k]] -= 1
                if dic[s[i-k]] == 0:
                    del dic[s[i-k]]
            dic[s[i]] += 1
            if i >= k-1 and len(dic) == k-1:
                count += 1
        return count