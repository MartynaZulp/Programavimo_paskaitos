from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/skaicius")
def skaiciavimo():
    return "<p>Hello, World!</p>"

if __name__ == " __main__":
    app.run(debug=True)

'''

    pip install Flask
    pip3 install Flask

'''
'''# Funkcija sudeda du skaicius
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

select = ("taip")
while select == "taip":
    # Klausia ar vartotojas nori skaiciuoti toliau
    select = (input("Ar norite skaiciuoti toliau(taip/ne):"))
    
    print("Pasirinkite skaiciuotuvo operacija -\n" \
            "1. Sudetis\n" \
            "2. Atimtis\n" \
            "3. Daugyba\n" \
            "4. Dalyba\n")

    # Vartotojas iveda duomenis
    select = int(input("Pasirinkite operacijas: 1, 2, 3, 4 :"))
    
    pirmas = int(input("Iveskite pirmaji numeri: "))
    antras = int(input("Iveskite antraji numeri: "))
    
    if select == 1:
        print(pirmas, "+", antras, "=",
                        sudetis(pirmas, antras))
    
    elif select == 2:
        print(pirmas, "-", antras, "=",
                        atimtis(pirmas, antras))
    
    elif select == 3:
        print(pirmas, "*", antras, "=",
                        daugyba(pirmas, antras))
    
    elif select == 4:
        if antras == 0:
            print("Dalyba iš 0 negalima")
        else:
            print(pirmas, "/", antras, "=",
                        dalyba(pirmas, antras))
    else:
        print("Neteisinga ivestis")'''

