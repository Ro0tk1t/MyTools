#! /usr/bin/python3

import argparse 
pars = argparse.ArgumentParser()
pars.add_argument('-k',help='移位数')
pars.add_argument('-s',help='待加解密字符串')
parsers = pars.parse_args()
L_letter = 'abcdefghijklmnopqrstuvwxyz'
U_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
Input = ''

def decrypt(k, s):
	global result
	for strLen in range(len(s)):
		c = s[strLen]
			#result += c.islower()?L_letter[key+Input.index(c)]:(c.isupper()?U_letter[key+Input.index[c]]:c)
			#好吧，py里面没有三目运算符。。。
		result += L_letter[(int(k)+L_letter.index(c))%26] if c.islower() else (U_letter[(int(k)+U_letter.index(c))%26] if c.isupper() else c)
	print('[+]  key= %s  result= %s'%(k,result))
	result = ''
	return result

if (parsers.k == None):
	print('plaese input what you wanna encrypt or decrypt:')
	Input = input()
	print('*************\n\nAll results are : ')
	for key in range(1,26):
		decrypt(key,Input)

else:
	print('*************\n\nAll results are : ')
	decrypt(parsers.k, parsers.s)

print('\n*************')
