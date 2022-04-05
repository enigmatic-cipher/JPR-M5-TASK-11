"""
Given a number n as input, calculate the sum of its digits.
Input-> 29013
output-> 15
"""

def sum_of_digit(n):
  sum = 0
  num = str(n)
  for digit in num:
    sum = sum + int(digit)
  print(sum)
    
num = 29013
sum_of_digit(num)
  