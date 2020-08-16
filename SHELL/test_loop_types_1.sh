#!/bin/bash

a=0
while [ "$a" -lt 10 ]    # this is loop1
do
   b="$a"
   while [ "$b" -ge 0 ]  # this is loop2
   do
      echo -n "$b "
      b=`expr $b - 1`
   done
   echo
   a=`expr $a + 1`
done
echo "----------------------------------------------------------------"
a=0

while [ $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
echo "----------------------------------------------------------------"
for var in 0 1 2 3 4 5 6 7 8 9
do
   echo $var
done
echo "----------------------------------------------------------------"
for FILE in $HOME/.bash*
do
   echo $FILE
done
echo "----------------------------------------------------------------"
a=0

until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
echo "----------------------------------------------------------------"
select DRINK in tea cofee water juice appe all none
do
   case $DRINK in
      tea|cofee|water|all) 
         echo "Go to canteen"
         ;;
      juice|appe)
         echo "Available at home"
      ;;
      none) 
         break 
      ;;
      *) echo "ERROR: Invalid selection" 
      ;;
   esac
done
