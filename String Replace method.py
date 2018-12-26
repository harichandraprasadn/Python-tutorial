# String Replace method

a = "I Like Hari"
b = a.replace('Like','Love')
print(b)

#Changing upper or Lower case strings
a = "I Like Hari"
print(a.upper())
print(a.lower())

a = "i like hari"
print(a.capitalize())

#Using Join function for the string
print(":".join("Python"))

#reversing string
String='Chanda'
print(''.join(reversed(String)))

#Split strings
string = "Hari Chandra Prasad"
print(string.split(' '))

#Strings are Immutable
x = "Guru99"
x = x.replace("Guru99","Python")
print(x)
