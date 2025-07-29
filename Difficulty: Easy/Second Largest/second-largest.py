class Solution:
    def getSecondLargest(self, arr):
        max = 0
        sec_max = 0
        for i in arr:
            if max<i:
                sec_max = max
                max = i
            if sec_max<i and max>i:
                sec_max = i
        return -1 if sec_max == 0 else sec_max