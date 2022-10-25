# Every key assumed as UserName and its value as password.

from random import randint
import json

authorizedUsers = {
'admin':'admin'
}
generalUsers = {
'user':'1234'
}
items = {
   '123aa':('Applicance','karachi','bad'),
}
voluneeredUsers={
   'admin':'itemid'
}
try:
   with open('authorizedUsers.json') as f:
      authorizedUsers = json.load(f)
   with open('generalUsers.json') as f:
      generalUsers = json.load(f)
   with open('items.json') as f:
      items = json.load(f)
except: pass
authorizedUser = False
voluneered = False
print("\nProject Donate\n")
print("Please select following options: ")
while True:
   login = input("1.Login\n2.Register\n>")
   if login == '1': pass
   elif login == '2':
      name = input("Enter your user name: ")
      name = name.lower()
      if name in [*generalUsers] or name in [*authorizedUsers]:
         print("Sorry, User name already exists try again...")
         continue
      else:
         password = input("Enter your password: ")
         print("Registration Complete\n Login using your new account.")
         generalUsers[name]=password
         with open('generalUsers.json', 'w') as f:
            json.dump(generalUsers, f)
   else:
      print("Invalid, Please select valid option.")
      continue
   break
while True:
   name = input("Enter your user name: ")
   password = input("Enter your password: ")
   name = name.lower()
   if name == 'q' or password == 'q': 
      print("System terminated...")
      exit()
   elif name in [*authorizedUsers]:
      authorizedUser = True
      if authorizedUsers[name] == password:
         print('\nAuthorized User')
      else:
         print('wrong password')
         continue
      break
   elif name in [*generalUsers]:
      authorizedUser = False
      if generalUsers[name] == password:
         print('\nGeneral User')
      else:
         print('wrong password')
         continue
      break
   else : print('User name not found, please try again or "q" to quit.')

print("\nWelcome "+ name +"...")
if authorizedUser == True:
   while True:
      select = input("\n1. View donated items\n2. View list of GeneralUsers\n>")
      if select == '1':
         for item in [*items]:
            print('\nId:', item,"\nitemType:", items[item][0], "\nLocation:", items[item][1],"\nQuality:", items[item][2])
      elif select == '2':
         for user in [*generalUsers]:
            print("\n UserName:",user)
      print("Please, type item id at end to voluneer to distribute item.")
      idItem = input(">>")
      if idItem in [*items]:
         print('\nId:', idItem,"\nitemType:", items[idItem][0], "\nLocation:", items[idItem][1],"\nQuality:", items[idItem][2])
         confrim = input('\nDo you want to deliver this item (Y/N):')
         if confrim.lower() == "y":
            print("You've voluneered to deviler the item within 24hours\n")
            exit()
            break
         else: continue
      else:
         print("item not found, try again")
         continue
            
print("Please select one of the options:")
print("1. Donate items.\n2. Donate cash")
while True:
   option = input('>>')
   if option == '1': 
      while True:
         itemType = input('please specify item type from one of following list: \n1.Appliances.\n2.Furniture.\n3.Electronic Equipment.\n4.Carpets.\n')
         print()
         if itemType == '1':
            itemType = 'Appliances'
         elif itemType == '2':
            itemType = 'Furniture'
         elif itemType == '3':
            itemType = "Electronic Equipment"
         elif itemType == '4':
            itemType = 'Carpets'
         else:
            print("Invaild, please choose from the list.\n")
            continue
         break
      while True:
         location = input('please specify location of item.\n1.Jamshoro.\n2.Hyderabad.\n3.Karachi.\n')
         print()
         if location == '1':
            location = 'Jamshoro'
         elif location == '2':
            location = 'Hyderabad'
         elif location == '3':
            location = "Karachi"
         else:
            print("Invaild, please choose from the list.\n")
            continue
         break
      while True:
         quality = input('please specify condition of the item.\n1.Very Good.\n2.Good.\n3.Bad.\n')
         print()
         if quality == '1':
            quality = 'Very Good'
         elif quality == '2':
            quality = 'Good'
         elif quality == '3':
            quality = "Bad"
         else:
            print("Invaild, please choose from the list.\n")
            continue
         break
      a = str(randint(1,100)) + quality[randint(0,2)] + str(randint(1,100)) + location[randint(0,2)]
      b = str(randint(1,100)) + quality[randint(0,2)] + str(randint(1,100)) + location[randint(0,2)]
      itemId = a + b
      items [itemId] = (itemType, location, quality)
      print("Item has been donated.Thanks for your support.\n")
      break
   elif option == '2':
      print("This feature is currently unavialabe...\n")
      continue
   else:
      print("please select valid option.\n")
      continue
   break
with open('authorizedUsers.json', 'w') as f:
    json.dump(authorizedUsers, f)
with open('generalUsers.json', 'w') as f:
    json.dump(generalUsers, f)
with open('items.json', 'w') as f:
    json.dump(items, f)