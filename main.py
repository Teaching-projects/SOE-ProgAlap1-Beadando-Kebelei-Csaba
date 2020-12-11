import pygame
import json

def Clear():
    import os
    try:
        os.system("clear")
    except:
        os.system("cls")

def GenGame():
    return {
        "width" : 800,
        "height" : 600,
        "run" : True,
        "score" : 0,
        "foodInMap" : False,
        "white" : (255, 255, 255),
        "black" : (0, 0, 0)
    }

def GenSnake():
    return {
        "size" : 20,
        "head" : {"x" : 300, "y" : 300},
        "body" : [],
        "moving" : {"x" : 20, "y" : 0}
    }

def Close(event):
    if event.type == pygame.QUIT: return False
    else: return True

def Keydown(event, size, mov):
    x = mov["x"]
    y = mov["y"]
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and (x != size and y != 0):
            x = -size
            y = 0
        elif event.key == pygame.K_RIGHT and (x != -size and y != 0):
            x = size
            y = 0
        elif event.key == pygame.K_UP and (x != 0 and y != size):
            x = 0
            y= -size
        elif event.key == pygame.K_DOWN and (x != 0 and y != -size):
            x = 0
            y = size
    return {"x" : x, "y" : y}

def Move(snake):
    snake["head"]["x"] += snake["moving"]["x"]
    snake["head"]["y"] += snake["moving"]["y"]

def GenCoordinates(length):
    coor = []
    for i in range(0, length, 20):
        coor.append(i)
    return coor

def GoodCoordinates(x, y, body):
    for i in body:
        if i["x"] == x and i["y"] == y: return False
    return True

def GenFood(x, y, body):
    import random

    randx = random.choice(x)
    randy = random.choice(y)
    while True:
        if GoodCoordinates(randx, randy, body): break
        randx = random.choice(x)
        randy = random.choice(y)

    return {"x" : randx, "y" : randy}
   
def FoodPrint(x, y, black, screen):
    font = pygame.font.Font('freesansbold.ttf', 20) 
    text = font.render("π", True, black)
    screen.blit(text, (x, y))

def Eat(head, food):
    if head["x"] == food["x"] and head["y"] == food["y"]: return True
    else: return False

def Body(snake, score):
    snake["body"].append({"x" : snake["head"]["x"], "y" : snake["head"]["y"]})
    if len(snake["body"]) > (score + 1):
        snake["body"].pop(0)

def PrintSnake(snake, game, screen):
    Body(snake, game["score"])
    
    for i in range(len(snake["body"])):
        x = snake["body"][i]["x"]
        y = snake["body"][i]["y"]
        pygame.draw.rect(screen, game["black"],[x,y,20,20])

def Wall(head, width, height, size):
    if head["x"] == width or head["x"] == -size or head["y"] == height or head["y"] == -size: return True
    
def SnakeInSnake(body, head):
    for i in range(len(body)-1):
        if body[i]["x"] == head["x"] and body[i]["y"] == head["y"]: return True
    return False

def Death(snake, width, height):
    if Wall(snake["head"], width, height, snake["size"]) or SnakeInSnake(snake["body"], snake["head"]): return True

def Datetime():
    import datetime
    date = datetime.datetime.now()
    return "{}-{}-{}".format(date.year, date.strftime("%m"), date.strftime("%d"))

def Nickname():
    return input("Nickname: ")

def Load(fileName):
    try:
        infile = open(fileName, "r")
        fileList = json.load(infile)
        infile.close()
    except:
        fileList = []
    return fileList

def Save(score, fName):
    dict = {
        "name" : Nickname(),
        "date" : Datetime(),
        "score" : score
    }

    saveList = Load(fName)

    saveList.append(dict)

    statFile = open(fName, "wt")
    json.dump(saveList, statFile)

    statFile.close()
    Clear()
    return "{}, az eredményed elmentettük. 😁\n".format(dict["name"])

def SnakeGame():
    import pygame
    pygame.init()

    Clear()

    game = GenGame()
    snake = GenSnake()

    screen = pygame.display.set_mode([game["width"], game["height"]])
    pygame.display.set_caption('Snake game by Csabi')
    clock = pygame.time.Clock()

    while game["run"]:
        for event in pygame.event.get():
            game["run"] = Close(event)
            snake["moving"] = Keydown(event, snake["size"], snake["moving"])
        if Death(snake, game["width"], game["height"]): game["run"] = False
        
        Move(snake)

        screen.fill(game["white"])

        PrintSnake(snake, game, screen)

        if game["foodInMap"] == False:
            food = GenFood(GenCoordinates(game["width"]), GenCoordinates(game["height"]), snake["body"])
            game["foodInMap"] = True
        if Eat(snake["head"], food):
            game["score"] += 1
            game["foodInMap"] = False

        FoodPrint(food["x"], food["y"], game["black"], screen)    

        pygame.display.update()
        
        clock.tick(10)

    pygame.quit()

    return Save(game["score"], "stat.json")

def Stat():
    Clear()
    print("Hello, World!\n")

def Main():
    Clear()
    inp = 0
    print("Üdvözöllek a Snake játékban!\n")
    while inp != 3:
        print("[1] Snake játék indítása 🐍")
        print("[2] Statisztika megnézése 🏆")
        print("[3] Kilépés a játékból ❌")
        inp = int(input("Menüpont: "))
        if inp == 1: print(SnakeGame())
        elif inp == 2: Stat()
    Clear()

##########
#  TEST  #
##########

Main()
