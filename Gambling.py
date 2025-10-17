import random
from time import sleep

DELAY = 2

balance = 90

fourstarbalance = 10

fourstarcurrent = 0
fivestarcurrent = 0

threestars = 0
fourstars = 0
fivestars = 0

print("Let's go gacha gambling!")
sleep(DELAY)
print(f"You currently have {balance} wishes.")
sleep(DELAY)
choice = input("Will you do a ten pull or a one pull? [T]en/[O]ne: ")
if choice.lower() == "t" or choice.lower() == "ten":
    
    n1 = random.randint(1,10000)
    n2 = random.randint(1,10000)
    n3 = random.randint(1,10000)
    n4 = random.randint(1,10000)
    n5 = random.randint(1,10000)
    n6 = random.randint(1,10000)
    n7 = random.randint(1,10000)
    n8 = random.randint(1,10000)
    n9 = random.randint(1,10000)
    n10 = random.randint(1,10000)
    
    if fivestars > 0:
        fivestarchance = 60
        fivestarchance1 = 61
        fourstarchance = 570
        threestarchance = 571
        threestarchance2 = 10000
    if balance >= 15 and balance <= 90 and fivestars == 0:
        fivestarchance = 60
        fivestarchance1 = 61
        fourstarchance = 570
        threestarchance = 571
        threestarchance2 = 10000
    if balance >= 10 and balance <= 15 and fivestars == 0:
        fivestarchance = 3000
        fivestarchance1 = 3001
        fourstarchance = 3571
        threestarchance = 3572
        threestarchance2 = 10000
    if balance >= 5 and balance <= 9 and fivestars == 0:
        fivestarchance = 5000
        fivestarchance1 = 5001
        fourstarchance = 5571
        threestarchance = 5572
        threestarchance2 = 10000
    if balance >= 2 and balance <= 4 and fivestars == 0:
        fivestarchance = 8000
        fivestarchance1 = 8001
        fourstarchance = 8571
        threestarchance = 8572
        threestarchance2 = 10000
    if balance == 1 and fivestars == 0:
        fivestarchance = 10000
        fivestarchance2 = -1
        fourstarchance = -1
        threestarchance = -1
        threestarchance2 = -1

    if n1 >= 0 and n1 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n1 >= fivestarchance1 and n1 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n1 >= threestarchance and n1 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1

    if n2 >= 0 and n2 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n2 >= fivestarchance1 and n2 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n2 >= threestarchance and n2 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1
        
    if n3 >= 0 and n3 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n3 >= fivestarchance1 and n3 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n3 >= threestarchance and n3 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1

    if n4 >= 0 and n4 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n4 >= fivestarchance1 and n4 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n4 >= threestarchance and n4 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1

    if n5 >= 0 and n5 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n5 >= fivestarchance1 and n5 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n5 >= threestarchance and n5 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1

    if n6 >= 0 and n6 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n6 >= fivestarchance1 and n6 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n6 >= threestarchance and n6 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1

    if n7 >= 0 and n7 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n7 >= fivestarchance1 and n7 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n7 >= threestarchance and n7 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1

    if n8 >= 0 and n8 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n8 >= fivestarchance1 and n8 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n8 >= threestarchance and n8 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1

    if n9 >= 0 and n9 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n9 >= fivestarchance1 and n9 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n9 >= threestarchance and n9 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1

    if n10 >= 0 and n10 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
        print("You got a 5 star! Congratulations!")
        fivestars += 1
        balance -= 1
        fivestarcurrent += 1
    if n10 >= fivestarchance1 and n10 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
        print("You got a 4 star! Wow!")
        fourstars += 1
        fourstarcurrent += 1
        balance -= 1
    if n10 >= threestarchance and n10 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
        print("You got a 3 star!")
        threestars += 1
        fourstarbalance -= 1
        balance -= 1

print(f"Your account now consists of {threestars} three star(s), {fourstars} four star(s) and {fivestars} five star(s).")
print(f"You have {balance} wishes left.")

fourstarbalance = 10
fourstarcurrent = 0
fivestarcurrent = 0

