import json
import game

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
    game.Clear()
    return "{}, a te pontszámod {} és ezt eredményed elmentettük. 😁\n".format(dict["name"], score)
