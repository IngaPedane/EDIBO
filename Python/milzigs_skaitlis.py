#! /usr/bin/python3.6

print("Ievadiet skaitli")

# a=2**2000000

# te ir trīs darbības - vērtības sagaidīšana, vērtības pārveidošana un vērtības piešķiršana
# argument = input()
# int(argument)
# a = int(argument) -->

# pildot int(input()) "bez izmēģinājuma" programma var vienkārši izlidot ...
# tāpēc, lai "nelidotu" mēs izmantosim try ...  except ... finally kontrukciju
pazīme = False
while not pazīme:
# while pazīme==False:
# while pazīme!=True:
    try:
        a=int(input())
        pazīme = True
    except:
        print("Cienījamais lietotāj, diemžēl ievadīto vērtību nevar pārveidot par vesela tipa skaitli :(")
        print("Lūgums ievadīt SKAITLI vēlreiz!")

'''
pazīme = True
while pazīme:
    try:
        a=int(input())
        pazīme = False
    except:
        print("Cienījamais lietotāj, diemžēl ievadīto vērtību nevar pārveidot par vesela tipa skaitli :($
        print("Lūgums ievadīt SKAITLI vēlreiz!")
'''

# if (a == int): print("a**100")
# ja ļoti gribās, tad var salīdzināt type(a) == int -> rezultāts būs True

# if (a=type(int)):
print(a**100)
print("Aprēķins ir gatavs")
print(" Šis teksts atrodas ārpus bloka,\n",\
      "tāpēc tas parādīsies (pierakstīts bez atstarpēm priekšā).\n",\
      "Jebkurā gadījumā!")

# print ("Ievadāmai vērtībai jābūt skaitlim")

'''
if type(a) == int:
    print("GG")
else:
    print("YOU SUCK")
'''
