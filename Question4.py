# 4.	Check whether string is a palindrome or not.
# 	(A palindrome is a string that reads the same forwards and backwards.)


def palindrome(s1):
	if s1==s1[::-1]:
		print("String is a palindrome")
	else:
		print("String is not a palindrome")

palindrome("aaabaaa")     # check for palindrome
palindrome("abababaa")    # check for not a palindrome