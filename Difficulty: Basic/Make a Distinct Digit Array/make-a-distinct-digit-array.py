#User function Template for python3

class Solution:
	def common_digits(self, nums):
		aa = []
		for i in nums:
		    while i>0:
		        mod = i%10
		        i = i//10
		        if mod not in aa:
		            aa.append(mod)
		aa.sort()
		return aa
		