if choice.lower() == "o" or choice.lower() == "one":
        n = random.randint(1,10000)

        if fivestars > 0:
            fivestarchance = 60
            fivestarchance1 = 61
            fourstarchance = 570
            threestarchance = 571
            threestarchance2 = 10000
        if balance >= 15 and balance <= 90 and fivestars == 0:
            fivestarchance = 60
            fivestarchance1 = 61
            fourstarchance = 570
            threestarchance = 571
            threestarchance2 = 10000
        if balance >= 10 and balance <= 15 and fivestars == 0:
            fivestarchance = 3000
            fivestarchance1 = 3001
            fourstarchance = 3571
            threestarchance = 3572
            threestarchance2 = 10000
        if balance >= 5 and balance <= 9 and fivestars == 0:
            fivestarchance = 5000
            fivestarchance1 = 5001
            fourstarchance = 5571
            threestarchance = 5572
            threestarchance2 = 10000
        if balance >= 2 and balance <= 4 and fivestars == 0:
            fivestarchance = 8000
            fivestarchance1 = 8001
            fourstarchance = 8571
            threestarchance = 8572
            threestarchance2 = 10000
        if balance == 1 and fivestars == 0:
            fivestarchance = 10000
            fivestarchance2 = -1
            fourstarchance = -1
            threestarchance = -1
            threestarchance2 = -2

        if n1 >= 0 and n1 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
            print("You got a 5 star! Congratulations!")
            fivestars += 1
            balance -= 1
            fivestarcurrent += 1
        if n1 >= fivestarchance1 and n1 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
            print("You got a 4 star! Wow!")
            fourstars += 1
            fourstarcurrent += 1
            balance -= 1
        if n1 >= threestarchance and n1 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
            print("You got a 3 star!")
            threestars += 1
            fourstarbalance -= 1
            balance -= 1

