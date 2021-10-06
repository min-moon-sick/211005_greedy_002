
s = '0001100'
# s = '111001100' # len = 9
s = list(s)
print(s)
cnt = 0

pibot = s[0]

for i in range(1, len(s)):

  if s[i] != pibot:
    idx = i

    while s[i] != pibot and i <len(s)-1:
      i += 1

    cnt += 1
    
    if i == len(s)-1:
      s[idx:i] = pibot * (i  - idx)
      s[i] = pibot
    else:
      s[idx:i] = pibot * (i  - idx)



 
print(cnt)
