def prevrat(cislo_karty):
    return [x for x in cislo_karty[::-1]]

def suma_liche_pozice(cislo_karty_rev):
    return sum([int(cislo) for i, cislo in enumerate(karta_rev) if (i+1)%2])

def suma_sude_pozice(cislo_karty):
    sude_pozice = [cislo for i, cislo in enumerate(karta_rev) if not (i+1)%2]
    nasobky = [str(int(nasobek)*2) for nasobek in sude_pozice]
    suma = 0
    for i in "".join(nasobky):
        suma += int(i)
    return suma 