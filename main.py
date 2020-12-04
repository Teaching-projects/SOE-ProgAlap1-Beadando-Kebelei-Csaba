import pygame

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
        "foodInMap" : False
    }

def GenSnake():
    return {
        "size" : 20,
        "head" : {"x" : 300, "y" : 300},
        "body" : [],
        "moving" : {"x" : 20, "y" : 0}
    }

def Close():
    if event.type == pygame.QUIT: game["run"] = False 

def Keydown(size, mov):
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

def Move(mov):
    snake["head"]["x"] += mov["x"]
    snake["head"]["y"] += mov["y"]

def GenCoordinates(length):
    coor = []
    for i in range(0, length, 20):
        coor.append(i)
    return coor

def GoodCoordinates(x, y):
    for i in snake["body"]:
        if i["x"] == x and i["y"] == y: return False
    return True

def GenFood():
    import random
    x = GenCoordinates(game["width"])
    y = GenCoordinates(game["height"])

    randx = random.choice(x)
    randy = random.choice(y)
    while True:
        if GoodCoordinates(randx, randy): break
        randx = random.choice(x)
        randy = random.choice(y)

    return {"x" : randx, "y" : randy}
   
def FoodPrint(x, y):
    font = pygame.font.Font('freesansbold.ttf', 20) 
    text = font.render("π", True, black)
    screen.blit(text, (x, y))

def Eat():
    if snake["head"]["x"] == food["x"] and snake["head"]["y"] == food["y"]: return True
    else: return False

def Body():
    snake["body"].append({"x" : snake["head"]["x"], "y" : snake["head"]["y"]})
    if len(snake["body"]) > (game["score"] + 1):
        snake["body"].pop(0)

def PrintSnake():
     
    Body()
    
    for i in range(len(snake["body"])):
        x = snake["body"][i]["x"]
        y = snake["body"][i]["y"]
        pygame.draw.rect(screen, black,[x,y,20,20])

def Wall(x, y):
    if x == game["width"] or x == -20 or y == game["height"] or y == -20: return True
    
def SnakeInSnake():
    for i in range(len(snake["body"])-1):
        if snake["body"][i]["x"] == snake["head"]["x"] and snake["body"][i]["y"] == snake["head"]["y"]: return True
    return False

def Death():
    if Wall(snake["head"]["x"], snake["head"]["y"]) or SnakeInSnake(): return True

pygame.init()

Clear()

white = (255, 255, 255)
black = (0, 0, 0)

game = GenGame()
snake = GenSnake()

screen = pygame.display.set_mode([game["width"], game["height"]])
pygame.display.set_caption('Snake game by Csabi')
clock = pygame.time.Clock()

while game["run"]:
    for event in pygame.event.get():
        Close()
        snake["moving"] = Keydown(snake["size"], snake["moving"])
    if Death(): game["run"] = False
    
    Move(snake["moving"])

    screen.fill(white)

    PrintSnake()

    if game["foodInMap"] == False:
        food = GenFood()
        game["foodInMap"] = True
    if Eat():
        game["score"] += 1
        game["foodInMap"] = False

    FoodPrint(food["x"], food["y"])    

    pygame.display.update()
    
    clock.tick(10)

print(game["score"])

pygame.quit()
quit()