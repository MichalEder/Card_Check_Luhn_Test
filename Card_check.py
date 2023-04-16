def prevrat(cislo_karty):
    return [x for x in cislo_karty[::-1]]

def suma_liche_pozice(cislo_karty_rev):
    return sum([int(cislo) for i, cislo in enumerate(karta_rev) if (i+1)%2])

