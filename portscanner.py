import os 

print("Network port scanner")

ip = input(str("Enter The Ip / Website you wana scan [ ports ] : -> "))

x = input(str("wanted fast port scan? (press y for yes and n for no :-> ")).lower()

if x == "y":
	a = os.system("rustscan " + ip )

	print(a)

b = input(str("wana do nmap scan also?  (press y for yes or n for no :-> ")).lower()

if b == "y":
	d = os.system("nmap -sC -sV " +  ip)
	print(d)
