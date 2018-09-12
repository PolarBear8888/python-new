from sys import argv

script, filename = argv
txt = open(filename,'w+')

line1 = input()
line2 = input()
line3 = input()
txt.write(line1 + '\n'+ line2 +'\n' + line3) 
txt.close()
txt1 = open("C://python练习//ex15_sample.txt")
#关闭文件 之后只能输入系统路径打开
print(txt1.read())