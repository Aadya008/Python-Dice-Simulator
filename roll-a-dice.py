import random
from PIL import Image

response = input("Say 'y' if you want to roll the dice. Say 'n' if not: ")
#print (response)
while response =='y':
    number = random.randint(1,6)
    if number == 1:
        image =Image.open("dice1.jpeg")
        image.show()
    if number == 2:
        image = Image.open("dice2.png") 
        image.show()   
    if number == 3:
        image = Image.open("dice3.png") 
        image.show()   
    if number == 4:
        image = Image.open("dice4.png") 
        image.show()  
    if number == 5:
        image = Image.open("diceno5.png") 
        image.show() 
    if number == 6:
        image = Image.open("dice6.png") 
        image.show()                      
    response = input("Say 'y' if you want to roll the dice. Say 'n' if not: ")
if response == 'n':
    print("Thank You For Playing!") 