#! /usr/bin/python3
Dict = {'-': 45, 'R': 82, '6': 54, 'h': 104, ';': 59, 'E': 69, 'G': 71, '#': 35, 'g': 103, '{': 123, '@': 64, '1': 49, 'a': 97, '<': 60, '=': 61, 'U': 85, '9': 57, '2': 50, 'w': 119, 'I': 73, 'i': 105, '|': 124, 'c': 99, 'u': 117, '/': 47, '5': 53, 'B': 66, 'b': 98, '>': 62, 'N': 78, 'x': 120, '_': 95, 'f': 102, '&': 38, '!': 33, '.': 46, '8': 56, 'O': 79, 'M': 77, 'X': 88, '`': 96, 'l': 108, 'd': 100, 'D': 68, '*': 42, ' ': 32, 'P': 80, '0': 48, 'e': 101, 'j': 106, 'J': 74, 'Q': 81, '~': 126, 'Z': 90, '%': 37, '4': 52, 'n': 110, '+': 43, '"': 34, '7': 55, 'm': 109, 'S': 83, 'F': 70, '3': 51, "'": 39, 'W': 87, '}': 125, 'C': 67, 'o': 111, '\\': 92, 'z': 122, 't': 116, '(': 40, '^': 94, 'y': 121, 'Y': 89, '$': 36, 'H': 72, 'A': 65, ']': 93, 'k': 107, ',': 44, 'T': 84, 's': 115, 'q': 113, ':': 58, 'V': 86, '[': 91, 'L': 76, 'p': 112, '?': 63, 'r': 114, 'K': 75, 'v': 118, ')': 41}
print("Please input character that you wanna encrypt:")
a = input()
print('\n********')
print('Encrypt result is:\n[+] ',end='')
for x in range(len(a)):
    print(Dict[a[x]],end='')
    print(' ',end='')
print('\n********\n')