class Solution:
    def countDistinct(self, arr, k):
        dic = dict()
        res = []
        for i in range(k):
            if arr[i] in dic:
                dic[arr[i]] += 1
            else:
                dic[arr[i]] = 1
        res.append(len(dic))
        for j in range(k,len(arr)):
            if arr[j] in dic:
                dic[arr[j]] += 1
            else:
                dic[arr[j]] = 1
            dic[arr[j-k]] -= 1
            if dic[arr[j-k]] == 0:
                del dic[arr[j-k]]
            res.append(len(dic))
        return res