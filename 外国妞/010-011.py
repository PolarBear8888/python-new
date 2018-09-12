Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mix = ['小甲鱼',3.0,4,[1,2,3]]
>>> mix
['小甲鱼', 3.0, 4, [1, 2, 3]]
>>> mix.append('福禄娃娃')
>>> mix
['小甲鱼', 3.0, 4, [1, 2, 3], '福禄娃娃']
>>> len(mix)
5
>>> mix.append('哇','方法')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    mix.append('哇','方法')
TypeError: append() takes exactly one argument (2 given)
>>> mix.extend(['竹林小溪'])
>>> mix.extend(['竹林小溪','百事可乐'])
>>> mix
['小甲鱼', 3.0, 4, [1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪', '百事可乐']
>>> mix.insert(0,'哇咔咔')
>>> mix
['哇咔咔', '小甲鱼', 3.0, 4, [1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪', '百事可乐']
>>> mix[3]
4
>>> mix[1]
'小甲鱼'
>>> temp = mix(0)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    temp = mix(0)
TypeError: 'list' object is not callable
>>> temp = mix[0]
>>> mix[0] = mix[1]
>>> mix[1] = temp
>>> mix[0]
'小甲鱼'
>>> mix
['小甲鱼', '哇咔咔', 3.0, 4, [1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪', '百事可乐']
>>>  mix.remove('哇咔咔')
SyntaxError: unexpected indent
>>> mix.remove('哇咔咔')
>>> mix
['小甲鱼', 3.0, 4, [1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪', '百事可乐']
>>> del mix[0]
>>> mix
[3.0, 4, [1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪', '百事可乐']
>>> mix.pop(0)
3.0
>>> name = mix.pop(0)
>>> mix
[[1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪', '百事可乐']
>>> name
4
>>> mix.pop()
'百事可乐'
>>> mix[1:3}
SyntaxError: invalid syntax
>>> mix[1:3]
['福禄娃娃', '竹林小溪']
>>> mix
[[1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪']
>>> mix[0]
[1, 2, 3]
>>> mix[:1]
[[1, 2, 3]]
>>> mix[2:]
['竹林小溪', '竹林小溪']
>>> mix
[[1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪']
>>> mix[:]
[[1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪']
>>> mix2 = mix[:]
>>> mix2
[[1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪']
>>> mix.pop()
'竹林小溪'
>>> mix
[[1, 2, 3], '福禄娃娃', '竹林小溪']
>>> mix2
[[1, 2, 3], '福禄娃娃', '竹林小溪', '竹林小溪']
>>> mix[:]
[[1, 2, 3], '福禄娃娃', '竹林小溪']
>>> 
