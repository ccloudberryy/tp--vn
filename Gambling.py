import random
from time import sleep

delay = 2
balance = 10
threestar = 0
fourstar = 0
fivestar = 0

print("Let's go gacha gambling!")
sleep(delay)
print(f"You currently have {balance} wishes.")
sleep(delay)
choice = input("Do you want to pull on the gacha banner once? [Y]es/[N]o: ")
if choice.lower() == "n" or choice.lower() == "no":
    print(f"Your pulling session included: {threestar} three stars, {fourstar} four stars and {fivestar} five stars.")
    balance -= 10
if choice.lower() == "y" or choice.lower() == "yes":
        n = random.randint(1,10000)
        balance -= 1
        if n >= 60:
            n = random.randint(1,10000)
            if n <= 510:
                print("You got a 4 star! Wow!")
                print("...")
                sleep(0.5)
                print(f"Wishes left: {balance}")
                fourstar += 1
            if n >= 510:
                print("You got a 3 star!")
                print("...")
                sleep(0.5)
                print(f"Wishes left: {balance}")
                threestar += 1
        if n <= 60:
            print("You got a 5 star! Congratulations!")
            print("...")
            sleep(0.5)
            print(f"Wishes left: {balance}")
            fivestar += 1
        while balance > 1:
            choice = input("Pull again? [Y]es/[N]o: ")
            if choice.lower() == "n" or choice.lower() == "no":
                balance -= 10
            if choice.lower() == "y" or choice.lower() == "yes":
                m = random.randint(1,10000)
                balance -= 1
                if m >= 60:
                    m = random.randint(1,10000)
                    if m <= 510:
                        print("You got a 4 star! Wow!")
                        print("...")
                        sleep(0.5)
                        print(f"Wishes left: {balance}")
                        fourstar += 1
                    if m >= 510:
                        print("You got a 3 star!")
                        print("...")
                        sleep(0.5)
                        print(f"Wishes left: {balance}")
                        threestar += 1
                if m <= 60:
                    print("You got a 5 star! Congratulations!")
                    print("...")
                    sleep(0.5)
                    print(f"Wishes left: {balance}")

                    fivestar += 1
if balance == 1 and fourstar == 0:
    choice = input("Pull again? [Y]es/[N]o:")
    if choice.lower() == "n" or choice.lower() == "no":
        balance -= 10
    if choice.lower() == "y" or choice.lower() == "yes":
        print("You got a 4 star!")
        fourstar += 1
        balance -= 1
        print("...")
        sleep(0.5)
        print(f"Wishes left: {balance}")
if balance <= 0:
    print("...")
    sleep(delay)
    print("You have no more wishes!")
    sleep(0.5)
    print(f"Your pulling session included: {threestar} three star(s), {fourstar} four star(s) and {fivestar} five star(s).")

            
                

