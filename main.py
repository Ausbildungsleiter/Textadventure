# https://www.helloworld.cc - Heft 1 - Seite 52
# Scary cave game -- Original Version CC BY-NC-SA 3.0
# Diese modifizierte Version (C) 2023 Roland Härter r.haerter@wut.de
Nirgendwo = None

raumbeschreibung = {
    'Küche': 'Du bist in der Küche. Diese scheint verlassen zu sein.',
    'Wohnzimmer':
    'Du befindest dich im Wohnzimmer. In einer Ecke steht eine alte Rüstung.',
    'Vorratskammer':
    'Du befindest dich in einer Speisekammer. Hier drin ist es kalt.',
    'Diele': 'Diele. Hier ist der Ausgang aus diesem Haus.'
}

erlaubte_befehle = ['w', 'a', 's', 'd', 'hilfe', 'beenden', 'karte zeichnen']

nach_norden = {
    'Küche': Nirgendwo,
    'Wohnzimmer': Nirgendwo,
    'Vorratskammer': 'Küche',
    'Diele': 'Wohnzimmer'
}
nach_süden = {
    'Küche': 'Vorratskammer',
    'Wohnzimmer': 'Diele',
    'Vorratskammer': Nirgendwo,
    'Diele': Nirgendwo
}
nach_osten = {
    'Küche': 'Wohnzimmer',
    'Wohnzimmer': Nirgendwo,
    'Vorratskammer': Nirgendwo,
    'Diele': Nirgendwo
}
nach_westen = {
    'Küche': Nirgendwo,
    'Wohnzimmer': 'Küche',
    'Vorratskammer': Nirgendwo,
    'Diele': Nirgendwo
}

compass = {
    'w': nach_norden,
    'a': nach_westen,
    's': nach_süden,
    'd': nach_osten,
}

def hilfe():
    print("\nZum Bewegen gibt es 'w' 'a' 's' und 'd'.")
    print("Es gibt folgende weitere Befehle: ")
    for befehlswort in erlaubte_befehle:
        if befehlswort in ['w', 'a', 's', 'd']:
            pass
        else:
            print(f"'{befehlswort}' ", end="")
    print("\n")


print('\n	*** Willkommen in Ravenswood Manor ***')
hilfe()

aktueller_raum = 'Küche'
vorheriger_raum = aktueller_raum
print(raumbeschreibung[aktueller_raum])
zielraum = 'Diele'

kommando = ''
while (aktueller_raum is not None):
    kommando = input('Was möchtest du tun? ').lower()
    while kommando not in erlaubte_befehle:
        kommando = input(
            'Dieses Kommando gibt es nicht. Was möchtest du tun? ').lower()
    if kommando == 'hilfe':
        hilfe()
    elif kommando == 'beenden':
        aktueller_raum = None
    elif kommando == 'karte zeichnen':
        import sys
        import generiere_karte
        generiere_karte.generiere_karte(sys.argv[0])
    elif compass[kommando][aktueller_raum] is not None:
        vorheriger_raum = aktueller_raum
        aktueller_raum = compass[kommando][aktueller_raum]
        if aktueller_raum == zielraum:
            print(raumbeschreibung[aktueller_raum])
            print('Du hast den letzten Raum gefunden. Das Spiel ist aus.')
            aktueller_raum = None
    else:
        print('Es gibt keinen Weg in diese Richtung. ', end='')
    if aktueller_raum != None:
        print(raumbeschreibung[aktueller_raum])
