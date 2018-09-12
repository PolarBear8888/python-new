Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1 = [123]
>>> list2 = [234]
>>> list1>list2
False
>>> list2>list1
True
>>> list1= [123,567]
>>> list2= [234,567]
>>> list1>list2
False
>>> list2>list1
True
>>> list3 =list2 + list1
>>> list3
[234, 567, 123, 567]
>>> list3 *3
[234, 567, 123, 567, 234, 567, 123, 567, 234, 567, 123, 567]
>>> 234 in list3
True
>>> '111' not in list
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    '111' not in list
TypeError: argument of type 'type' is not iterable
>>> '111' not in list3
True
>>> list4 = [123,['小甲鱼'],456]
>>> '小甲鱼' in list4
False
>>> '小甲鱼' in list1
False
>>> '小甲鱼' in list4[1]
True
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> list1.count(123)
1
>>> list3.index(234)
0
>>> list3.index(567)
1
>>> list3.index(234,2,6)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list3.index(234,2,6)
ValueError: 234 is not in list
>>> list3*=3
>>> list3
[234, 567, 123, 567, 234, 567, 123, 567, 234, 567, 123, 567]
>>> list3.index(234,2,5)
4
>>> list3.index(234,2,4)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list3.index(234,2,4)
ValueError: 234 is not in list
>>> list3.reverse
<built-in method reverse of list object at 0x020E9670>
>>> list3.reverse()
>>> list3
[567, 123, 567, 234, 567, 123, 567, 234, 567, 123, 567, 234]
>>> list3.sort()
>>> list3
[123, 123, 123, 234, 234, 234, 567, 567, 567, 567, 567, 567]
>>> sort(func,key)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    sort(func,key)
NameError: name 'sort' is not defined
>>> list3.sort(reverse=Ture)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list3.sort(reverse=Ture)
NameError: name 'Ture' is not defined
>>> list3.sort(reverse=True)
>>> list3
[567, 567, 567, 567, 567, 567, 234, 234, 234, 123, 123, 123]
>>> 
