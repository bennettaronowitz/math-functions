from itertools import permutations
from sys import argv

def print_word_permutations(word):
	ugly_perms = list(permutations(word))
	for perm in ugly_perms:
		print("".join(perm))
		
print_word_permutations(argv[1])
