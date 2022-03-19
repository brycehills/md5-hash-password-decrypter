import sys,numpy
import hashlib  # library to implement md5
import binascii # for hex conversion
import time
from itertools import product
from string import ascii_lowercase

def initialization(pw, salt, magic):
	alt = pw + salt + pw
	res = pw + magic + salt
	
	h = hashlib.md5(alt).digest()
	
	l = len(pw)	# get len(pw) -- should be 6 in our case
	
	while l > 0: #concat h to res for len(l)
		res = res + h[0:min(16,l)]
		l = l - 16

	l = len(pw) #reset l
	# For each bit in length(password), from low to high bits
	while l:
		if l & 1:
			res += b'\x00' # append null chr
		else:
			res += pw[0:1] # append first byte of pw
		l>>= 1 				#shiftleft

	hashedres = hashlib.md5(res).digest() # hash concatenated version of res
	
	return hashedres
	
def loop(hashedres,pw,salt):
	for i in range(1000):
		tmp = b"" 					# tmp str
		if i&1: tmp += pw
		else: tmp += hashedres # should this be hashed version or regular string?
		
		if i%3: tmp += salt
		
		if i%7: tmp += pw
	
		if i&1: tmp += hashedres
		else: tmp += pw
		
		hashedres = hashlib.md5(tmp).digest()
		
	return hashedres
	
#@jit		
def reorder(pw,salt,magic,finalsum):
	tmp = b""
	order = [11, 4, 10, 5, 3, 9, 15, 2, 8, 14, 1, 7, 13, 0, 6, 12]
	for i in order: #reorder finalsum
		tmp += finalsum[i:i+1]	
	return tmp

#@njit(parallel = True)
def to64(v):
	tmp = ""
	for i in range(22):
		tmp += base64[v&0x3f]
		v>>=6
	return tmp

	
#define input variables
guesses = 0
start_time = time.clock()

magic = b'$1$'
pw = b'\x7a\x68\x67\x6e\x6e\x64'
samplesalt = b'\x68\x66\x54\x37\x6a\x70\x32\x71'
salt = b'4fTgjp6q'
res = b''
base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#comp string for final hash
shadowHash = "$1$4fTgjp6q$RhNhei1Mem7zJ9xTv1HSc/"
alphabet = ['w','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','a','x','y','z']
alphabet2 = ['w','z','y','x','a','v','u','t','s','r','q','p','m','n','o','l','k','j','i','h','g','f','e','d','c','b']
alphabet3 = ['n','r','y','x','h','v','u','t','s','z','q','p','m','w','o','l','k','j','i','a','g','f','e','d','c','b']
alphabet4 = ['o','r','m','d','h','v','y','t','s','z','q','p','u','w','n','l','k','j','i','a','g','f','e','x','c','b']
alphabet5 = ['q','g','m','d','h','v','y','t','s','z','o','p','u','w','n','l','k','j','i','a','r','f','e','x','c','b']
alphabet6 = ['c','q','t','b','h','v','y','d','s','z','l','p','u','w','n','r','o','j','i','a','g','f','e','x','c','m']

while("$1$" + "4fTgjp6q" + "$" + str(res) != shadowHash):
	for a in alphabet6:
		for b in alphabet6:
			for c in alphabet6:
				for d in alphabet6:
					for e in alphabet6:
						for f in alphabet6:
							password = str(a+b+c+d+e+f)
							print("guessing: " + str(password))
							password = password.encode()
							res = initialization(password,salt,magic)
							res = loop(res,password,salt)
							res = reorder(password,salt,magic,res)
							res = int(binascii.hexlify(res),16) #convert res to int for encoding
							res = to64(res)
							guesses+=1 #increment # of passwords guessed
							if("$1$4fTgjp6q$" + str(res) == shadowHash):
								print("$1$" + "4fTgjp6q$" + str(res) + " is equal to " + shadowHash)
								print("\nThe password is: " + str(password))
								print("# of guesses: " + str(guesses))
								totalTime =  (time.clock() - start_time)
								print("Throughput = " + str(guesses/totalTime) + " guesses per second")
								sys.exit()
							else:
								print("$1$" + "4fTgjp6q$" + str(res) + " is NOT equal to " + shadowHash)




	
	