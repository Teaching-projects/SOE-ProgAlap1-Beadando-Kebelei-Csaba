from moduls import game as GAME
from moduls import stat as STAT

def Main():
    GAME.Clear()
    inp = 0
    print("Üdvözöllek a Snake játékban!\n")
    while inp != 3:
        print("[1] Snake játék indítása 🐍")
        print("[2] Eredmények megnézése 🏆")
        print("[3] Kilépés a játékból ❌")
        inp = input("Menüpont: ")
        if inp in "123":
            inp = int(inp)
            if inp == 1: print(GAME.SnakeGame())
            elif inp == 2: STAT.Stat()
        else:
            GAME.Clear()
            print("Ilyen menüpont nem létezik.\n")
    GAME.Clear()

Main()
