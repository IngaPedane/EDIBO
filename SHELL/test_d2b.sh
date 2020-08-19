#!/bin/bash
printf "Ievadiet skaitli: "; read a
#echo  $a
re='^[0-9]+$'
until [[ $a =~ $re ]]
do
  printf "error: Not a number "; read a
done
b=$a
#echo "please, enter a number: "; read $2
#fi

array=()

while [ $a != 0 ]
do
array+=$(($a%2))
a=$(($a/2))
done 

c=$(echo "${array[*]}" | rev)
echo "Binārā vērtība skaitlim $b ir:" $c


