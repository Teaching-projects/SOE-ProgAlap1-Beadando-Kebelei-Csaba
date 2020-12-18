from moduls import game as GAME
from moduls import file as FILE


def Place(statlist):
    returnList = []
    for i in statlist:
        returnList.append(i["score"])
    returnList = list(set(returnList))
    return sorted(returnList, reverse=True)[:3]

def Winners(statlist):
    places = Place(statlist[:])
    returnList = []
    emojiList = ["🥇", "🥈", "🥉"]
    for i in range(len(places)):
        for j in range(len(statlist)):
            if places[i] == statlist[j]["score"]:
                statlist[j]["place"] = emojiList[i]
                returnList.append(statlist[j])
    return returnList

def Stat():
    GAME.Clear()
    list = Winners(FILE.Load("stat.json")[:])
    print("{:<16} {:<17} {:<17} {:<17}".format("Eredmény", "Nickname", "Dátum", "Pontszám"))
    if len(list) == 0:
        print("Nincs adatunk... Még játszani kell. 😉")
    else:
        for i in list:
            print("{:<15} {:<17} {:<17} {:<17}".format("{:^8}".format(i["place"]), i["name"], i["date"], i["score"]))
    print()
