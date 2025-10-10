import random
from time import sleep

DELAY = 2

balance = 90
threestar = 0
fourstar = 0
fivestar = 0

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
    if n1 >= 60:
        n1 = random.randint(1,10000)
        if n1 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n1 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n1 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    if n2 >= 60:
        n2 = random.randint(1,10000)
        if n2 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n2 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n2 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    if n3 >= 60:
        n3 = random.randint(1,10000)
        if n3 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n3 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n3 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    if n4 >= 60:
        n4 = random.randint(1,10000)
        if n4 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n4 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n4 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    if n5 >= 60:
        n5 = random.randint(1,10000)
        if n5 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n5 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n5 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    if n6 >= 60:
        n6 = random.randint(1,10000)
        if n6 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n6 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n6 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    if n7 >= 60:
        n7 = random.randint(1,10000)
        if n7 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n7 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n7 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    if n8 >= 60:
        n1 = random.randint(1,10000)
        if n8 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n8 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n8 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    if n9 >= 60:
        n9 = random.randint(1,10000)
        if n9 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n9 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n9 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    if fourstar == 0:
        print("You got a 4 star! Wow!")
        fourstar += 1
    elif n10 >= 60:
        n10 = random.randint(1,10000)
        if n10 <= 510:
            print("You got a 4 star! Wow!")
            fourstar += 1
        if n10 >= 510:
            print("You got a 3 star!")
            threestar += 1
    if n10 <= 60:
        print("You got a 5 star! Congratulations!")
        fivestar += 1
    print(f"You recieved {threestar} three star(s), {fourstar} four star(s) and {fivestar} five star(s).")
    print(f"Du har totalt {balance} wishes kvar.")
    balance -= 10
if choice.lower() == "o" or choice.lower() == "one":
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
    sleep(DELAY)
    print("You have no more wishes!")
    sleep(0.5)
    print(f"Your pulling session included: {threestar} three star(s), {fourstar} four star(s) and {fivestar} five star(s).")

            
                

