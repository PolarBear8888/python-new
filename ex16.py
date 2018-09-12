from sys import argv
#从sys软件包取出argv特性
script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTEL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename,'w')
#'w'表示文件的写入模式
print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#target.write(line1+"\n"+line2+'\n'+line3)
print("And finally, we close it.")
target.close()