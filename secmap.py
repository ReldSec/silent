#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket
import sys
import argparse
from colorama import Fore
import platform
import os
import time
import requests
from os import path

parse = argparse.ArgumentParser()
parse.add_argument('-t','--target',help='target')
parse.add_argument('-s','--seconds',help='seconds sleep',default=0.3,type=int)
parse.add_argument('-o','--output',help='save')
argsv = parse.parse_args()

def slowprint(cad):
	for c in cad + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(.1)

class colors:
	blue = Fore.LIGHTBLUE_EX
	green = Fore.LIGHTGREEN_EX
	red = Fore.LIGHTRED_EX
	yellow = Fore.LIGHTYELLOW_EX
	white = Fore.LIGHTWHITE_EX
	black = Fore.BLACK


ports = [21, 22, 23, 25, 66, 79, 80, 107, 110, 118, 119, 137, 138, 139, 150, 161, 194, 209, 217, 389, 407, 443, 445, 515, 522, 531, 992, 993, 995, 1417, 1420, 1547, 3000, 3128, 3389, 4099, 5190, 5500, 5631, 5632, 5800, 5900, 6346, 6891, 6900, 6901, 20000, 28800, 29000]

def save_ports(lista,file_save):
	if path.exists(file_save):
		print('[{}!{}] {}Exists File'.format(colors.red,colors.white,colors.red))
		sys.exit(1)
	else:
		if len(lista) > 0:
			if file_save.__contains__('.'):
				file = open(file_save+'.txt','w+')
				file.write('======================\n')
				file.write('PORTS SAVE\n')
				file.write('======================\n')
				for n in lista:
					file.write(str(n))
					file.write('\n=====================\n')
				file.close()
				print('\n{}==========================================\n'.format(colors.yellow))
				print('\t{}SAVE => {}'.format(colors.red,file_save))
				print('\n{}==========================================\n'.format(colors.yellow))
			else:
				file = open(file_save+'.txt','w+')
				file.write('======================\n')
				file.write('PORTS SAVE\n')
				file.write('======================\n')
				for n in lista:
					file.write(str(n))
					file.write('\n=====================\n')
				print('\n{}==========================================\n'.format(colors.yellow))
				print('\t{}SAVE => {}.txt'.format(colors.red,file_save))
				print('\n{}==========================================\n'.format(colors.yellow))
				file.close()
		else:
			print('[{}!{}] {}Ports Not Found :('.format(colors.red,colors.white,colors.red))

def scanner(ip):
	list_ports = []
	print('[{}SLEEP{}] {}'.format(colors.green,colors.white,argsv.seconds))
	for p in ports:
		time.sleep(argsv.seconds)
		sc = socket.socket()
		try:
			sc.settimeout(2)
			sc.connect((ip,p))
			print('\n[{}+{}] {}OPEN{} Search Banner In {}...{}\n'.format(colors.red,colors.white,colors.green,colors.red,p,colors.white))
			sc.send(b'a')
			try:
				rb = sc.recv(1024)
				print('\n[{}+{}] {}{}{}'.format(colors.green,colors.white,colors.green,rb,colors.white))
			except socket.timeout:
				print('\n[{}!{}] {}Banner Not Found{}'.format(colors.red,colors.white,colors.red,colors.white))
			list_ports.append(p)
			sc.close()
		except socket.error:
			print('\n[{}!{}] PORT {} {}CLOSED or FILTERED{}'.format(colors.red,colors.white,p,colors.red,colors.white))
		finally:
			sc.close()
	if argsv.output:
		save_ports(list_ports,argsv.output)
	else:
		if len(list_ports) > 0:
			print('\n{}==========================================\n'.format(colors.yellow))
			print('{}\tOPEN PORTS IN {}\n'.format(colors.yellow,ip))
			for l in list_ports:
				print('\t[{}+{}] {} OPEN{}'.format(colors.green,colors.white,l,colors.white))
			print('\n{}==========================================\n'.format(colors.yellow))
		else:
			print('[{}!{}] {}Ports Not Found :('.format(colors.red,colors.white,colors.red))
		sys.exit(1)

def banner():
	print('''

{}   ▄████████  ▄█   ▄█          ▄████████ ███▄▄▄▄       ███     
  ███    ███ ███  ███         ███    ███ ███▀▀▀██▄ ▀█████████▄ 
  ███    █▀  ███▌ ███         ███    █▀  ███   ███    ▀███▀▀██ 
{} ███        ███▌ ███        ▄███▄▄▄     ███   ███     ███   ▀ 
▀███████████ ███▌ ███       ▀▀███▀▀▀     ███   ███     ███     
         ███ ███  ███         ███    █▄  ███   ███     ███     
{}  ▄█    ███ ███  ███▌    ▄   ███    ███ ███   ███     ███     
 ▄████████▀  █▀   █████▄▄██   ██████████  ▀█   █▀     ▄████▀   
                  ▀                                            
{}
 												 \t\t\t\t\t\t\t\n Twitter: @IDX4CKS                                                                    
'''.format(colors.black,colors.red,colors.yellow,colors.green))
	print('{}'.format(colors.white))


def main():
	banner()
	if argsv.target:
		target = argsv.target
		if target.startswith('http://'):
			target = target.replace('http://','')
		elif target.startswith('https://'):
			target = target.replace('http://','')
		else:
			pass
		scanner(target)

if __name__ == '__main__':
	try:
		if len(sys.argv) < 2:
			print('Need Arguments')
			sys.exit()
		else:
			if platform.system() == 'Windows':
				cmd = os.system('cls')
				main()
			elif platform.system() == 'Linux':
				cmd = os.system('reset')
				main()
	except KeyboardInterrupt:
		slowprint('{}Bye Bye ^-^/'.format(colors.red))
		sys.exit()
