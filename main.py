import pygame

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
        "body" : [
            {"x" : 300, "y" : 300},
            {"x" : 280, "y" : 300},
            {"x" : 260, "y" : 300}
        ],
        "change_x" : 20,
        "change_y" : 0
    }

def Close():
    if event.type == pygame.QUIT: game["run"] = False 

def Keydown():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and (snake["change_x"] != snake["size"] and snake["change_y"] != 0):
            snake["change_x"] = -snake["size"]
            snake["change_y"] = 0
        elif event.key == pygame.K_RIGHT and (snake["change_x"] != -snake["size"] and snake["change_y"] != 0):
            snake["change_x"] = snake["size"]
            snake["change_y"] = 0
        elif event.key == pygame.K_UP and (snake["change_x"] != 0 and snake["change_y"] != snake["size"]):
            snake["change_x"] = 0
            snake["change_y"] = -snake["size"]
        elif event.key == pygame.K_DOWN and (snake["change_x"] != 0 and snake["change_y"] != -snake["size"]):
            snake["change_x"] = 0
            snake["change_y"] = snake["size"]

def Move():
    snake["head"]["x"] += snake["change_x"]
    snake["head"]["y"] += snake["change_y"]

def GenCoordinates(length):
    coor = []
    for i in range(0, length, 20):
        coor.append(i)
    return coor

def GoodCoordinates(x, y):
    good = True
    for i in snake["body"]:
        if i["x"] == x and i["y"] == y: good = False
    if good: return True
    else: return False

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

def Wall(x, y):
    if x == game["width"] or x == -20 or y == game["height"] or y == -20: return True
    
def Death():
    if Wall(snake["head"]["x"], snake["head"]["y"]): return True

#region Main
pygame.init()

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
        Keydown()
    if Death(): game["run"] = False
    
    Move()
    
    #for i in range(len(snake["body"])):
    #    x = snake["body"][i]["x"]
    #    y = snake["body"][i]["y"]

    #    pygame.draw.rect(screen, black,[x,y,20,20])
    screen.fill(white)
    pygame.draw.rect(screen, black, [snake["head"]["x"], snake["head"]["y"], snake["size"], snake["size"]])
    
    if game["foodInMap"] == False:
        food = GenFood()
        game["foodInMap"] = True
    if Eat():
        game["score"] += 1
        game["foodInMap"] = False

    FoodPrint(food["x"], food["y"])    

    pygame.display.update()
    
    clock.tick(15)

print(game["score"])

pygame.quit()
quit()
#endregion