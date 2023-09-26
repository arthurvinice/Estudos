#This code makes a travel register.
#Asks for a traveler name, show some destination options
#and print the selected destination.

from travel import Travel

travel0 = Travel("Berlin")
travel1 = Travel("Dublin")
travel2 = Travel("Rome")
travel3 = Travel("Paris")
travel4 = Travel("Oslo")

print("Welcome! Check out the Air Travels offers!")
name = input("Your name is? ")
print(f'Okay, {name}, we have the perfect destinations for you. Type the number that matches your choice:'
'''
[0] Berlin
[1] Dublin
[2] Rome
[3] Paris
[4] Oslo''')

choice = int(input('Destination: '))
cities_list = [travel0, travel1, travel2, travel3, travel4]
choice_int = int(choice)
for choice in cities_list:
    if 0 > choice_int >= 5:
       print('Error: Not possible.')
       break
    else:
       print(f'{name}, your travel to {cities_list[choice_int].place} is now confirmed! ')
       print('Thanks for chosing Air Travel!')
       break
   