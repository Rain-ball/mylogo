#Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
import turtle
z = "1"
while z != "exit":
	z = input(">>> ")
	x = float()
	if z == "fd":
		x = float(input(">>> fd "))
		turtle.forward(x)
	elif z == "bk":
		x = float(input(">>> bk "))
		turtle.back(x)
	elif z == "lt":
		x = float(input(">>> lt "))
		turtle.left(x)
	elif z == "rt":
		x = float(input(">>> rt "))
		turtle.right(x)
	elif z == "circle":
		x = float(input(">>> circle "))
		turtle.circle(x)
	#elif z == "penup":
		#turtle.penUp()
	#elif z == "pendown":
		#turtle.pendown()
	elif z == "dot":
		turtle.dot()
	elif z == "shapeturtle":
		y = str(input(">>> shapeturtle "))
		turtle.shape(y)
	elif z == "//":
		q = input("// ")
	elif z == "exit":
		c = int(input(">>> return "))
		input("Program ended with exit code" + c + ". Press enter to exit...")
	else:
		print("Wrong command!")
