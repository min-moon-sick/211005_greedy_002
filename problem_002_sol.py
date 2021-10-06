
x = input()

x = list(x)

x = [int(i) for i in x]
print(x)

result = x[0]

for i in range(0, len(x)-1):
  if x[i] != 0:
    result = result * x[i+1]
    print("1 result : ", result)
  else:
    result = result + x[i+1]
    print("2 result : ", result)

print(result)

