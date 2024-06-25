num = 445
res = 0

while num != 0:
    dig = num % 10
    res += dig
    num //= 10

print(res)