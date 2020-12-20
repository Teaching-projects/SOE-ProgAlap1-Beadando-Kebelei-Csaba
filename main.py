from moduls import game as GAME
from moduls import stat as STAT

def Main():
    """Egy egyszerű menüt vezérel. A terminál törlése után egy üdvözlő felirat jelenik meg, majd a menü, aminek 3 pontja van.
    Az első elindítja a Snake játékot. A második az eredményeket mutatja meg. A harmadik a szoftver futását szakítja meg,
    vagyis bezárja, majd törli a terminált mintha semmi sem történt volna. Egy "Menüpont: " után várja a megfelelő menüpontot.
    Ha nem 1-et, 2-őt vagy 3-at adunk meg, akkor arról "Ilyen menüpont nem létezik." tájékoztatást kapunk,
    amit a terminál törlése előz meg.
    """
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

#########
# START #
#########
Main()