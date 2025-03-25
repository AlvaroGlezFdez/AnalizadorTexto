# este script es simplemente para limpiar la consola rapidamente cuando queramos y dar una mejor experiencia de usuario

import os

def consola_clear():
    os.system('cls' if os.name == 'nt' else 'clear')