while balance >= 1:
    choice = input("Pull again? [Y]es/[N]o: ")
    if choice.lower() == "n" or choice.lower() == "no":
        balance -= 10
    if choice.lower() == "y" or choice.lower() == "yes":
        choice = input("What kind of pull? [T]en/[O]ne:")
        if choice.lower() == "ten" or choice.lower() == "t":
            fourstarbalance = 10

            n1 = random.randint(1,10000)
            n2 = random.randint(1,10000)
            n3 = random.randint(1,10000)
            n4 = random.randint(1,10000)
            n5 = random.randint(1,10000)
            n6 = random.randint(1,10000)
            n7 = random.randint(1,10000)
            n8 = random.randint(1,10000)
            n9 = random.randint(1,10000)
            n10 = random.randint(1,10000)
            
            if fivestars > 0:
                fivestarchance = 60
                fivestarchance1 = 61
                fourstarchance = 570
                threestarchance = 571
                threestarchance2 = 10000
            if balance >= 15 and balance <= 90 and fivestars == 0:
                fivestarchance = 60
                fivestarchance1 = 61
                fourstarchance = 570
                threestarchance = 571
                threestarchance2 = 10000
            if balance >= 10 and balance <= 15 and fivestars == 0:
                fivestarchance = 3000
                fivestarchance1 = 3001
                fourstarchance = 3571
                threestarchance = 3572
                threestarchance2 = 10000
            if balance >= 5 and balance <= 9 and fivestars == 0:
                fivestarchance = 5000
                fivestarchance1 = 5001
                fourstarchance = 5571
                threestarchance = 5572
                threestarchance2 = 10000
            if balance >= 2 and balance <= 4 and fivestars == 0:
                fivestarchance = 8000
                fivestarchance1 = 8001
                fourstarchance = 8571
                threestarchance = 8572
                threestarchance2 = 10000
            if balance == 1 and fivestars == 0:
                fivestarchance = 10000
                fivestarchance2 = -1
                fourstarchance = -1
                threestarchance = -1
                threestarchance2 = -2

            if n1 >= 0 and n1 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n1 >= fivestarchance1 and n1 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n1 >= threestarchance and n1 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1

            if n2 >= 0 and n2 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n2 >= fivestarchance1 and n2 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n2 >= threestarchance and n2 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1
                
            if n3 >= 0 and n3 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n3 >= fivestarchance1 and n3 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n3 >= threestarchance and n3 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1

            if n4 >= 0 and n4 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n4 >= fivestarchance1 and n4 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n4 >= threestarchance and n4 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1

            if n5 >= 0 and n5 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n5 >= fivestarchance1 and n5 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n5 >= threestarchance and n5 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1

            if n6 >= 0 and n6 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n6 >= fivestarchance1 and n6 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n6 >= threestarchance and n6 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1

            if n7 >= 0 and n7 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n7 >= fivestarchance1 and n7 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n7 >= threestarchance and n7 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1

            if n8 >= 0 and n8 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n8 >= fivestarchance1 and n8 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n8 >= threestarchance and n8 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1

            if n9 >= 0 and n9 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n9 >= fivestarchance1 and n9 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n9 >= threestarchance and n9 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1

            if n10 >= 0 and n10 <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if n10 >= fivestarchance1 and n10 <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if n10 >= threestarchance and n10 <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1

            print(f"Your account now consists of {threestars} three star(s), {fourstars} four star(s) and {fivestars} five star(s).")
            print(f"You have {balance} wishes left.")

            fourstarbalance = 10
            fourstarcurrent = 0
            fivestarcurrent = 0

        if choice.lower() == "one" or choice.lower() == "o":        
            m = random.randint(1,10000)

            if fivestars > 0:
                fivestarchance = 60
                fivestarchance1 = 61
                fourstarchance = 570
                threestarchance = 571
                threestarchance2 = 10000
            if balance >= 15 and balance <= 90 and fivestars == 0:
                fivestarchance = 60
                fivestarchance1 = 61
                fourstarchance = 570
                threestarchance = 571
                threestarchance2 = 10000
            if balance >= 10 and balance <= 15 and fivestars == 0:
                fivestarchance = 3000
                fivestarchance1 = 3001
                fourstarchance = 3571
                threestarchance = 3572
                threestarchance2 = 10000
            if balance >= 5 and balance <= 9 and fivestars == 0:
                fivestarchance = 5000
                fivestarchance1 = 5001
                fourstarchance = 5571
                threestarchance = 5572
                threestarchance2 = 10000
            if balance >= 2 and balance <= 4 and fivestars == 0:
                fivestarchance = 8000
                fivestarchance1 = 8001
                fourstarchance = 8571
                threestarchance = 8572
                threestarchance2 = 10000
            if balance == 1 and fivestars == 0:
                fivestarchance = 10000
                fivestarchance2 = -1
                fourstarchance = -1
                threestarchance = -1
                threestarchance2 = -2

            if m >= 0 and m <= fivestarchance: #0-60, 0-3000, 0-5000, 0-8000, 0-10000
                print("You got a 5 star! Congratulations!")
                fivestars += 1
                balance -= 1
                fivestarcurrent += 1
            if m >= fivestarchance1 and m <= fourstarchance: #61-570, 3001-3571, 5001-5571, 8001-8571, 0
                print("You got a 4 star! Wow!")
                fourstars += 1
                fourstarcurrent += 1
                balance -= 1
            if m >= threestarchance and m <= threestarchance2: #571-10000, 3572-10000, 5571-10000, 8571-10000, 0
                print("You got a 3 star!")
                threestars += 1
                fourstarbalance -= 1
                balance -= 1


if fourstarbalance == 1 and fourstarcurrent == 0:
    choice = input("Pull again? [Y]es/[N]o:")
    if choice.lower() == "n" or choice.lower() == "no":
        balance -= 10
    if choice.lower() == "y" or choice.lower() == "yes":
        print("You got a 4 star!")
        fourstars += 1
        balance -= 1
        print("...")
        sleep(0.5)
        print(f"Wishes left: {balance}")

if balance <= 0:
    print("...")
    sleep(DELAY)
    print("You have no more wishes!")
    sleep(0.5)
    print(f"Your pulling session included: Your account now consists of {threestars} three star(s), {fourstars} four star(s) and {fivestars} five star(s).")

            
                

