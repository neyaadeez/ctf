import string

LOWER_OFFSET = ord('a')
Alph = string.ascii_lowercase[:16]
bkey = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"
keyin = ''

def shift(c, k):
	t1 = ord(c) - LOWER_OFFSET
	t2 = ord(k) - LOWER_OFFSET
	return Alph[(t1 - t2) % len(Alph)]

def b16_decode(cipher):
    dec = ""
    # loop through the cipher 2 characters at a time
    for c in range(0, len(cipher), 2):
        # turn the two characters into one binary string
        b = ""
        b += "{0:b}".format(Alph.index(cipher[c])).zfill(4)
        b += "{0:b}".format(Alph.index(cipher[c+1])).zfill(4)
        # turn the binary string to a character and add
        dec += chr(int(b,2))
    
    return dec

for ll in Alph:
	keyin = ll
	reunshift= ""
	for i, c in enumerate(bkey):
		reunshift += shift(c, keyin[i % len(keyin)])
	res = b16_decode(reunshift)
	print(res)
	


	
	