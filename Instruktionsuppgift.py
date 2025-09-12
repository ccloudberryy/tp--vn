#Instruktionsuppgift
name = input("Vad heter du? ")
while True:
    if name.lower() == "jens":
        choice = input("Nu, Jens, är det dags för att lära ut eltreorna! Du får totalt 3 liv. Hälsar du på dina elever? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("De hälsar tillbaka! Emil ger dig till och med en high-five. Du känner dig peppad.")

        if choice.lower() == "n" or choice.lower() == "no":
            print("Alla eleverna tar upp sina telefoner. Inte en bra start, Jens.")
            choice = input("Säger du till dem på skarpen? [Y]es/[N]o: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Alla sätter bort sina telefoner, men de lyssnar inte. -1 liv")
        
            if choice.lower() == "n" or choice.lower() == "no":
                print("Alla lyssnar på dig när du säger till dem snällt. Du mår bra.")
        

        choice = input("Du förbereder presentationen, men du märker att Viggo håller på att göra ett pappersflygplan. Tar du papperet och kastar den i soptunnan? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Alla skrattar åt Viggo! Du har fått klassens respekt. Du känner dig maktfull.")

        if choice.lower() == "n" or choice.lower() == "no":
            print("Viggo kastar pappersflygplanet på Gustav! Han blir ledsen och går ut ur klassrummet. -1 liv")
        

        choice = input("Det är 30 minuter kvar av lektionen. Alla jobbar intensivt. Lyssnar du på dina tankar och skriker? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Alla stirrar på dig. Det tar en sekund, men Mohammad börjar garvskratta och sedan följer resten. Du känner dig rolig.")

        if choice.lower() == "n" or choice.lower() == "no":
            print("Ingenting händer, men du känner dig töntig som inte skrek. -1 liv")
        
        choice = input("Nu är lektionen snart slut! Låter du dina elever sluta 5 minuter tidigare? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Alla jublar och ler samtidigt som de reser sig upp för att gå! Du har klarat av sista fredagslektionen. Bra jobbat, Jens!")
            life_lost = input("Hur många liv förlorade du totalt? ")
            if life_lost == "0":
                print("Bra jobbat, du överlevde dagen! Du fick till och med en maraboukaka av Elvira.")
            if life_lost == "1":
                print("Kunde gjort bättre, men rektorn gav dig en stjärna för att ha avklarat dagen ändå.")
            if life_lost == "2":
                print("Det var nära gränsen, men du överlevde dagen!")
            if life_lost == "3":
                print("Dagen är över och du fick tomater kastade på dig av elever samt lärare. Dags att gråta dig själv till sömns.")
            if life_lost == "4":
                print("Hur lyckades du?")
            else:
                print("Du ljuger!")
            break
        
        if choice.lower() == "n" or choice.lower() == "no":
            print("Ingen är glad. Alvin har somnat och Alexander drog tidigt för att supa sig full. -1 liv")
            life_lost = input("Hur många liv förlorade du totalt? ")
            if life_lost == "0":
                print("Bra jobbat, du överlevde dagen! Du fick till och med en maraboukaka av Elvira.")
            if life_lost == "1":
                print("Kunde gjort bättre, men rektorn gav dig en stjärna för att ha avklarat dagen ändå.")
            if life_lost == "2":
                print("Det var nära gränsen, men du överlevde dagen!")
            if life_lost == "3":
                print("Dagen är över och du fick tomater kastade på dig av elever samt lärare. Dags att gråta dig själv till sömns.")
            if life_lost == "4":
                print("Hur lyckades du?")
            else:
                print("Du ljuger!")
            break

    else:
        print("Du är inte berättigad för att lära ut elarna.")
        break
        