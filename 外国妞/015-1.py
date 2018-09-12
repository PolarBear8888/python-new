Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '{0} love {1}.{2}'.format('I
			      
SyntaxError: EOL while scanning string literal
>>> '{0} love {1}.{2}'.format('I','fish','com')
			      
'I love fish.com'
>>> '{a} love {b}.{c}'.format(a='I',b='fish',c='com')
			      
'I love fish.com'
>>> '{0} love {a}.{b}'.format('I',a='fish',b='com')
			      
'I love fish.com'
>>> '{a} love {b}.{0}'.format( a='I',b='fish',0='com')
			      
SyntaxError: keyword can't be an expression
>>> '{a} love {b}{c}'.format( a='I',b='fish',c='.com')
			      
'I love fish.com'
>>> '{a} love {b}{c}'.format( 'I','fish','.com')
			      
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    '{a} love {b}{c}'.format( 'I','fish','.com')
KeyError: 'a'
>>> print('\ta')
			      
	a
>>> 
			      
>>> 
			      
>>> 
			      
>>> print('\\')
			      
\
>>> '{{0}}'.format('I')
			      
'{0}'
>>> print(I)
			      
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(I)
NameError: name 'I' is not defined
>>> print('I')
			      
I
>>> print({0})
			      
{0}
>>> '{0;.1f}{1}'.format(27.658,'GB')
			      
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    '{0;.1f}{1}'.format(27.658,'GB')
KeyError: '0;'
>>> '{0:.1f}{1}'.format(27.658,'GB')
			      
'27.7GB'
>>> '%d + %d = %d'%(4,5,9)
			      
'4 + 5 = 9'
>>> '%x'% 29
			      
'1d'
>>> '%f'%25.6666
			      
'25.666600'
>>> '%#x'%10
			      
'0xa'
>>> '%#o'%10
			      
'0o12'
>>> print(\ta)
			      
SyntaxError: unexpected character after line continuation character
>>> print('\ta')
			      
	a
>>> 
