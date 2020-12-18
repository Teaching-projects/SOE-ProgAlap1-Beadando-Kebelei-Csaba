import json
from moduls import game as GAME

def Datetime() -> str:
    """A függvény képes az éppeni dátum formázott megjelenítésére: év-hónap-nap.

    Returns:
        str: év-hónap-nap karakterlánc.
    """
    import datetime
    date = datetime.datetime.now()
    return "{}-{}-{}".format(date.year, date.strftime("%m"), date.strftime("%d"))

def Load(fileName:str) -> list:
    """Betölti a fájlban lévő adatokat.

    Args:
        fileName (str): A fájl neve.

    Returns:
        list: Ha a fájlban van adat akkor azzal tér vissze, különben egy üres listával.
    """
    try:
        infile = open(fileName, "r")
        fileList = json.load(infile)
        infile.close()
    except:
        fileList = []
    return fileList

def Save(score:int, fName:str, nickname:str) -> str:
    """Egy fájlba kiírja egy az eddigi eredmények és a most elért eredmény tartalmát, 
    vagyis a nickname-et, dátumot és pontszámot.

    Args:
        score (int): A pontszám, amit a játék során elértünk.
        fName (str): A fájl neve, ahova kíirjuk az adatokat.
        nickname (str): A játékos által megadott nickname.

    Returns:
        str: Egy személyre szóló visszajelzés, hogy elmentettük az eredményt.
    """
    dict = {
        "name" : nickname,
        "date" : Datetime(),
        "score" : score
    }

    saveList = Load(fName)

    saveList.append(dict)

    statFile = open(fName, "wt")
    json.dump(saveList, statFile)

    statFile.close()
    GAME.Clear()
    return "{}, a te pontszámod {} és ezt az eredményed elmentettük. 😁\n".format(dict["name"], score)
