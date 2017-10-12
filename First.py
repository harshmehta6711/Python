one = 1
two = 4
print(one)
print("The first variable")

myint = 10
mystring = "hello"
myfloat = float(12)
if isinstance(myint, int):
    print("The number is int, %d" % myint)
if isinstance(myfloat, float):
    print("The number is float, %f" % myfloat)
if mystring == "hello":
    print("The string is %s" % mystring)
newstr = "Python Programming"
print(newstr[1])
print("Limiting the string ", newstr[6:9])  # First character is not included
print("updating the string ", "Python" + newstr[4:])
print(newstr)
print(newstr * 5)

sum = lambda arg1, arg2: arg1 + arg2

print("THe sum is : %d" % sum(106542383, 544345))
