class Solution:
    def InfixtoPostfix(self, s):
        precedence = {
            '^':3,
            '*':2,
            '/':2,
            '+':1,
            '-':1
        }
        stack = []
        output = []
        
        def is_operator(c):
            return c in precedence
        def is_higher(op1,op2):
            return precedence[op1] >= precedence[op2]
            
        for token in s:
            if token.isalnum():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif is_operator(token):
                while (stack and stack[-1] != '(' and is_operator(stack[-1]) and is_higher(stack[-1],token)):
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return ''.join(output)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        exp = str(input())
        ob = Solution()
        print(ob.InfixtoPostfix(exp))
        print("~")

# } Driver Code Ends