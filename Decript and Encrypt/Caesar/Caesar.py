#! /usr/bin/python3

from string import ascii_lowercase as lower
from string import ascii_uppercase as upper

import argparse 

pars = argparse.ArgumentParser()
pars.add_argument('-k',help='移位数')
pars.add_argument('-s',help='待加解密字符串')
parsers = pars.parse_args()


def decrypt(k, s):
	result = ''
	for strLen in range(len(s)):
		c = s[strLen]
		#result += c.islower()?lower[key+Input.index(c)]:(c.isupper()?upper[key+Input.index[c]]:c)
	    	#好吧，py里面没有三目运算符。。。
		result += lower[(int(k)+lower.index(c))%26] if c.islower() else (upper[(int(k)+upper.index(c))%26] if c.isupper() else c)
	print('[+]  key= %s  result= %s'%(k,result))
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
