from __builtins__ import *

# Metaroot 制作了这个游戏
# The Farmer Was Replaced
# 编程农场

def goto(x, y):
    if x >= get_world_size() or y >= get_world_size():
        return None
    if x > get_pos_x(): 
        while x - get_pos_x():
            move(East)
    elif x < get_pos_x():
        while x - get_pos_x():
            move(West)
    if y > get_pos_y(): 
        while y - get_pos_y():
            move(North)
    elif y < get_pos_y():
        while y - get_pos_y():
            move(South)

def moveto(direction, s):
    for i in range(s):
        move(direction)

def set_ground(g):
    if get_ground_type() != g:
        till()

def plant_bush():
    set_ground(Grounds.Grassland)
    if plant(Entities.Bush):
        move(North)

def plant_carrot():
    set_ground(Grounds.Soil)
    if plant(Entities.Carrot):
        move(North)

def plant_pumpkin():
    set_ground(Grounds.Soil)
    if plant(Entities.Pumpkin):
        move(North)

def plant_hay():
    set_ground(Grounds.Grassland)
    move(North)

def plant_tree():
    set_ground(Grounds.Grassland)
    if plant(Entities.Tree):
        move(North)

def plant_cactus():
    set_ground(Grounds.Soil)
    if plant(Entities.Cactus):
        move(North)

def plant_sunflower():
    set_ground(Grounds.Soil)
    if plant(Entities.Sunflower):
        move(North)

def init():
    clear()
    goto(0,0)

def water():
    use_item(Items.Water)
    use_item(Items.Water)

# strategy ---------------------

def ptree():
    while True:
        goto(0,0)
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if can_harvest():
                    harvest()
                    if x % 2 == 0:
                        if y % 2 == 0:
                            plant_tree()
                        else:
                            plant_hay()
                    elif x % 2 != 0:
                        if y % 2 != 0:
                            plant_tree()
                        else:
                            plant_hay()
                else:
                    move(North)
            move(East)
def pbch():
    while True:
        goto(0,0)
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if can_harvest():
                    harvest()
                    if x >= 16:
                        plant_carrot()
                    elif (x >= 0) and (x % 2 == 0):
                        if y % 2 == 0:
                            plant_tree()
                        else:
                            plant_hay()
                    elif (x >= 0) and (x % 2 != 0):
                        if y % 2 != 0:
                            plant_tree()
                        else:
                            plant_hay()
                else:
                    move(North)
            move(East)

def phay():
    while True:
        goto(0,0)
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if can_harvest():
                    harvest()
                move(North)
            move(East)

def pbchf():
    while True:
        goto(0,0)
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                water()
                if can_harvest():
                    harvest()
                    if x >= 28:
                        plant_sunflower()
                    elif x >= 12:
                        plant_carrot()
                    elif x >= 0 and (x % 2 == 0):
                        if y % 2 == 0:
                            plant_tree()
                        else:
                            plant_hay()
                    elif x >= 0 and (x % 2 != 0):
                        if y % 2 != 0:
                            plant_tree()
                        else:
                            plant_hay()
                else:
                    move(North)
            move(East)

# MAIN ########################################################################

def main():
    while True:
        goto(0,0)
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                water()
                if can_harvest():
                    harvest()
                if x >= 24:
                    plant_carrot()
                elif x >= 8:
                    plant_sunflower()
                elif x >= 0 and (x % 2 == 0):
                    if y % 2 == 0:
                        plant_tree()
                        use_item(Items.Fertilizer)
                    else:
                        plant_hay()
                elif x >= 0 and (x % 2 != 0):
                    if y % 2 != 0:
                        plant_tree()
                        use_item(Items.Fertilizer)
                    else:
                        plant_hay()
            move(East)
        # plant 6x6 big pumpkin
        for i in range(4):
            plant_pumpkin_big(26,i * 6 + i * 1)
        plant_cactus_sort() # plant Cactus
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                harvest()
                move(North)
            move(East)
        get_mazes() # create maze
        # search Gold
        if dfs(North) == False:
            dfs(South)

def plant_pumpkin_big(tx,ty):
    goto(tx,ty)
    for y in range(ty, ty+6):
        if y % 2:
            for x in range(tx+5,tx-1,-1):
                water()
                goto(x,y)
                if can_harvest():
                    harvest()
                plant_pumpkin()
        else:
            for x in range(tx,tx+6,1):
                water()
                goto(x,y)
                if can_harvest():
                    harvest()
                plant_pumpkin()
    goto(tx,ty)
    n = 0
    bad = []
    while True:
        for y in range(ty, ty+6):
            if y % 2:
                for x in range(tx+5,tx-1,-1):
                    goto(x,y)
                    if can_harvest():
                        if (x,y) in bad:
                            bad.remove((x,y))
                    else:
                        plant_pumpkin()
                        if (x,y) not in bad:
                            bad.append((x,y))
            else:
                for x in range(tx,tx+6,1):
                    goto(x,y)
                    if can_harvest():
                        if (x,y) in bad:
                            bad.remove((x,y))
                    else:
                        plant_pumpkin()
                        if (x,y) not in bad:
                            bad.append((x,y))
        do_a_flip()
        if len(bad) == 0:
            harvest()
            break

def plant_cactus_sort():
    goto(0,0)
    for x in range(17):
        for y in range(16):
            if can_harvest():
                harvest()
                plant_cactus()
            else:
                plant_cactus()
        goto(x,0)
    goto(0,0)
    array2d = []
    for x in range(0,16):
        array = []
        for y in range(0,16):
            goto(x,y)
            array.append(measure())
        array2d.append(array)
    for x in range(0,16):
        for y in range(0,16):
            swapped = False
            for yi in range(0, 16-y-1):
                if array2d[x][yi] > array2d[x][yi+1]:
                    array2d[x][yi],array2d[x][yi+1]=array2d[x][yi+1],array2d[x][yi]
                    goto(x,yi)
                    swap(North)
                    swapped = True
            if not swapped:
                break
    for y in range(0,16):
        for x in range(0,16):
            swapped = False
            for xi in range(0, 16-x-1):
                if array2d[xi][y] > array2d[xi+1][y]:
                    array2d[xi][y],array2d[xi+1][y]=array2d[xi+1][y],array2d[xi][y]
                    goto(xi,y)
                    swap(East)
                    swapped = True
            if not swapped:
                break
    goto(0,0)
    if can_harvest():
        harvest()

def get_mazes():
    goto(0,15)
    harvest()
    water()
    set_ground(Grounds.Grassland)
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1))

def dfs(before):
    opposite={East:West,West:East,North:South,South:North}
    if (get_pos_x(),get_pos_y()) == measure():
        harvest()
        return True
    dire=[East,South,West,North]
    s = []
    for d in dire:
        if d == opposite[before]:
            continue
        if can_move(d):
            s.append(d)
    for m in s:
        move(m)
        if dfs(m):
            return True
    move(opposite[before])
    return False

def dino():
    goto(0,0)
    i = 0
    change_hat(Hats.Dinosaur_Hat)
    nx,ny=measure()
    while True:
        if i >=10:
            break
        nx,ny=measure()
        if (nx==None)or(ny==None):
            return False
        goto(nx,ny)
        i+=1
    change_hat(Hats.Brown_Hat)

if __name__ == '__main__':
    #clear()         
    #init()
    goto(0,0)
    #pbchf()
    #main()
    #plant_cactus_sort()
    #clear()


