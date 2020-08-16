Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> print(letter[3])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(letter[3])
IndexError: string index out of range
>>> print(letter = fruit[3])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(letter = fruit[3])
TypeError: 'letter' is an invalid keyword argument for this function
>>> fruit[5]
'a'
>>> fruit[3]
'a'
>>> fruit[2]
'n'
>>> fruit[2]+[8]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fruit[2]+[8]
TypeError: must be str, not list
>>> fruit[1]+fruit[3]+fruit[5]
'aaa'
>>> N = len(fruit)
>>> n
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> N
6
>>> length = len(fruit)
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> number = []
>>> len(numbers)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    len(numbers)
NameError: name 'numbers' is not defined
>>> len(number)
0
>>> numbers.append(1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    numbers.append(1)
NameError: name 'numbers' is not defined
>>> number.append(1)
>>> len(number)
1
>>> number.append(55)
>>> len(number)
2
>>> number
[1, 55]
>>> vardi = ['a', 'ab', 'abc']
>>> vardi
['a', 'ab', 'abc']
>>> vardu_garumi = []
>>> vardu_garumi.append(len(vardi[0]))
>>> vardu_garumi.append(len(vardi[1]))
>>> vardu_garumi.append(len(vardi[2]))
>>> vardu_garumi
[1, 2, 3]
>>> print(last)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(last)
NameError: name 'last' is not defined
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> length = len(fruit)
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> len(fruit)
6
>>> last = fruit[length-1]
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> print(last)
a
>>> type(vardi)
<class 'list'>
>>> vardi = ['a', 'ab', 'abc', '10']
>>> type(vardi)
<class 'list'>
>>> fruit
'banana'
>>> len(fruit)
6
>>> fruit[0]
'b'
>>> fruit[1]
'a'
>>> fruit[2]
'n'
>>> fruit[3]
'a'
>>> fruit[4]
'n'
>>> fruit[5]
'a'
>>> fruit[len(fruit)-1]
'a'
>>> fruit=abcdef
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    fruit=abcdef
NameError: name 'abcdef' is not defined
>>> fruit= "abcdef"
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> fruit[length]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    fruit[length]
IndexError: string index out of range
>>> fruit[length-1]
'f'
>>> index = 5
>>> index = 6-1
>>> while index >= len(fruit):
	letter = fruit[index]
	print(letter)
	index = index +1

	
>>> while index >= len(fruit):
	letter = fruit[index]
	print(letter)
	index = index -1

	
>>> 1
1
>>> while len(fruit) < 0:
	letter = fruit[index]
	print(letter)
	index = index +1

	
>>> while index >= 0:
	letter = fruit[index]
	print(letter)
	index = index -1

	
f
e
d
c
b
a
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index +1

	
f
a
b
c
d
e
f
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index +1

	
a
b
c
d
e
f
>>> 
