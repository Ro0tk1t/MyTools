#! /usr/bin/python3
print('[+] please input ASCIInumber: ')

Input = input().strip()

print('[+] ASCII decrypt result is:   ',end='')
try:
    if ' ' in Input:
        inputHandle = Input.split(' ')
        for x in inputHandle:
            print(chr(int(x)),end='')
    elif '  ' in Input:
        inputHandle = Input.split('  ')
        for x in inputHandle:
            print(chr(int(x)),end='')
    elif ',' in Input:
        inputHandle = Input.split(', ')
        for x in inputHandle:
            print(chr(int(x)),end='')
    elif '，' in Input:
        inputHandle = Input.split('，')
        for x in inputHandle:
            print(chr(int(x)),end='')
    elif ':' in Input:
        inputHandle = Input.split(':')
        for x in inputHandle:
            print(chr(int(x)),end='')
    elif '\\' in Input:
        inputHandle = Input.split('\\')
        for x in inputHandle:
            print(chr(int(x)),end='')
    print()
except:
    print()
