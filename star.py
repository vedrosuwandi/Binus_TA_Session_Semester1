# Triangle
length = input("insert length :")
length = int(length)
x = 1
while x <= length:
    print ("*" * x)
    x = x + 1

# Triangle#2
length = input("insert length :")
length = int(length)
x = 1
while x <= length:
    print("*" * (length - x + 1))
    x = x + 1
    y=0

# Triangle#3
length = input("insert length :")
length = int(length)
x = 1
while x <= length:
    print(" " * (length - x), "*" * x)
    x = x + 1

# Triangle#4
length = input("insert length :")
length = int(length)
x = 1
while x <= length:
    print(" " * (x - 1), "*" * (length - x + 1))
    x = x + 1

# 3 same size
length = input("insert length :")
length = int(length)
x = 1
while x <= length :
    print(" " * (length - x), "* " * x )
    x = x + 2


#Reversed 3 same size
length = input("insert length :")
length = int(length)
x = 1
while x <= length:
    print(" " * x , "* " * (length - x + 1))
    x = x + 2

# making diamond
length = input("insert length :")
length = int(length)
x = 1
while x <= length:
    print(" " * (length - x), "* " * x)
    x = x + 1
x = 1
while x <= length :
    print(" " * (x - 1 + 1), "* " * (length - x ))
    x = x + 1


