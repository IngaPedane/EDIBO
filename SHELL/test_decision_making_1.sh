#!/bin/bash

a=10
b=20

if [ $a == $b ]
then
   echo "a is equal to b"
fi

if [ $a != $b ]
then
   echo "a is not equal to b"
fi


c=10
d=20

if [ $c == $d ]
then
   echo "c is equal to d"
else
   echo "c is not equal to d"
fi

e=10
f=20

if [ $e == $f ]
then
   echo "e is equal to f"
elif [ $e -gt $f ]
then
   echo "e is greater than f"
elif [ $e -lt $f ]
then
   echo "e is less than f"
else
   echo "None of the condition met"
fi

FRUIT="kiwi"

case "$FRUIT" in
   "apple") echo "Apple pie is quite tasty." 
   ;;
   "banana") echo "I like banana nut bread." 
   ;;
   "kiwi") echo "New Zealand is famous for kiwi." 
   ;;
esac

option="${1}" 
case ${option} in 
   -f) FILE="${2}" 
      echo "File name is $FILE"
      ;; 
   -d) DIR="${2}" 
      echo "Dir name is $DIR"
      ;; 
   *)  
      echo "`basename ${0}`:usage: [-f file] | [-d directory]" 
      exit 1 # Command to come out of the program with status 1
      ;; 
esac 
