from moduls import game as GAME
from moduls import file as FILE

def Place(statlist:list) -> list:
    """A legjobb pontszámokat adja vissza.

    Args:
        statlist (list): Lista, ami az eredményeket tárolja.

    Returns:
        list: Lista, ahol az első három legjobb eredmény pontszáma van benne csökkenő sorrendben.
    """
    returnList = []
    for i in statlist:
        returnList.append(i["score"])
    returnList = list(set(returnList))
    return sorted(returnList, reverse=True)[:3]

def Winners(statlist:list) -> list:
    """A legjobb 3 eredményt, illetve a holtversenyt adja vissza a helyezés emojival.

    Args:
        statlist (list): Lista, ami az eredményeket tárolja.

    Returns:
        list: A legjobb eredmények csökkenő sorrendben a megfelelő helyezést jelentő emojival. 
    """
    places = Place(statlist[:])
    returnList = []
    emojiList = ["🥇", "🥈", "🥉"]
    for i in range(len(places)):
        for j in range(len(statlist)):
            if places[i] == statlist[j]["score"]:
                returnList.append(
                    {
                        "name" : statlist[j]["name"],
                        "date" : statlist[j]["date"],
                        "score" : statlist[j]["score"],
                        "place" : emojiList[i]
                    }
                )
    return returnList

def Stat():
    """A függvény törli a terminál eddigi tartalmát, majd megjeleníti egy eredménytáblában a legjobb eredményeket.
    Ha nincs eredmény, vagyis az eredmények listája üres, akkor arról külön tájékoztatást jelenít meg a függvény.
    """
    GAME.Clear()
    list = Winners(FILE.Load("stat.json")[:])
    print("{:<16} {:<17} {:<17} {:<17}".format("Eredmény", "Nickname", "Dátum", "Pontszám"))
    if len(list) == 0:
        print("Nincs adatunk... Még játszani kell. 😉")
    else:
        for i in list:
            print("{:<15} {:<17} {:<17} {:<17}".format("{:^8}".format(i["place"]), i["name"], i["date"], i["score"]))
    print()
