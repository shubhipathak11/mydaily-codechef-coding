# Problem
# A tutorial for this problem is now available on our blog. Click here to read it.
# You are asked to calculate factorials of some small positive integers.
#
# Input
# An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1<=n<=100.
#
# Output
# For each integer n given at input, display a line with the value of n!
#
# Sample 1:
# Input
# Output
# 4
# 1
# 2
# 5
# 3
# 1
# 2
# 120
# 6
# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

#Note that it's python3 Code. Here, we are using input() instead of raw_input().
#You can check on your local machine the version of python by typing "python --version" in the terminal.

def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
for i in range(n):
    num=int(input())
    print(factorial(num))




