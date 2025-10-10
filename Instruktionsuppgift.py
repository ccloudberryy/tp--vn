#Instruktionsuppgift
from time import sleep
import random

DELAY = 0.5
longdelay = 3

name = input("Vad heter du? ")
life = 4
demon = 20

sen = 0
bajs = 0
tänder = 0
monster = 0
droger = 0
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
        print("[Emils tale börjar, och DU styr den!]")
        sleep(DELAY)
        print("...")
        sleep(DELAY)
        print("Emil gäspar och stiger upp ur sängen.")
        sleep(longdelay)
        choice = input("Han kollar sig själv i spegeln och märker att han inte har borstat sina tänder än. Borstar han sina tänder? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Han går in till badrummet och borstar sina tänder.")
        if choice.lower() == "n" or choice.lower() == "no":
            print("Emil tänker efter lite, men bestämmer sig för att inte borsta sina tänder. Han orkar inte.")
            tänder += 1
            # OBORSTADE TÄNDER = 1
        sleep(longdelay)
        print("Emil sätter på sig sina kläder och ska nu ta sig till skolan.")
        sleep(longdelay)
        choice = input("Han känner sig fortfarande trött i kroppen. Ska Emil ta bussen? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Han går till sin busshållplats och väntar 5 minuter tills den äntligen kommer.")
            sleep(longdelay)
            choice = input("Han stiger på bussen. Försöker han undvika att betala sin bussbiljett? [Y]es/[N]o: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Han försöker smita sig på bussen, men busschauffören skriker och kickar ut honom.")
                sleep(longdelay)
                print("Han väntar 15 minuter på nästa buss och betalar sin bussbiljett den här gången.")
                sen += 1
                # SEN TILL SKOLAN
            if choice.lower() == "n" or choice.lower() == "no":
                print("Han stiger på bussen och betalar sin bussbiljett.")
                sleep(longdelay)
                print("Busschauffören ger Emil en sne blick som om han kunde läsa Emil tankar.")    
        if choice.lower() == "n" or choice.lower() == "no":
            print("Han tar på sig sina skor och börjar promenera till skolan.")
            sleep(longdelay)
            choice = input("Emil märker inte det, men det ligger hundbajs framför honom. Du bestämmer, ska han gå i det? [Y]es/[N]o: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Han går i hundbajset. Han märker att sina skor är kladdiga och tar en titt.")
                sleep(longdelay)
                print('"EWWW!!" skriker han. Han står en stund i tystnad men fortsätter gå. Han har en lektion att ta sig till.')
                bajs += 1
                # BAJS PÅ SKORNA
            if choice.lower() == "n" or choice.lower() == "no":
                print("Han märker hundbajset på sista sekunden och undviker det.")
                sleep(longdelay)
                print("Han låter ut ett ljud av lättnad. Han fortsätter promenera till skolan.")
        sleep(longdelay)
        print("Nu är han framme vid skolan. Han går in och ser sin vän Isak Engman.")
        sleep(longdelay)
        choice = input("De går in i hissen tillsammans. Skriker dem? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print('De skriker högt "HJÄLP!!! HJÄÄÄLP!!!". När de stiger ut ur hissen märker de att Eszter står precis utanför.')
            sleep(longdelay)
            print('Eszter säger till dem på skarpen.')
        if choice.lower() == "n" or choice.lower() == "no":
            print("Ovanligt beteende för Emil. Han skriker inte i hissen.")
            sleep(longdelay)
            choice = input("Tar Emil på Isaks bröst istället? [Y]es/[N]o: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Isak stönar högt medan hissen är påväg upp.")
                sleep(longdelay)
                print("När hissdörren öppnas så märker de att Eszter står precis utanför.")
                sleep(longdelay)
                print("Hon säger till dem båda på skarpen, även om Emil försökte säga att det bara var Isak.")
            if choice.lower() == "n" or choice.lower() == "no":
                print("Ingenting sker.")
                sleep(longdelay)
                print("När hissdörren öppnas så lättnar Emil då han ser Eszter precis utanför. Bra att han inte gjorde något.")
        sleep(longdelay)
        print("Emil tar av sig sina skor och går till sin lektion i Aristoteles.")
        sleep(longdelay)
        if sen == 1:
            print("Mattias kollar på Emil.")
            sleep(longdelay)
            print('"Du är sen. Sätt dig ner och börja jobba med din jävla server. 67."')
            sleep(longdelay)
            choice = input("Emil ser Elvira. Skriker han slurs mot henne? [Y]es/[N]o: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Elvira kollar på Emil med ett half-assed leende.")
                sleep(longdelay)
                choice = input('Mattias blir sur. "Vill du ha en kränkningsanmälen eller?" säger han. Vill Emil det? [Y]es/[N]o: ')
                if choice.lower() == "y" or choice.lower() == "yes":
                    print('"Ja! Anmäl mig!" säger Emil. "Haha am i mutted?"')
                    sleep(longdelay)
                    print('"Då anmäler jag dig", säger Elvira skämtsamt.')
                if choice.lower() == "n" or choice.lower() == "no":
                    print('"Nej, no sir!" säger Emil. Mattias glor på Emil och hintar på att han ska sätta sig ner.')
                    sleep(longdelay)
                    print('"Jag önskar jag hade en redbull just nu..." sa Mattias till sig själv tyst.')
            if choice.lower() == "n" or choice.lower() == "no":
                print("Emil sätter sig ner och börjar jobba på sin server. Elvira känner sig överraskad.")
        if sen == 0:
            print('"Wow, du är på tid! Bra jobbat! 67." säger Mattias.')
            sleep(longdelay)
            print('"Sätt dig ner och börja jobba med din förjävlade server innan jag köper mig själv en redbull." fortsätter han.')
        sleep(longdelay)
        print("Emil jobbar hårt med sin förbaskade server. Han märker att klockan börjar närma sig rast.")
        sleep(longdelay)
        print('"Mattias, får vi sluta tidigare? Snälla?" Mattias tittar på han.')
        sleep(longdelay)
        choice = input("Frästar Emil honom med en redbull som han har i sin väska? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print('Mattias suckar. "Ge mig den och stick ut innan jag ändrar mig."')
            sleep(longdelay)
            print("Emil springer ut ur klassrummet och sätter sig i Helios, utanför det nybyggda biblioteket.")
        if choice.lower() == "n" or choice.lower() == "no":
            print('Mattias suckar. "Nej, det får ni inte. Forstätt jobba med din server."')
            sleep(longdelay)
            print('"Jag bryr mig inte om du är klar", säger han.')
            sleep(longdelay)
            print('"Jag kan lägga ut en till uppgift åt dig om du vill?", fortsätter han.')
            sleep(longdelay)
            print('"Nej tack. Jag väntar bara. 67." säger Emil.')
            sleep(longdelay)
            print("Emil stirrar på sin dator i 10 minuter tills det äntligen blir rast.")
            sleep(longdelay)
            print("Emil springer ut ur klassrummet och sätter sig i Helios, utanför det nybyggda biblioteket.")
        sleep(longdelay)
        print("Både Wilmer och Emil sätter sig ner på soffan.")
        sleep(longdelay)
        print('"Ska vi dra på Coop? Coop rushen kallar. 67." säger Emil.')
        sleep(longdelay)
        if tänder == 1:
            print('"Helvete!" Wilmer täcker för sin näsa.')
            sleep(DELAY)
            print("...")
            sleep(longdelay)
            print('"Borstade du inte dina tänder imorse? Din andedräkt stinker som fan!"')
            sleep(longdelay)
            print('"Nah jag orkade inte, men kan vi dra på Coop jag är skithungrig? 67." svarar Emil.')
            sleep(longdelay)
            print('"Jaja, nu drar vi." säger Wilmer. Resten av elarna följer med också.')
        if tänder == 0:
            print('"Ja, men jag måste bara säga, Emil. Dina tänder är ovanligt rena."')
            sleep(longdelay)
            print('"Borstade du dem för första gången den här veckan eller?", skrattade Wilmer.')
            sleep(longdelay)
            print('"Käften! Jag borstar varje dag!". Emil ljuger rakt igenom sina tänder.')
            sleep(longdelay)
            print('"Jaja, vad du än säger. Nu drar vi." säger Wilmer. Resten av elarna följer med också.')
        sleep(longdelay)
        print("*Queue slur-slinging musik*")
        sleep(longdelay)
        choice = input("Nu är de äntligen framme! Emil kan inte bestämma sig mellan en vit monster eller en munk. Väljer han monstern? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Emil tittar på sina val, men väljer i slutändan den vita monstern.")
            monster += 1
        if choice.lower() == "n" or choice.lower() == "no":
            print("Emil tittar på sina val, men väljer i slutändan munken.")
            sleep(longdelay)
            print('"Rub my belly!" skriker någon i bakgrunden. Det var Elvira.')
            sleep(DELAY)
            print("...")
            sleep(longdelay)
            print("Emil känner sig tjock.")
        sleep(longdelay)
        print("Elarna promenerar tillbaka till skolan med sina köpta varor.")
        sleep(longdelay)
        choice = input("De andra elarna tar hissen. Tar Emil också hissen upp? [Y]es/[N]o: ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("Emil går in i hissen med de andra elarna. ")
            sleep(longdelay)
            print("Plötsligt hör de ett krak i hissen. Vad pågår?")
            sleep(longdelay)
            print("Hissen bryts. Lampan börjar blinka.")
            sleep(longdelay)
            print("Plötsligt blev allting svart.")
            sleep(longdelay)
            print("För många elare var i hissen samtidigt. Kabeln bröt. Du dog tillsammans med de andra elarna.")
            sleep(longdelay)
            print("[HISS ENDING]")
            sleep(longdelay)
            #hiss ending
        if choice.lower() == "n" or choice.lower() == "no":
            print("Emil hör massa stönande och skrik i hissen medan han går upp för trapporna.")
            sleep(longdelay)
            choice = input("Trycker han på knappen på 1:a våningen? [Y]es/[N]o: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Emil trycker på knappen. Han går upp till andra våningen och hör en massa slur-slinging:")
                sleep(longdelay)
                print('"Jävla b*g! F*ggot! Tr*nny!" hör han samtidigt som han går in till skolan.')
            if choice.lower() == "n" or choice.lower() == "no":
                print("Emil springer upp för trapporna och går in i skolan innan hissen är på andra våningen.")
        sleep(longdelay)
        print("Emil sätter sig i Helios. De andra elarna sätter sig runt bordet.")
        sleep(longdelay)
        if bajs == 1:
            print('"Asså, det var hundskit på golvet över hela trappan."')
            sleep(DELAY)
            print("...")
            sleep(longdelay)
            print("Emil kollar under sin sko framför de andra. Det är fan från tidigare!")
            sleep(longdelay)
            print("Alla skrattar och hånar Emil.")
            sleep(longdelay)
            choice = input("Kastar Emil skon på Gustav? [Y]es/[N]o: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Emil kollar upp och ner från sin sko och kastar den snabbt på Gustav.")
                sleep(longdelay)
                print('"VAFAN! JAG KOMMER SÄGA TILL SARA! JÄVLA VIDER DU ÄR, EMIL!" skriker Gustav')
                sleep(longdelay)
                print("Efter en stund så kommer Sara och skäller ut Emil. Han blir skickad hem och avstängd från skolan.")
                sleep(longdelay)
                print("[HUNDSKIT ENDING]")
                sleep(longdelay)
                #hundskit ending
            if choice.lower() == "n" or choice.lower() == "no":
                print("Emil kollar upp och ner från sin sko, men bestämmer sig för att hålla tillbaka sin ilska.")
                sleep(longdelay)
                print("Han går vidare med sitt liv, även om han kommer bli hånad för resten av månaden.")
        if bajs == 0:
            print("Elarna skrattar och har kul i Helios tills nästa lektion börjar. De går dit och jobbar med sina servrar.")
        sleep(longdelay)
        print("Efter vad som kändes som en lång jävla lektion är det äntligen lunch.")
        sleep(longdelay)
        print("Emil går till lunchen tillsammans med sina polare.")
        sleep(longdelay)
        choice = input("Det är nattbakad fläskkarre till lunch. Hoppar Emil av lunchen? [Y]es/[N]o:")
        if choice.lower() == "y" or choice.lower() == "yes":
            print('"Ehhh asså vet du vad grabbar, jag hoppar av lunchen" säger Emil.')
            sleep(DELAY)
            print("...")
            sleep(longdelay)
            choice = input('"Ska vi ta droger tillsammans? Det kallar mig." frågar Zander. [Y]es/[N]o: ')
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Emil och elarna går tillbaka till skolan och in på handikappstoan.")
                sleep(longdelay)
                print("De tar ett djupt andetag. Emil känner sig borta.")
                sleep(longdelay)
                droger += 1
                choice = input("Ska Emil ta en till hit? [Y]es/[N]o: ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    print("Emil tar en till hit.")
                    sleep(longdelay)
                    print('"Näe asså jag ser formerna nu grabbar", säger Emil.')
                    sleep(longdelay)
                    print("Du har tappat kontroll över Emil. Han tog för många hits. Sätt dig bak och kolla på.")
                    droger += 1
                if choice.lower() == "n" or choice.lower() == "no":
                    print('"Jag slutar här. Annars kommer Mattias komma på mig nästa lektion.", stammar Emil.')
            if choice.lower() == "n" or choice.lower() == "no":
                print("Emil tackar nej till förslaget.")
                sleep(longdelay)
                print('"Vi kommer vara för borta under nästa lektion", säger Emil.')
                sleep(longdelay)
                print("De går vingligt till nästa lektion.")
        if choice.lower() == "n" or choice.lower() == "no":
            print("Emil ställer sig i kön, plockar på mat och käkar tillsammans med de andra elarna. De har kul.")
            sleep(longdelay)
            print("De vandrar tillbaka till skolan, in i lektionen. Nästa lektion börjar.")
            sleep(longdelay)
        print("Mattias sätter upp projektorn. Han ser sina elever komma in till Aristoteles.")
        sleep(longdelay)
        if droger == 0:
            print('"Hej! Välkommen tillbaka. Sätt er ner och studera för fan." beordrar Mattias.')
            sleep(longdelay)
            print("Emil sätter sig ner och studerar.")
            sleep(DELAY)
            print("...")
            sleep(longdelay)
            print("Överraskande, så händer ingenting under hela förmiddagen.")
            sleep(longdelay)
            print("Emil säger hejdå till sina vänner och går hem.")
            sleep(longdelay)
            print("[GOOD ENDING]")
            sleep(longdelay)
            #good ending
        if droger == 1:
            print("Mattias kollar lite snett på sina elever.")
            sleep(longdelay)
            print("Han tar en närmare titt på deras ögon. De är lite röda.")
            sleep(longdelay)
            print('"Jag vet inte vad som har hänt, men det är inte mitt ansvar." säger Mattias.')
            sleep(longdelay)
            print('Mattias fortsätter: "Sätt er ner och jobba, annars åker ni fan dit.", instämmer han')
            sleep(longdelay)
            choice = input("Jobbar Emil? [Y]es/[N]o:")
            if choice.lower() == "y" or choice.lower() == "yes":
                print("Emil öppnar sin laptop. Texten är suddig, det är svårt att jobba.")
                sleep(DELAY)
                print("...")
                sleep(longdelay)
                print("Han gör sitt bästa, men blir bara halvvägs klar med sin uppgift.")
                sleep(longdelay)
                print('"Mattias, jag är fan inte klar. Jag fortsätter hemma." säger Emil, samtidigt som han packar upp sina saker.')
                sleep(longdelay)
                print('Mattias suckar. "Så länge det blir klart inom de närmaste månaderna får du göra hur du än vill.", svarar han.')
                sleep(longdelay)
                print("Emil säger hejdå till sina vänner och drar hem.")
                sleep(longdelay)
                print("[HEMLÄXA ENDING]")
                sleep(longdelay)
                #hemläxa ending
            if choice.lower() == "n" or choice.lower() == "no":
                print("Emil öppnar sin laptop. Texten är suddig. Han väljer att inte jobba.")
                sleep(DELAY)
                print("...")
                sleep(longdelay)
                print("Lektionen börjar närma sitt slut.")
                sleep(longdelay)
                print('"Hur långt har ni kommit? 67", frågar Mattias.')
                sleep(longdelay)
                print("Emil säger att han är klar, så Mattias tar en titt.")
                sleep(longdelay)
                print('"Jävla tegare! Du har fan inte ens rört uppgiften!", skriker Mattias.')
                sleep(longdelay)
                print("Emil, borta som fan, skriker tillbaka. Han blir utkastad från klassrummet.")
                sleep(longdelay)
                choice = input("Väntar Emil på sina vänner innan han åker hem? [Y]es/[N]o:")
                if choice.lower() == "y" or choice.lower() == "yes":
                    print("Emil väntar tålmodigt på att hans vänner ska gå ut från Aristoteles.")
                    sleep(longdelay)
                    print("Emil säger hejdå till sina vänner och drar hem.")
                    sleep(longdelay)
                    print("[NEUTRAL ENDING, och han behåller sina vänner!]")
                    sleep(longdelay)
                    #neutral ending
                if choice.lower() == "n" or choice.lower() == "no":
                    print("Emil sticker hem på direkten. Han har haft nog.")
                    sleep(longdelay)
                    print("[NEUTRAL ENDING, och han förlorar sina vänner!]")
                    sleep(longdelay)
                    #neutral ending
        if droger == 2:
            print("Mattias stirrar ner sina elever.")
            sleep(longdelay)
            print('"Ut med er." säger han på direkten.')
            sleep(longdelay)
            if monster == 1:
                print('"FUCK THAT! TR*NNY!" säger Emil och kastar sin nyköpta monster på Mattias.')
            if monster == 0:
                print('"FUCK THAT! TR*NNY!" säger Emil och kastar en stol på Mattias.')
            sleep(longdelay)
            print('"VAFAN EMIL DIN JÄVLA TEGBO!! STICK HEM!! DU KOMMER FAN BLI ANMÄLD DITT JÄVLA SVIN", skriker Mattias tillbaka.')
            sleep(longdelay)
            print('"JAG BRYR MIG FAN INTE, FUCK YOU OCH DINA UPPGIFTER!", svarar Emil med en högd röst.')
            sleep(longdelay)
            print("Emil springer ut ur klassrummet, springer ut från skolan och drar hem.")
            sleep(longdelay)
            print("Kvällen den dagen blir han utskälld av sina föräldrar.")
            sleep(longdelay)
            print("Emil får utegångsförbud och förlorar sina alkoholpengar för resten av året, och det är bara februari!")
            sleep(longdelay)
            print("[BAD ENDING]")  
            sleep(longdelay)
            #bad ending
        print("Alla endings:")
        print("     [HISS ENDING]")
        print("     [HUNDSKIT ENDING]")
        print("     [HEMLÄXA ENDING]")
        print("     [BAD ENDING]")
        print("     [NEUTRAL ENDING, och han förlorar sina vänner!]")
        print("     [NEUTRAL ENDING, och han behåller sina vänner!]")
        print("     [GOOD ENDING]")
        break

    else:
        print("Du finns inte i mitt register. Hejdå.")
        break
        