# den här koden kastar två tärningar och sätter sedan ihop dem till ett totalnummer

import random
while True:
    print ('Tärningarna är kastade:')
    n = random.randint(1,6) # randomizar ett nummer för n
    m = random.randint(1,6) # randomizar ett nummer för m
    print(n) # printar det randomizade nummeret för n
    print(m) # printar det randomizade nummeret för m
    print('Du fick', n, 'och', m)
    print('Totalnummer är', n + m)
    
    if n == m:
        choice = input("Du fick två likadana! Vill du fortsätta? [Y]es/[N]o: ")
        if choice.lower() == "n" or choice.lower() == "no":
            print("Okej, lycka till nästa gång!")
            break
        if choice.lower == "y" or choice.lower() == "yes":
            continue