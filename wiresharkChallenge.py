word = 'cvpbpgsc33xno00_1_f33_h_qrnqorrs'
res = []
for ch in word:
    num = ord(ch) - ord('a')
    num += 13
    num = num % 26
    res.append(chr(num + ord('a')))
print(''.join(res))