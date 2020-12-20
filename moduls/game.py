from moduls import file as FILE
import pygame

def Clear():
    """Terminál törlését, tisztítását végzi el a függvény.
    """
    import os
    try:
        os.system("clear")
    except:
        os.system("cls")

def GenGame() -> dict:
    """A függvény létrehoz egy game dictionary-t.

    Returns:
        dict:

            width (int): Pálya hosszusága.
        
            height (int): Pálya magassága.
        
            run (bool): Megadja, hogy fut-e a játék.
        
            score (int): A játék éppen pontszáma.
        
            foodInMap (bool): Megadja, hogy van-e kaja generálva a pályára. 
    """
    return {
        "width" : 800,     
        "height" : 600,
        "run" : True,
        "score" : 0,
        "foodInMap" : False
    }

def GenSnake(startX:int, startY:int) -> dict:
    """A függvény létrehoz egy snake dictionary-t.

    Args:
        startX (int): A kígyó kezdő pozíciójának x koordinátája
        startY (int): A kígyó kezdő pozíciójának y koordinátája

    Returns:
        dict:

            size (int): A kígyó egy darabjának mérete.

            head (dict): Itt tárolódik a kígyó fejének az x és y koordinátája.
    
            body (list): Itt tárolódik a kígyó testének minden darabjának a x és y koordinátája.
        
            moving (dict): A kígyó irányát adja meg x és y koordinátákkal.
    """
    return {
        "size" : 20,
        "head" : {"x" : startX, "y" : startY},
        "body" : [],
        "moving" : {"x" : 20, "y" : 0}
    }

def Close(event) -> bool:
    """Az ablak bezárásának vizsgálása.

    Args:
        event (event): pygame saját típusa, ha valami történt akkor így tárolódik el.

    Returns:
        bool: A függvény True értékkel tér vissza, ha a pygame ablakot bezárjuk és False értékkel, ha nem történt semmi.
    """
    if event.type == pygame.QUIT: return False
    return True

