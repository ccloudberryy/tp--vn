#Instruktionsuppgift
from time import sleep
import random

DELAY = 0.5

name = input("Vad heter du? ")
life = 4
demon = 20

sen = 0
bajs = 0
tänder = 0

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
    if name.lower() == "emil":
        print("[Emils tale börjar, och DU styr honom!]")
        sleep(DELAY)
        print("...")
        sleep(DELAY)
        print("Emil gäspar och stiger upp ur sängen.")
        sleep(DELAY)
        choice.input("Han kollar sig själv i spegeln och märker att han inte har borstat sina tänder än. Borstar han sina tänder?: [Y]es/[N]o")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Han går in till badrummet och borstar sina tänder.")
        if choice.lower() == "n" or choice.lower() == "no":
            print("Emil tänker efter lite, men bestämmer sig för att inte borsta sina tänder. Han orkar inte.")
            tänder += 1
            # OBORSTADE TÄNDER = 1
        sleep(DELAY)
        input("Emil sätter på sig sina kläder och ska nu ta sig till skolan.")
        choice.input("Han känner sig fortfarande trött i kroppen. Ska Emil ta bussen?: [Y]es/[N]o")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Han går till sin busshållplats och väntar 5 minuter tills den äntligen kommer.")
            sleep(DELAY)
            choice.input("Han stiger på bussen. Försöker han undvika att betala sin bussbiljett?: [Y]es/[N]o")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Han försöker smita sig på bussen, men busschauffören skriker och kickar ut honom.")
                sleep(DELAY)
                print("Han väntar 15 minuter på nästa buss och betalar sin bussbiljett den här gången.")
                sen += 1
                # SEN TILL SKOLAN
            if choice.lower() == "n" or choice.lower() == "no":
                print("Han stiger på bussen och betalar sin bussbiljett.")
                sleep(DELAY)
                print("Busschauffören ger Emil en sne blick som om han kunde läsa Emil tankar.")    
        if choice.lower() == "n" or choice.lower() == "no":
            print("Han tar på sig sina skor och börjar promenera till skolan.")
            sleep(DELAY)
            choice.print("Emil märker inte det, men det ligger hundbajs framför honom. Du bestämmer, ska han gå i det?: [Y]es/[N]o")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Han går i hundbajset. Han märker att sina skor är kladdiga och tar en titt.")
                sleep(DELAY)
                print('"EWWW!!" skriker han. Han står en stund i tystnad men fortsätter gå. Han har en lektion att ta sig till.')
                bajs += 1
                # BAJS PÅ SKORNA
            if choice.lower() == "n" or choice.lower() == "no":
                print("Han märker hundbajset på sista sekunden och undviker det.")
                sleep(DELAY)
                print("Han låter ut ett ljud av lättnad. Han fortsätter promenera till skolan.")
        sleep(DELAY)
        print("Nu är han framme vid skolan. Han går in och ser sin vän Isak Engman.")
        sleep(DELAY)
        choice.input("De går in i hissen tillsammans. Skriker dem?: [Y]es/[N]o")
        if choice.lower() == "y" or choice.lower() == "yes":
            print('De skriker högt "HJÄLP!!! HJÄÄÄLP!!!". När de stiger ut ur hissen märker de att Eszter står precis utanför.')
            sleep(DELAY)
            print('Eszter säger till dem på skarpen.')
        if choice.lower() == "n" or choice.lower() == "no":
            print("Ovanligt beteende för Emil. Han skriker inte i hissen.")
            sleep(DELAY)
            choice.input("Tar Emil på Isaks bröst istället?: [Y]es/[N]o.")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Isak stönar högt medan hissen är påväg upp.")
                sleep(DELAY)
                print("När hissdörren öppnas så märker de att Eszter står precis utanför.")
                sleep(DELAY)
                print("Hon säger till dem båda på skarpen, även om Emil försökte säga att det bara var Isak.")
            if choice.lower() == "n" or choice.lower() == "no":
                print("Ingenting sker.")
                sleep(DELAY)
                print("När hissdörren öppnas så lättnar Emil då han ser Eszter precis utanför. Bra att han inte gjorde något.")
        print("Emil tar av sig sina skor och går till sin lektion i Aristoteles.")
        sleep(DELAY)
        if sen == 1:

    else:
        print("Du är inte berättigad för att lära ut elarna.")
        break
        