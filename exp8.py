while True:
	print("1-Check the File Not Found \n")
	print("2=Check for VAlue Error \n")
	print("3=Check Type Error \n")
	print("4=Type Error \n")
	print("5=Check the Name Error \n")
	print("0=Exit \n")
	n=int(input("Enter your Choice"))
	if n==1:
		try:
			file1 = open("database.py")
			print(file1.read())
			file1.close
		except FileNotFoundError:
			print("\n \n \nFile Not Found \n")
	elif n==2:
                try:
                        file1 = open("open.py",'z')
                        print(file1.read())
                        file1.close
                except ValueError:
                        print("Value Not Found \n")
	elif n==3:
                try:
                        file1 = open("ab.py","r","w")
                        print(file1.read())
                        file1.close
                except TypeError:
                        print("type error in the file")
	elif n==4:
                try:
                        file1 = open("ab.py","r")
                        print(file1.read())
                        file1.close
                except IOError:
                        print("There is An IO Error\n")
	elif n==5:
                try:
                        file1 = open("abc.py","r")
                        print(file1.read())
                        file1.close
                except NameError:
                        print("Name Error In file \n")
	elif n==0:
		print("not valid input")
		break

