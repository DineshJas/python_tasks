def func():
	a = int(input("enter a number : "))
	if a > 0:
		aa = a % 2
		if aa == 0:
			print("even")
		else:
			print("odd")
	else:
		print("invalid")
	
func()
