Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> if type(a) == int:
	print("GG!")
elif type(a) == float:
	print("Still counts..")
else:
	print("YOU SUCK!")

	
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    if type(a) == int:
NameError: name 'a' is not defined
>>> a=10
>>> if type(a) == int:
	print("GG!")
elif type(a) == float:
	print("Still counts..")
else:
	print("YOU SUCK!")

	
GG!
>>> 2.3
2.3
>>> a=2.3
>>> if type(a) == int:
	print("GG!")
elif type(a) == float:
	print("Still counts..")
else:
	print("YOU SUCK!")

	
Still counts..
>>> a = d
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a = d
NameError: name 'd' is not defined
>>> a = "d"
>>> if type(a) == int:
	print("GG!")
elif type(a) == float:
	print("Still counts..")
else:
	print("YOU SUCK!")

	
YOU SUCK!
>>> if type(a) == int:
	print("GG!")
elif type(a) == float:
	print("Still counts..")
elif type(a) == int:
	print("chill out..")
else:
	print("YOU SUCK!")

	
YOU SUCK!
>>> a=10
>>> if type(a) == int:
	print("GG!")
elif type(a) == float:
	print("Still counts..")
elif type(a) == int:
	print("chill out..")
else:
	print("YOU SUCK!")

	
GG!
>>> if type(a) == int:
	print("GG!")
elif type(a) == float:
	print("Still counts..")
elif type(a) == int:
	print("chill out.. - šo tekstu neviens nekad neredzēs :D")
else:
	print("YOU SUCK!")

	
GG!
>>> print("aaa\n bbb\n")
aaa
 bbb

>>> print("aaa\t bbb\t")
aaa	 bbb	
>>> print("aaa\t bbb\c")
aaa	 bbb\c
>>> print("aaa\t bbb\v")
aaa	 bbb
>>> print("aaa\t 111\nbbb\v")
aaa	 111
bbb
>>> 
