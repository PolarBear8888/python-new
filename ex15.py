from sys import argv
#调用库
script, filename = argv
#解包 依次赋给左边的变量
txt = open(filename)
#open接受一个参数，返回一个文件（有着你给他的命令）
print(f"Here's your file {filename}:")
print(txt.read())
#用（.)接受文件 无需参数
txt.close()
print('Type the filename again:')
file_again = input("> ")
#输入名称
txt_again = open(file_again)
#打开
print(txt_again.read())
#读取
txt_again.close()