#Instruktionsuppgift
from time import sleep
import random

DELAY = 0.2

name = input("Vad heter du? ")
life = 4
demon = 20
while True:
    if name.lower() == "jens":
        choice = input("Nu, Jens, är det dags för att lära ut eltreorna! Du får totalt 4 liv. Hälsar du på dina elever? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("De hälsar tillbaka! Emil ger dig till och med en high-five. Du känner dig peppad.")

        if choice.lower() == "n" or choice.lower() == "no":
            print("Alla eleverna tar upp sina telefoner. Inte en bra start, Jens.")
            sleep(DELAY)
            print("...")
            sleep(DELAY)
            choice = input("Säger du till dem på skarpen? [Y]es/[N]o: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Alla sätter bort sina telefoner, men de lyssnar inte. -1 liv")
                life -= 1
            
            if choice.lower() == "n" or choice.lower() == "no":
                print("Alla lyssnar på dig när du säger till dem snällt. Du mår bra.")
        sleep(DELAY)
        print("...")
        sleep(DELAY)
        choice = input("Du förbereder presentationen, men du märker att Viggo håller på att göra ett pappersflygplan. Tar du papperet och kastar den i soptunnan? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Alla skrattar åt Viggo! Du har fått klassens respekt. Du känner dig maktfull.")
        if choice.lower() == "n" or choice.lower() == "no":
            print("Viggo kastar pappersflygplanet på Gustav! Han blir ledsen och går ut ur klassrummet. -1 liv")
            life -= 1
        sleep(DELAY)
        print("...")
        sleep(DELAY)
        choice = input("Det är 30 minuter kvar av lektionen. Alla jobbar intensivt. Lyssnar du på dina tankar och skriker? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Alla stirrar på dig. Det tar en sekund, men Mohammad börjar garvskratta och sedan följer resten. Du känner dig rolig.")
        if choice.lower() == "n" or choice.lower() == "no":
            print("Ingenting händer, men du känner dig töntig som inte skrek. -1 liv")
            life -= 1
        sleep(DELAY)
        print("...")
        sleep(DELAY)
        choice = input("Nu är lektionen snart slut! Låter du dina elever sluta 5 minuter tidigare? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Alla jublar och ler samtidigt som de reser sig upp för att gå! Du har klarat av sista fredagslektionen. Bra jobbat, Jens!")
        elif choice.lower() == "n" or choice.lower() == "no":
            print("Ingen är glad. Alvin har somnat och Alexander drog tidigt för att supa sig full. -1 liv")
            life -= 1
        
        sleep(DELAY)
        print("...")
        sleep(DELAY)
        if life == 4:
            print("Liv kvar: 4")
            print("Bra jobbat, du överlevde dagen! Du fick till och med en maraboukaka av Elvira.")
        elif life == 3:
            print("Liv kvar: 3")
            print("Kunde gjort bättre, men rektorn gav dig en stjärna för att ha avklarat dagen ändå.")
        elif life == 2:
            print("Liv kvar: 2")
            print("Det var nära gränsen, men du överlevde dagen!")
        elif life == 1:
            print("Liv kvar: 1")
            print("Dagen är över och du fick tomater kastade på dig av elever samt lärare. Dags att gråta dig själv till sömns.")
        elif life == 0:
            print("Liv kvar: 0")
            print("Hur lyckades du?")
            break

        sleep(DELAY)
        print("...")
        sleep(DELAY)
        life *= 10
        print("Nu är det dags för att sova och förbereda dig själv inför nästa dag... Vänta, vad är det där?")
        sleep(DELAY)
        print("...")
        sleep(DELAY)
        print("En sömnparalys demon har dykt upp! Besegra den med liven du har kvar!")
        sleep(DELAY)
        print("Dina liv multipliceras med 10! Nuvarande liv kvar: ", life)
        if life == 0:
            sleep(DELAY)
            print("...")
            sleep(DELAY)
            print("Sömnparalys demonen äter upp dig. Det visade sig att det var Gustav all along! Du skäms.")
            break
        sleep(DELAY)
        print("...")
        sleep(DELAY)
        choice = input("Är du redo att gambla bort dina liv? [Y]es:")
        if choice.lower() == "y" or choice.lower() == "yes":
            while True:
                print ('Livet har kastats...')
                sleep(DELAY)
                print("...")
                sleep(DELAY)
                n = random.randint(1,6) # randomizar ett nummer för n
                m = random.randint(1,6) # randomizar ett nummer för m
                print("Du slog en: ", n,)
                print("Sömnparalys demonen slog en: ", m)
                life -= n
                demon -= m
                sleep(DELAY)
                print("...")
                sleep(DELAY)
                print("Dina liv kvar: ", life)
                print("Demonens liv kvar: ", demon)
                sleep(DELAY)
                print("...")
                sleep(DELAY)
                if life <= 0:
                    print("Sömnparalys demonen äter upp dig. Det visade sig att det var Gustav all along! Du skäms.")
                    break
                if demon <= 0:
                    print("Du besegrade din värsta mardröm! Du inspekterar demonen, och... Är det där Gustav? Gustav Hörnlund?")
                    sleep(DELAY)
                    print("...")
                    sleep(DELAY)
                    print("Du defenestrerar honom.")
                    break
                choice = input("Är du redo att slå igen? [Y]es:")
            else:
                print("nähä")
                break
    else:
        print("Du är inte berättigad för att lära ut elarna.")
        break
        