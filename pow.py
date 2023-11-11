def pow10(n):
  if n == 0: # base case
   return 1
  else:
    return pow10(n-1) * 10
pow10(5)