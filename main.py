

kintamasis = 1
kintamasis2 = 2

def funkcija():
    print(kintamasis)
    print(kintamasis2)
    print(f'test:{kintamasis2}{kintamasis}')
    print('test:{}{}'.format({kintamasis2,kintamasis}))

# Funkcija sudeda du skaicius
def sudetis(pirmas, antras):
    return pirmas+antras
# Funkcija is pirmo atima antraji skaiciu
def atimtis(pirmas, antras):
    return pirmas-antras
# Funkcija daugina viena skaiciu is kito
def daugyba (pirmas, antras):
    return pirmas*antras
# Funkcija dalina viena skaiciu is kito
def dalyba(pirmas, antras):
    return pirmas/antras

print("Pasirinkite skaiciuotuvo operacija -\n" \
        "1. Sudetis\n" \
        "2. Atimtis\n" \
        "3. Daugyba\n" \
        "4. Dalyba\n")




