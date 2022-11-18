import random
price = random.randint(1, 10)
score=100
tentatives=0
print("Try to find the right price")
print("The right price is a number inclued between 1 and 10")

while True:
    number = int(input())
    tentatives += 1
    if number < price:
        print("The right price is upper")
    if number > price:
        print("The right price is downer")
    if number == price:
        print("Congratuation you win ! You find the right price {} in {} try, you're score is {} !" .format(price, tentatives, int(score / tentatives)))
        break
    
print ("endgame")

    #(c) Alexis.d AKA Aldbg74 2022
    #42 for ever