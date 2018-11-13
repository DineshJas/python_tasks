def func():
	a = int(input("enter the 1st value"))
	b = int(input("enter the 2nd value"))
	c = int(input("enter the 3rd value"))
	if (a >= b) and (a >= c):
	    print(f"{a} is greatest")
	elif (b >= a) and (b >= c):
	    print(f"{b} is greatest")
	else:
		print(f"greatest value is {c}")

func()
