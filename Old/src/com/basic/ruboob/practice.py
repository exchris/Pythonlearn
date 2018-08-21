def jiechen(n):
  result = 1
  for i in range(1, n+1):
    result = result * i
  return(result)

input = input()
n = int(input)
odd ,even = 0, 0
for j in range(1, n+1):
    if (j%2==0) :
        odd = odd + jiechen(j)
    else :
        even = even + jiechen(j)
print('%s %s' %(even, odd))