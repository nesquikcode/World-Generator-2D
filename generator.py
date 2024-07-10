import pygame, random, json, os
from PIL import Image
from settings import COLUMNS, ROWS, DIRTCHANCE, DIRT, DARKDIRT, WATER, SUBWATER, WIDTH, HEIGHT, BLOCKX, BLOCKY, SAND, ITERATIONS, WATER_ITERATIONS, SUBWATER_ITERATIONS, FOREST_ITERATIONS, FORESTCHANCE, MOUNTAINS, HIGH_MOUNTAINS, MOUNTAINS_ITERATIONS, HIGH_MOUNTAINS_ITERATIONS, MOUNTAINS_CHANCE, HIGH_MOUNTAINS_CHANCE, SNOW, SNOW_CHANCE, SNOW_ITERATIONS, FINAL_ITERATIONS, ENABLE_LOAD_CALLBACK, CONSOLE_MODE
global screen
screen = None

def loadbar(loaded, all):
    print(f"Loaded {loaded}/{all} - {round(loaded/(all/100), 2)}.")

def generate(load_bar_func = loadbar):
    worldmap = []
    
    for x in range(1, COLUMNS*ROWS+1):
        a = random.randint(int(DIRTCHANCE.split(":")[0]), int(DIRTCHANCE.split(":")[1]))
        if a == int(DIRTCHANCE.split(":")[0]):
            worldmap.append("d")
        else:
            worldmap.append("w")

        if x/(COLUMNS*ROWS/100) % 10 == 0 and load_bar_func != None:
            if ENABLE_LOAD_CALLBACK: load_bar_func(x, COLUMNS*ROWS)

    for range_counter in range(0, ITERATIONS):
        for info in enumerate(worldmap):
            
            x = info[1]
            up_left = info[0]-COLUMNS-1
            up = info[0]-COLUMNS
            up_right = info[0]-COLUMNS+1
            right = info[0]+1
            left = info[0]-1
            down_left = info[0]+COLUMNS-1
            down = info[0]+COLUMNS
            down_right = info[0]+COLUMNS+1
            center = info[0]

            dirt_counter = 0
            water_counter = 0

            try:
                if worldmap[up_left] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[up_right] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass
            
            try:
                if worldmap[up] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[left] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[right] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down_left] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down_right] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            if x == "d":
                if water_counter in [3,6,7,8]:
                    worldmap[center] = "w"
            elif x == "w":
                if dirt_counter in [3,6,7,8]:
                    worldmap[center] = "d"
        if ENABLE_LOAD_CALLBACK: loadbar(range_counter+1, ITERATIONS)
    
    for range_counter in range(0, WATER_ITERATIONS):

        for info in enumerate(worldmap):
            
            x = info[1]
            up_left = info[0]-COLUMNS-1
            up = info[0]-COLUMNS
            up_right = info[0]-COLUMNS+1
            right = info[0]+1
            left = info[0]-1
            down_left = info[0]+COLUMNS-1
            down = info[0]+COLUMNS
            down_right = info[0]+COLUMNS+1
            center = info[0]

            dirt_counter = 0
            water_counter = 0
            sand_counter = 0

            try:
                if worldmap[up_left] == "d": dirt_counter += 1
                elif worldmap[up_left] == "s": sand_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[up_right] == "d": dirt_counter += 1
                elif worldmap[up_right] == "s": sand_counter += 1
                else: water_counter += 1
            except: pass
            
            try:
                if worldmap[up] == "d": dirt_counter += 1
                elif worldmap[up] == "s": sand_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[left] == "d": dirt_counter += 1
                elif worldmap[left] == "s": sand_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[right] == "d": dirt_counter += 1
                elif worldmap[right] == "s": sand_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down] == "d": dirt_counter += 1
                elif worldmap[down] == "s": sand_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down_left] == "d": dirt_counter += 1
                elif worldmap[down_left] == "s": sand_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down_right] == "d": dirt_counter += 1
                elif worldmap[down_right] == "s": sand_counter += 1
                else: water_counter += 1
            except: pass

            if water_counter > 0 and dirt_counter > 1:
                worldmap[center] = "s"
            if sand_counter > 6 and worldmap[center] != "s":
                if random.randint(1, 10) < 3:
                    worldmap[random.choice([up, up_left, up_right, down, down_left, down_right, left, right, center])] = "s"
            if sand_counter == 9:
                worldmap[center] = "s"

        if ENABLE_LOAD_CALLBACK: loadbar(range_counter+1, WATER_ITERATIONS)

    for range_counter in range(0, SUBWATER_ITERATIONS):

        for info in enumerate(worldmap):
            
            x = info[1]
            up_left = info[0]-COLUMNS-1
            up = info[0]-COLUMNS
            up_right = info[0]-COLUMNS+1
            right = info[0]+1
            left = info[0]-1
            down_left = info[0]+COLUMNS-1
            down = info[0]+COLUMNS
            down_right = info[0]+COLUMNS+1
            center = info[0]

            dirt_counter = 0
            water_counter = 0
            sand_counter = 0
            subwater_counter = 0

            try:
                if worldmap[up_left] == "d": dirt_counter += 1
                elif worldmap[up_left] == "s": sand_counter += 1
                elif worldmap[up_left] == "sw": subwater_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[up_right] == "d": dirt_counter += 1
                elif worldmap[up_right] == "s": sand_counter += 1
                elif worldmap[up_right] == "sw": subwater_counter += 1
                else: water_counter += 1
            except: pass
            
            try:
                if worldmap[up] == "d": dirt_counter += 1
                elif worldmap[up] == "s": sand_counter += 1
                elif worldmap[up] == "sw": subwater_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[left] == "d": dirt_counter += 1
                elif worldmap[left] == "s": sand_counter += 1
                elif worldmap[left] == "sw": subwater_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[right] == "d": dirt_counter += 1
                elif worldmap[right] == "s": sand_counter += 1
                elif worldmap[right] == "sw": subwater_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down] == "d": dirt_counter += 1
                elif worldmap[down] == "s": sand_counter += 1
                elif worldmap[down] == "sw": subwater_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down_left] == "d": dirt_counter += 1
                elif worldmap[down_left] == "s": sand_counter += 1
                elif worldmap[down_left] == "sw": subwater_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down_right] == "d": dirt_counter += 1
                elif worldmap[down_right] == "s": sand_counter += 1
                elif worldmap[down_right] == "sw": subwater_counter += 1
                else: water_counter += 1
            except: pass

            if water_counter > 0 and sand_counter > 0 and worldmap[center] == "w":
                worldmap[center] = "sw"
            if worldmap[center] == "w" and subwater_counter > 0:
                if random.randint(1, 20) < 3:
                    worldmap[center] = "sw"
                    
        if ENABLE_LOAD_CALLBACK: loadbar(range_counter+1, SUBWATER_ITERATIONS)

    for x in enumerate(worldmap):
        if x[1] == "d":
            a = random.randint(int(FORESTCHANCE.split(":")[0]), int(FORESTCHANCE.split(":")[1]))
            if a == int(FORESTCHANCE.split(":")[0]):
                worldmap[x[0]] = "d"
            else:
                worldmap[x[0]] = "dd"

    for range_counter in range(0, FOREST_ITERATIONS):
        for info in enumerate(worldmap):
            
            x = info[1]
            up_left = info[0]-COLUMNS-1
            up = info[0]-COLUMNS
            up_right = info[0]-COLUMNS+1
            right = info[0]+1
            left = info[0]-1
            down_left = info[0]+COLUMNS-1
            down = info[0]+COLUMNS
            down_right = info[0]+COLUMNS+1
            center = info[0]

            dirt_counter = 0
            water_counter = 0

            try:
                if worldmap[up_left] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[up_right] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass
            
            try:
                if worldmap[up] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[left] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[right] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down_left] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            try:
                if worldmap[down_right] == "d": dirt_counter += 1
                else: water_counter += 1
            except: pass

            if x == "d":
                if water_counter in [3,6,7,8]:
                    worldmap[center] = "dd"
            elif x == "dd":
                if dirt_counter in [3,6,7,8]:
                    worldmap[center] = "d"
        if ENABLE_LOAD_CALLBACK: loadbar(range_counter+1, FOREST_ITERATIONS)

    for x in enumerate(worldmap):
        if x[1] == "dd":
            a = random.randint(int(MOUNTAINS_CHANCE.split(":")[0]), int(MOUNTAINS_CHANCE.split(":")[1]))
            if a == int(MOUNTAINS_CHANCE.split(":")[0]):
                worldmap[x[0]] = "m"
            else:
                worldmap[x[0]] = "dd"

    for range_counter in range(0, MOUNTAINS_ITERATIONS):

        for info in enumerate(worldmap):
            
            x = info[1]
            up_left = info[0]-COLUMNS-1
            up = info[0]-COLUMNS
            up_right = info[0]-COLUMNS+1
            right = info[0]+1
            left = info[0]-1
            down_left = info[0]+COLUMNS-1
            down = info[0]+COLUMNS
            down_right = info[0]+COLUMNS+1
            center = info[0]

            forest_counter = 0
            mountains_counter = 0

            try:
                if worldmap[up_left] == "dd": forest_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[up_right] == "dd": forest_counter += 1
                else: mountains_counter += 1
            except: pass
            
            try:
                if worldmap[up] == "dd": forest_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[left] == "dd": forest_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[right] == "dd": forest_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[down] == "dd": forest_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[down_left] == "dd": forest_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[down_right] == "dd": forest_counter += 1
                else: mountains_counter += 1
            except: pass

            if worldmap[center] == "dd":
                if mountains_counter in [3,6,7,8]:
                    worldmap[center] = "m"
            elif worldmap[center] == "m":
                if forest_counter in [3,6,7,8]:
                    worldmap[center] = "dd"
                    
        if ENABLE_LOAD_CALLBACK: loadbar(range_counter+1, MOUNTAINS_ITERATIONS)

    for x in enumerate(worldmap):
        if x[1] == "m":
            a = random.randint(int(HIGH_MOUNTAINS_CHANCE.split(":")[0]), int(HIGH_MOUNTAINS_CHANCE.split(":")[1]))
            if a == int(HIGH_MOUNTAINS_CHANCE.split(":")[0]):
                worldmap[x[0]] = "hm"
            else:
                worldmap[x[0]] = "m"

    for range_counter in range(0, HIGH_MOUNTAINS_ITERATIONS):

        for info in enumerate(worldmap):
            
            x = info[1]
            up_left = info[0]-COLUMNS-1
            up = info[0]-COLUMNS
            up_right = info[0]-COLUMNS+1
            right = info[0]+1
            left = info[0]-1
            down_left = info[0]+COLUMNS-1
            down = info[0]+COLUMNS
            down_right = info[0]+COLUMNS+1
            center = info[0]

            high_mountains_counter = 0
            mountains_counter = 0

            try:
                if worldmap[up_left] == "hm": high_mountains_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[up_right] == "hm": high_mountains_counter += 1
                else: mountains_counter += 1
            except: pass
            
            try:
                if worldmap[up] == "hm": high_mountains_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[left] == "hm": high_mountains_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[right] == "hm": high_mountains_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[down] == "hm": high_mountains_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[down_left] == "hm": high_mountains_counter += 1
                else: mountains_counter += 1
            except: pass

            try:
                if worldmap[down_right] == "hm": high_mountains_counter += 1
                else: mountains_counter += 1
            except: pass

            if worldmap[center] == "hm":
                if mountains_counter in [3,6,7,8]:
                    worldmap[center] = "m"
            elif worldmap[center] == "m":
                if high_mountains_counter in [3,6,7,8]:
                    worldmap[center] = "hm"
                    
        if ENABLE_LOAD_CALLBACK: loadbar(range_counter+1, HIGH_MOUNTAINS_ITERATIONS)

    return worldmap

