class Solution:
	def maxProduct(self,arr):
	    pre = 1
	    suff = 1
	    maxii = float('-inf')
		for i in range(len(arr)):
		    if pre == 0:
		        pre = 1
		    if suff == 0:
		        suff = 1
		    pre = pre * arr[i]
		    suff = suff * arr[len(arr)-i-1]
		    maxii = max(maxii,max(pre,suff))
		return maxii