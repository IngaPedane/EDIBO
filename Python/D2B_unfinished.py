print("Ievadiet skaitli: ")
a=int(input())
######### Kā dabūt, lai inputs un teksts ir vienā līnijā? #########
#a=int(input ("Ievadiet skaitli: ")()) 
#a=int(input())("Ievadiet skaitli: ")
#print(, a)

######### Kā dabūt, lai informācija attēlojas ar tukšu rindu starpā? #########
#print("Ievadiet skaitli:", a)
#print("\n")
#b=a

while int(a) != 0:
######### Kā dabūt b vērtību teksta vidū? #########
    print("Šī ir skaitļa b binārā vērtība", (int(a))%2) 
    #print(a)
    a = int(a/2)

######### Kā izprintēt loop mainīgos vienā rindā? #########
#for i in range(a/2):
    #print(i)
     
#print("Šī ir skaitļa b binārā vērtība")
