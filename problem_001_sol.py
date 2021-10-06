
# n = int(input())

x = [3, 3, 1, 2, 2]

x = sorted(x)

cnt = 0

print(x)


x_i = len(x)
print(x_i)

while x_i > 0:

  # value
  x_v = x[x_i - 1]

  # index
  x_i = x_i - x_v

  cnt += 1

print("cnt : ", cnt)
