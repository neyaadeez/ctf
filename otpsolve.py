from pwn import *
import binascii

conn = remote('mercury.picoctf.net', 20266)
conn.recvline()
conn.recvline()
key = conn.recvline().strip()

conn.recvuntil('?')
conn.sendline('X'*(50000-32))
conn.recvuntil('?')
conn.sendline('X'*32)
conn.recvline()
padval = conn.recvline().strip()
gpadval = binascii.unhexlify(padval)
print(gpadval)

message = 'A'*32
kk = []
for i in range(len(gpadval)):
    kk.append(ord(message[i])^gpadval[i])

key1 = binascii.unhexlify(key)
flag = []
for i in range(32):
    flag.append(chr(kk[i]^key1[i]))
flag = ''.join(flag)
print(flag)
conn.close()