def render_map(screen, wmap):
    xcount = 0
    ycount = 0
    for x in wmap:
        for y in pygame.event.get():
            if y.type == pygame.QUIT:
                pass

        if xcount >= WIDTH:
            xcount = 0
            ycount += BLOCKY
        
        if ycount >= HEIGHT:
            break

        if x == "d":
            pygame.draw.rect(screen, DIRT, (xcount, ycount, BLOCKX, BLOCKY))
        elif x == "w":
            pygame.draw.rect(screen, WATER, (xcount, ycount, BLOCKX, BLOCKY))
        elif x == "s":
            pygame.draw.rect(screen, SAND, (xcount, ycount, BLOCKX, BLOCKY))
        elif x == "sw":
            pygame.draw.rect(screen, SUBWATER, (xcount, ycount, BLOCKX, BLOCKY))
        elif x == "dd":
            pygame.draw.rect(screen, DARKDIRT, (xcount, ycount, BLOCKX, BLOCKY))
        elif x == "m":
            pygame.draw.rect(screen, MOUNTAINS, (xcount, ycount, BLOCKX, BLOCKY))
        elif x == "hm":
            pygame.draw.rect(screen, HIGH_MOUNTAINS, (xcount, ycount, BLOCKX, BLOCKY))
        elif x == "sn":
            pygame.draw.rect(screen, SNOW, (xcount, ycount, BLOCKX, BLOCKY))

        xcount += BLOCKX


if __name__ == "__main__":
    if "map.json" not in os.listdir():
        wmap = generate(loadbar)
        json.dump({'map' : wmap, "columns" : COLUMNS, "rows" : ROWS}, open("map.json", "x"))
    else:
        winfo = json.load(open("map.json"))
        wmap = winfo['map']
        if winfo['columns'] != COLUMNS:
            print("Мир не поддерживается на данных настройках. Настройки будут изменены для открытия мира. (COLUMNS WARN)")
            COLUMNS = winfo['columns']
            BLOCKX = WIDTH/winfo['columns']
        if winfo['rows'] != ROWS:
            print("Мир не поддерживается на данных настройках. Настройки будут изменены для открытия мира. (ROWS WARN)")
            ROWS = winfo['rows']
            BLOCKY = HEIGHT/winfo['rows']


    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.Clock()
    fps = 60

    run = True

    render_map(screen, wmap)
    pygame.display.flip()

    pygame.image.save(screen, "map.png")
    img = Image.open("map.png")
    image = img.resize((COLUMNS, ROWS), resample=Image.LANCZOS)
    image.save("map.png")

    while run:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                pygame.quit()
                run = False