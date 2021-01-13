import random
def sarah():
    a = 0 
    gentille = []
    while a <= 100:
        stockeur = random.randint(0, 999)
        gentille.append(stockeur)
        if gentille[a] % 2 == 0:
            print(gentille[a])
        a += 1


sarah()

