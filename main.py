#Given an integer n, return the number of trailing zeroes in n!.
def fast_trailing_zero_factorial(n):
  ans = 0
  val = n%5
  ans = n - val
  ans = ans/5
  if n>24:
    n = n - n%25
    ans = ans + n/25
  return ans

#print("Enter number")
#n = input()
#n = int(n)
#print("The number of trailing zeroes is " + str(fast_trailing_zero_factorial(n)))