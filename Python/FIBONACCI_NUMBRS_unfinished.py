# Fibonači skaitļu daudzums pēc pieprasījuma

x = int(input("Cik Fibonači skaitļus attēlot? "))

# Pirmie divi skaitļi
n1, n2 = 0, 1
count = 0

# Vai ievadītais skaitlis ir pozitīvs reāls skaitlis?
if x <= 0:
######### Pārveidot par nebeidzamu loop, kamēr netiks ievadīts poz., reāls skaitlis!!!
   print("Ievadīt positīvu, reālu skaitli:")
elif x == 1:
   print(0)
else:
######### Kā izprintēt loop mainīgos vienā rindā? #########
   print("Pieprasītie",x,"fibonači skaitļi: ")
   while count < x:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
