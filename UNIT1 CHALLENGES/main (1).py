#1 recursive function to calculate factorial
def fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact(n - 1)


number = int(input("enter number to find factorial:"))
res = fact(number)
print("the factorial of {} is {}".format(number, res))
