from itertools import permutations
from sys import argv

def print_word_permutations(word):
	ugly_perms = list(permutations(word))
	for perm in ugly_perms:
		print("".join(perm))
		
def get_permutations(word):
	perm_storage = []
	for char in word:
		for letter in word[1:3]:
			perm = char + letter
			for letter2 in word[2:3]:
				perm += letter2
				perm_storage.append(perm)
	print(perm_storage)
	

get_permutations("cat")
#print_word_permutations(argv[1])