def Keydown(event, size:int, mov:dict) -> dict:
    """A függvény a mozgás változását vizsgálja. Megváltozhat a kígyó mozgási iránya,
    ami a billentyűzet nyilai közül valamelyik megnyomásával történik.
    Ha ellentétes az irányba akarjuk megváltoztatni az irányt, mint amerre eddig mozgott a kígyó,
    akkor nem fog irányváltoztatás történni. Pl.: Ha jobb irányba tart a kígyó, akkor balra nem tud mozogni.

    Args:
        event (event): Pygame saját típusa, ha valami történt akkor így tárolódik el.
        size (int):  A kígyó egy darabjának mérete.
        mov (dict): A kígyó irányát adja meg x és y koordinátákkal.

    Returns:
        dict: A megváltoztatott irány x és y koordinátákkal. Ezek a koordínáta értékek lesznek hozzáadva a kígyó fejének koordinátáihoz.
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

def Move(head:dict, mov:dict):
    """Az irányt x és y koordinátákkal definiáló mov dict segítségével a függvény a kígyó fejét a megfelelő irányba tereli.
    Pl.: Ha balra fog mozogni a kígyó akkor hozzáad az x koordinátához egy -x értéket, ahol az x a kígyó egy darabjának a mérete
    és az y koordinátához 0-át fog hozzáadni.

    Args:
        head (dict): Itt tárolódik a kígyó fejének az x és y koordinátája.
        mov (dict): A kígyó irányát adja meg x és y koordinátákkal.
    """
    head["x"] += mov["x"]
    head["y"] += mov["y"]

def GenCoordinates(length:int) -> list:
    """A függvény visszadja lehetséges koordináta értékeket, amik a pályán belül vannak.

    Args:
        length (int): Hossz, ameddig koordináta értékeket lehet generálni.

    Returns:
        list: Lehetséges koordináta értékek listája.
    """
    coor = []
    for i in range(0, length, 20):
        coor.append(i)
    return coor

def GoodCoordinates(x:int, y:int, body:dict) -> bool:
    """A függvény megvizsgálja, hogy a generált koordináták, nem-e egyeznek a kígyó koordinátáival.

    Args:
        x (int): Generált x koordináta.
        y (int): Generált y koordináta.
        body (dict): A kígyó testének x és y koordinátái.

    Returns:
        bool: Ha a generált koordináták pontosan megegyezznek a kígyó testének valamelyik helyzetével, akkor a függvény False értékkel tér vissza, különben True-val.
    """
    for i in body:
        if i["x"] == x and i["y"] == y: return False
    return True

def GenFood(x:list, y:list, body:dict) -> dict:
    """A függvény véletlenszerűen választ egy x és egy y értéket a lehetséges listákból,
    majd megvizsgálja, hogy megegyezik-e a kígyó testének valamelyik darabjával. Ha pontos egyezés van,
    akkor újra generálódnak az x és y koordináták addig, amíg nem kapunk egy olyan koordináta párt,
    ami nem egyezik meg a kígyó testének egyik darabjával sem.

    Args:
        x (list): A lehetséges x koordináták listája.
        y (list): A lehetséges y koordináták listája.
        body (dict): A kígyó testének x és y koordinátái.

    Returns:
        dict: Olyan x és y koordináta, aminek a helyzete nem egyezik meg a kígyó testének egyik darabjával sem.
    """
    import random
    randx = random.choice(x)
    randy = random.choice(y)
    while True:
        if GoodCoordinates(randx, randy, body): break
        randx = random.choice(x)
        randy = random.choice(y)
    return {"x" : randx, "y" : randy}
   
def FoodPrint(x:int, y:int, color:tuple, size:int, screen):
    """Megjeleníti a kígyó célpontját, az ételt, ami a jelen esetben egy π karakter.

    Args:
        x (int): Az étel x koordinátája.
        y (int): Az étel y koordinátája.
        color (tuple): Az étel megjelenési színének rgb kódja.
        size (int): Az étel mérete.
        screen (screen): Pygame saját típusú képernyője, ahol az étel megjelenik.
    """
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render("π", True, color)
    screen.blit(text, (x, y))

def Eat(head:dict, food:dict) -> bool:
    """A kígyó pontszerzését, étkezését vizsgálja.

    Args:
        head (dict): A kígyó fejének koordinátái.
        food (dict): Az étel koordinátái.

    Returns:
        bool: Ha kígyó fejének koordinátái megegyeznek az étel koordinátáival, akkor a függynény True értékkel tér vissza, ha nem egyezik meg, akkor False értékkel.
    """
    if head["x"] == food["x"] and head["y"] == food["y"]: return True
    return False

def Body(body:dict, head:dict, score:int):
    """A kígyó mozgását definiálja. A kígyó testéhez hozzáadja a kígyó fejéz ezzel megnő a hossza,
    majd a kígyó testének az utolsó darabját törli a listából. Vagyis mindig hozzáad egy elemet a kígyó elejéhez
    és egyet elvesz a testének végéből, így fog mozogni a pályán a kígyó.

    Args:
        body (dict): A kígyó testének x és y koordinátái.
        head (dict): A kígyó fejének koordinátái.
        score (int): A játék éppeni pontszáma.
    """
    body.append({"x" : head["x"], "y" : head["y"]})
    if len(body) > (score + 1):
        body.pop(0)

def PrintSnake(body:dict, head:dict, score:int, screen, color:tuple):
    """A kígyó éppeni helyzetét rajzolja ki a képernyőre.

    Args:
        body (dict): A kígyó testének x és y koordinátái.
        head (dict): A kígyó fejének koordinátái.
        score (int): A játék éppeni pontszáma.
        screen (screen): Pygame saját típusú képernyője, ahol a kígyó kirajzolódik.
        color (tuple): Az kígyó megjelenési színének rgb kódja.
    """
    Body(body, head, score)
    for i in range(len(body)):
        x = body[i]["x"]
        y = body[i]["y"]
        pygame.draw.rect(screen, color, [x,y,20,20])

def Wall(head:dict, width:int, height:int, size:int) -> bool:
    """Azt vizsgálja, hogy a kígyó a falhoz ért-e.

    Args:
        head (dict): A kígyó fejének koordinátái.
        width (int): Pálya hosszusága.
        height (int): Pálya magassága.
        size (int): A kígyó egy darabjának mérete.

    Returns:
        bool: Ha a kígyó fejének koordinátája megegyezik valamelyik fallal, akkor True értékkel tér vissza.
    """
    if head["x"] == width or head["x"] == -size or head["y"] == height or head["y"] == -size: return True
    
def SnakeInSnake(body:dict, head:dict) -> bool:
    """Azt vizsgálja, hogy a kígyó fejének a helyzete megegyezik-e a testének valamelyik darbjának helyzetével.

    Args:
        body (dict): A kígyó testének x és y koordinátái.
        head (dict): A kígyó fejének koordinátái.

    Returns:
        bool: Ha kígyó fejének helyzete pontosan megegyezik a kígyó testének valamelyik darabjának helyzetével, akkor a függvény True értékkel tér vissza.
    """
    for i in range(len(body)-1):
        if body[i]["x"] == head["x"] and body[i]["y"] == head["y"]: return True

def Death(snake:dict, width:int, height:int) -> bool:
    """A játék végét vizsgálja.

    Args:
        snake (dict): A kígyó adatai.
        width (int): Pálya hosszusága.
        height (int): Pálya magassága.

    Returns:
        bool: Ha falhoz ért a kígyó vagy a testének valamelyik eleméhez, akkor True-val tér vissza, vagyis akkor meghalt a kígyó.
    """
    if Wall(snake["head"], width, height, snake["size"]) or SnakeInSnake(snake["body"], snake["head"]): return True

def Nickname() -> str:
    """Egy bemeneti adatot vár, ami a nickname lesz, ez a karakterlánc nem lehet hoszabb 16 karakternél, ha hoszabb,
    akkor arról a függvény tájékoztatást ad és újra kéri a bemenetet.

    Returns:
        str: 16 karakternél nem hoszabb karakterlánc. Ez fog megjelenni az eredményeknél, mint a játékos neve.
    """
    name = ""
    while True:
        name = input("Nickname: ")
        if len(name) < 17: break
        print("Túl hosszú nickname! (16 karakternél ne legyen hosszabb)")
    Clear()
    if set(name) == {" "} or len(name) == 0: return "Anonim" 
    return name

def SnakeGame() -> str:
    """A szoftver a terminál törlésével kezdődik. A függvényen belül meg lettek adva az alap paraméterek és definiálva lettek a változók.
    A pygame indítása után egy ciklus indul el ami a játék végéig ismétlődik. A függvény figyeli az "event"-eket,
    vagyis ha valmi esemény történt (pl.: megnyomtunk egy gombot a billentyűzeten), akkor azt megvizsgálja, ez a mozgást,
    illetve a játék végét befolyásolja. A futás során mindig frissül a képernyő és fehér színnel tölti ki az egészet,
    amire az éppeni elemek kirajzolódnak fekete színnel. Vizsgálva van, hogy van-e étel a pályán, ha nincsen akkor véletlenszerűen
    generálva lesz egy. Ha kígyó megevett egy π karakter, akkor a pontszám megnő, illetve újra generálódik egy étel a pályán.
    A pygame saját időmérő funkciójával lett beállítva a játék futási sebessége. Ha a program kilépett a ciklusból,
    akkor a pygame-ból is kilép, majd elmenti az eredményeket egy json fájlba.

    Returns:
        str: Egy tájékoztató szöveg, hogy mentésre került az eredmény.
    """
    Clear()

    white = (255, 255, 255)
    black = (0, 0, 0)
    name = Nickname()
    game = GenGame()
    snake = GenSnake(160, 160)
    
    pygame.init()

    screen = pygame.display.set_mode([game["width"], game["height"]])
    pygame.display.set_caption('Snake game by Csabi')
    clock = pygame.time.Clock()

    while game["run"]:
        for event in pygame.event.get():
            game["run"] = Close(event)
            snake["moving"] = Keydown(event, snake["size"], snake["moving"])
        if Death(snake, game["width"], game["height"]): game["run"] = False
        
        Move(snake["head"], snake["moving"])
        screen.fill(white)
        PrintSnake(snake["body"], snake["head"], game["score"], screen, black)

        if game["foodInMap"] == False:
            food = GenFood(GenCoordinates(game["width"]), GenCoordinates(game["height"]), snake["body"])
            game["foodInMap"] = True
        if Eat(snake["head"], food):
            game["score"] += 1
            game["foodInMap"] = False

        FoodPrint(food["x"], food["y"], black, snake["size"],screen)    

        pygame.display.update()        
        clock.tick(10)

    pygame.quit()

    return FILE.Save(game["score"], "stat.json", name)