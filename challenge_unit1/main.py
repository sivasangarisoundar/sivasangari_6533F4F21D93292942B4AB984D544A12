def fact_rec(n):
  if n==0 or n==1:
     return;
  else:
    return n*fact_rec(n-1)
number=2
rest=fact_rec(number)
print("The factorial of {} is {}.format(num,rec)")
              