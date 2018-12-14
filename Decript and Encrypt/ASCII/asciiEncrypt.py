#! /usr/bin/python3
print("Please input character that you wanna encrypt:")
a = input()
print('\n********')
print('Encrypt result is:\n[+] ', end='')
for x in a:
    print(ord(x), end=' ')
print('\n********\n')
