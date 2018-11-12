def func():
	a = (input("enter a letter : "))
	if a.isalpha():
		if a in ['a', 'e', 'i', 'o', 'u']:
			print("it is a vowel")
		else:
			print("it is a consonent")
	else:
		print("invalid")

func()
