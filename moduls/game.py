import pygame
from moduls import file as FILE

def Clear():
    """
        Terminál törlését, tisztítását végzi el a függvény.
        Linux-on, Mac-en egyaránt működik.
    """
    import os
    try:
        os.system("clear")
    except:
        os.system("cls")

def GenGame() -> dict:
    """
        A függvény létrehoz egy game dictionary-t.

        width (int): Pálya hosszusága.
        height (int): Pálya magassága.
        run (bool): Megadja, hogy fut-e a játék.
        score (int): A játék éppen pontszáma.
        foodInMap (bool): Megadja, hogy van-e kaja generálva a pályára. 
        white: Fehér szín rgb kódja.
        black: Fekete szín rgb kódja.
    """
    return {
        "width" : 800,     
        "height" : 600,
        "run" : True,
        "score" : 0,
        "foodInMap" : False,
        "white" : (255, 255, 255),
        "black" : (0, 0, 0)
    }

def GenSnake() -> dict:
    """
        A függvény létrehoz egy snake dictionary-t.

        size (int): A kígyó méretes.
        head (dict): Itt tárolódik a kígyó fejének az x és y koordinátája.
        body (list): Itt tárolódik a kígyó testének minden darabjának a x és y koordinátája.
        moving (dict): A kígyó irányát adja meg x és y koordinátákkal.
    """
    return {
        "size" : 20,
        "head" : {"x" : 300, "y" : 300},
        "body" : [],
        "moving" : {"x" : 20, "y" : 0}
    }

def Close(event) -> bool:
    """
    A függvény True értékkel tér vissza, ha a pygame ablakot bezárjuk és False értékkel ha nem történt semmi.
    """
    if event.type == pygame.QUIT: return False
    return True

def Keydown(event, size:int, mov:dict) -> dict:
    """

    """
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

def Move(snake: dict):
    snake["head"]["x"] += snake["moving"]["x"]
    snake["head"]["y"] += snake["moving"]["y"]

def GenCoordinates(length:int) -> list:
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

def Nickname():
    name = ""
    while True:
        name = input("Nickname: ")
        if len(name) < 17: break
        print("Túl hosszú nickname! (16 karakternél ne legyen hosszabb)")
    Clear()
    if set(name) == {" "} or len(name) == 0: return "Anonim" 
    return name


def SnakeGame():
    pygame.init()

    Clear()

    name = Nickname()

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

    return FILE.Save(game["score"], "stat.json", name)