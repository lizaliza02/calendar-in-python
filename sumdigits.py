def SumDigits(n):
  total = 0
  #to iterate over the digit in n
  for num in n:
    num = int(num)
    total += num
  return total

number = input("Enter more than two digits: ")

result = SumDigits(number)
print(f"The sum is {result}.")