msb = 4 * 10**1
lsb = 2 * 10**0
print(msb)
print(lsb)

number = 42
ans = ''
while number != 0 and number != 1:
    ans = str((number%2)) + ans
    number = (int)(number/2)
    print(number)
if number == 1:
    ans = '1'+ans
print(ans)