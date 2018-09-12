score = int(input('请输入学生成绩：'))
if 90 <= score < 100:
        print("A")
if 80 <= score < 90:
        print("B")
if 60 <= score < 80:
        print("C")
if 0 <= score <= 60:
        print("D")
if 100 < score or score < 0:
        print("输入错误")
