#! /usr/bin/python3

def decrypt(Str, x, Len):
	tmp = ''
	if(Len%x == 0):
		L1 = int(Len/x)
		for z in range(x):
			for y in range(0,L1):
				tmp += Str[x * y + z]
				#print(x,y,tmp)
	return tmp

print('Please input what you wanna decrypt:')
Input = input()
Len = len(Input)
result = ''
print('**************\n\nResults is :')
for x in range(2,Len):		#因子
	if(Len%x == 0):
		result = decrypt(Input, x, Len)
		print('[+] key=%s   result= %s'%(x,result))
print('\n**************')
