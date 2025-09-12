# den här koden kastar två tärningar och sätter sedan ihop dem till ett totalnummer

import random
print ('Tärningarna är kastade:')
n = random.randint(1,6) # randomizar ett nummer för n
m = random.randint(1,6) # randomizar ett nummer för m
print(n) # printar det randomizade nummeret för n
print(m) # printar det randomizade nummeret för m
print('Du fick', n, 'och', m)
print('Totalnummer är', n + m)