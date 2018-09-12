from sys import  argv

script, input_file = argv

def print_all(f):
    print(f.read())
#读取文件
def rewind(f):
    f.seek(0)
#转到文件的什么位置
def print_a_line(line_count, f):
    print(line_count, f.readline())
#用于文件读取整行
current_file = open(input_file)
#打开文件 
print("First let's print the whole file:\n")

print_all(current_file)
#运行函数
print("Now let's rewind, kind of like a tape.")

rewind(current_file)
#运行函数
print("Let's print three lines:")

current_line = 1
print(current_line)
print_a_line(current_line, current_file)

current_line  += 1
print(current_line)
print_a_line(current_line, current_file)

current_line += 1
print(current_line)
print_a_line(current_line, current_file)