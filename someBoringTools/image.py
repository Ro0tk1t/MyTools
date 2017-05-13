#! /usr/bin/python3
# -*- coding:utf-8 -*-
from PIL import Image
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--path',help='shshhshh')
#parser.add_argument("output",help="输出保存为")
args = parser.parse_args()
def getimage(imgPath):
    img = Image.open(imgPath)
    im = img.convert("L")
    im = im.resize((330,140),Image.NEAREST)
    imsize = im.size
    x,y = 0,0
    charconnect = ''
    for y in range(imsize[1]):
        for x in range(imsize[0]):
            pix = im.getpixel((x,y))
            getgrey = int(pix/16)
            if getgrey in range(16):
                tochar = ASCII_char(getgrey)
                charconnect = charconnect+tochar
        charconnect+='\n'
    print(charconnect)

def ASCII_char(getgrey):
    chars = ['#','$','%','S','Y','C','=','*','+',';','l','|','^','-',',','.']
    if getgrey in range(16):
        regrey = chars[getgrey]
    return regrey
       
'''def newimage(cc):
    rowout = cc
    return rowout
    '''
getimage(args.path)
