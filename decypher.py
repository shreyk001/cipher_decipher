def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
	
	
def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
	
f=open("message.txt","r")
string=f.read()
keyword = "SHREY"
key = generateKey(string, keyword)
f1=open("message.txt","w")
decypher=originalText(string, key)
f1.write(decypher)
f1.close()
