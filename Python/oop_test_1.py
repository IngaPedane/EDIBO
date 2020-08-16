class PartyAnimal:
   x = 0

# __init__ metode tiks izpildīta tikai vienu reizi
# veidojot, (katru) instanci 
   def __init__(self):
     print('I am constructed')
     self.x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far x property of object",\
           "is: ",self.x)
     
#   def __del__(self):
#     print("I'm destructed", self.x)  

print("Before an = PArtyAnimal()")
# print(vars())
an = PartyAnimal()
print("After an = PArtyAnimal()")
# print(vars())
# print("an data type or class: ", type(an))
# print("an methods and properties: ", dir(an)) # noskaidrojam metodes attiecībā pret šo objektu
# print("an x property data type: ", type(an.x))
# print("an party method data type: ", type(an.party))
# print(vars(an))
# tikai ja klase ir ar __init__ ar self.x = ...,
# tikai tad {'x': 0}, citādi ir {}

print("\nBefore first an.party()")
an.party()
print("After first an.party()")
# print(vars(an)) # objekts "aiztikts" {'x': 1}

an.x = 100
an.__init__()

print("\nBefore second an.party()")
an.party()
print("After second an.party()")

an.x = 200

print("\nBefore third an.party()")
an.party()
print("After third an.party()")

print("\nBefore one more an.party()")
PartyAnimal.party(an)
print("After one more an.party()")

# print ("Type", type(an))
# print ("Dir ", dir(an))
# print ("Type", type(an.x))
# print ("Type", type(an.party))

# Code: http://www.py4e.com/code3/party3.py
