import random

# Lag en variabel som du kaller antall_sider. Be brukeren velge antall sider ved å bruke input()-funksjonen.
antall_sider = 6
### Her gjør vi om antall_sider fra å være en teksstreng til å være et heltall (fra sting til int)
#antall_sider = int(antall_sider)


def ikke_yahtzee():
    terning1 = random.randint(1,antall_sider)
    for i in range(0,4):
        kast = random.randint(1,antall_sider)
        if terning1 != kast:
            return True
    return False

# Lag en variabel antall_kast, som er lik 0
antall_kast = 0
while ikke_yahtzee():
    # Øk variabelen antall_kast med 1
    antall_kast += 1

print("Det tok " + str(antall_kast) + " kast før du fikk yatzy.")
print("Teoretisk er sannsynligheten for yahtzee " + str((1/antall_sider)**5))
