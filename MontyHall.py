import random

#Oppretter nytt tilfeldig spill
dor1 = "geit"
dor2 = "geit"
dor3 = "geit"

a = random.randint(1,3)

if a == 1:
    dor1 = "bil"
elif a == 2:
    dor2 = "bil"
else:
    dor3 = "bil"




#Bruker velger d�r
print("Velkommen til game showet Bil eller Geit")
valg = input("Nytt spill: Velg en d�r: 1,2 eller 3. Trykk enter for � avslutte\n")

while valg != "":
    if valg == "1":
        #Spiller velger d�r 1
        if dor1 == "bil":
            b = random.randint(1,2)
            if b == 1:
                nyttValg = input("Bak d�r 2 er det en geit, vil du bytte til d�r 3 eller beholde d�r 1(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("TAP: Du fikk en geit  :( ")
                else:
                    print("SEIER: Du vant en bil :D")
            else:
                nyttValg = input("Bak d�r 3 er det en geit, vil du bytte til d�r 2 eller beholde d�r 1(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("TAP: Du fikk en geit  :( ")
                else:
                    print("SEIER: Du vant en bil :D")
        else:
            if dor2 == "geit":
                nyttValg = input("Bak d�r 2 er det en geit, vil du bytte til d�r 3 eller beholde d�r 1(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("SEIER: Du vant en bil :D")
                else:
                    print("TAP: Du fikk en geit  :( ")
            else:
                nyttValg = input("Bak d�r 3 er det en geit, vil du bytte til d�r 2 eller beholde d�r 1(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("SEIER: Du vant en bil :D")
                else:
                    print("TAP: Du fikk en geit  :( ")

    elif valg == "2":
        if dor1 == "bil":
            b = random.randint(1,2)
            if b == 1:
                nyttValg = input("Bak d�r 1 er det en geit, vil du bytte til d�r 3 eller beholde d�r 2(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("TAP: Du fikk en geit  :( ")
                else:
                    print("SEIER: Du vant en bil :D")
            else:
                nyttValg = input("Bak d�r 3 er det en geit, vil du bytte til d�r 1 eller beholde d�r 2(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("TAP: Du fikk en geit  :( ")
                else:
                    print("SEIER: Du vant en bil :D")
        else:
            if dor1 == "geit":
                nyttValg = input("Bak d�r 1 er det en geit, vil du bytte til d�r 3 eller beholde d�r 2(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("SEIER: Du vant en bil :D")
                else:
                    print("TAP: Du fikk en geit  :( ")
            else:
                nyttValg = input("Bak d�r 3 er det en geit, vil du bytte til d�r 1 eller beholde d�r 2(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("SEIER: Du vant en bil :D")
                else:
                    print("TAP: Du fikk en geit  :( ")

    elif valg == "3":
        if dor3 == "bil":
            b = random.randint(1,2)
            if b == 1:
                nyttValg = input("Bak d�r 1 er det en geit, vil du bytte til d�r 2 eller beholde d�r 3(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("TAP: Du fikk en geit  :( ")
                else:
                    print("SEIER: Du vant en bil :D")
            else:
                nyttValg = input("Bak d�r 2 er det en geit, vil du bytte til d�r 1 eller beholde d�r 3(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("TAP: Du fikk en geit  :( ")
                else:
                    print("SEIER: Du vant en bil :D")
        else:
            if dor2 == "geit":
                nyttValg = input("Bak d�r 2 er det en geit, vil du bytte til d�r 1 eller beholde d�r 3(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("SEIER: Du vant en bil :D")
                else:
                    print("TAP: Du fikk en geit  :( ")
            else:
                nyttValg = input("Bak d�r 1 er det en geit, vil du bytte til d�r 2 eller beholde d�r 3(skriv: bytte eller beholde)\n")
                if nyttValg.lower() == "bytte":
                    print("SEIER: Du vant en bil :D")
                else:
                    print("TAP: Du fikk en geit  :( ")
    else:
        print("Ugyldig input, du m� skrive 1, 2 eller 3")

    dor1 = "geit"
    dor2 = "geit"
    dor3 = "geit"

    a = random.randint(1,3)

    if a == 1:
        dor1 = "bil"
    elif a == 2:
        dor2 = "bil"
    else:
        dor3 = "bil"

    valg = input("Nytt spill: Velg en d�r: 1,2 eller 3. Trykk enter for � avslutte\n")
