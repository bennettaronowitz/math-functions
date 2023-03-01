from sys import argv

RED = "\033[91m"
GREEN ="\033[92m"
BLUE = "\033[94m"

def reverse_string(word):
	reversed = ""
	for index in range(1, len(word) + 1):
		reversed += word[-index]
	return reversed
	
print(f"{GREEN}THE REVERSED VERSION OF {RED}{argv[1]} {GREEN}IS {BLUE}{reverse_string(argv[1])}")
