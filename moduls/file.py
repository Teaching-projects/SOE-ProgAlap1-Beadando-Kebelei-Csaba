import json
from moduls import game as GAME

def Datetime():
    import datetime
    date = datetime.datetime.now()
    return "{}-{}-{}".format(date.year, date.strftime("%m"), date.strftime("%d"))

def Load(fileName):
    try:
        infile = open(fileName, "r")
        fileList = json.load(infile)
        infile.close()
    except:
        fileList = []
    return fileList

def Save(score, fName, nickname):
    dict = {
        "name" : nickname,
        "date" : Datetime(),
        "score" : score,
        "place" : ""
    }

    saveList = Load(fName)

    saveList.append(dict)

    statFile = open(fName, "wt")
    json.dump(saveList, statFile)

    statFile.close()
    GAME.Clear()
    return "{}, a te pontszámod {} és ezt az eredményed elmentettük. 😁\n".format(dict["name"], score)
