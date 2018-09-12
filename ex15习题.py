from sys import argv

stript, filename = argv

print("Here's your file ")

filename = input('> ')

txt = open(filename)
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())