a=100
print(a)


# Declare a Variable and initialize it
f = 0
print(f)
# Re-Declaring the Variable works
f = 'Main guru'
print(f)

# Concatenate Variables

a="Hari"
b=99
print(a+str(b))

# Local & Global Variables
# Declare a Variable and initialize it
f=101
print(f)

# Global Vs Local variables in functions
def ExampleFunction():
    f = 'I am Learning Python'
    print(f)
ExampleFunction()
print(f)


# Declaring Global keyword inside the function
f = 101
print(f)
# Global vs.local variables in functions
def someFunction():
  global f
print(f)
f = "changing global variable"
someFunction()
print(f)

# Deleting a Variable
f=11
print(f)

del f
print(f)
