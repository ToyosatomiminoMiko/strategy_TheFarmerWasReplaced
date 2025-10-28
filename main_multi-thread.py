from f0 import *

def plant_col_tree0():
    while True:
        if get_water() < 0.5:
            use_item(Items.Water)
        if can_harvest():
            harvest()
        if get_pos_y() % 2 == 0:
            plant_tree()
        else:from plantx import *


def plant_col_sumflower():
    while True:
        for y in range(32):
            if can_harvest():
                harvest()
            if get_water()<0.5:
                use_item(Items.Water)
            plant_sunflower()

def plant_col_hay():
    for y in range(32):
        harvest()
        set_ground(Grounds.Grassland)
        move(North)
    for y in range(32):
        harvest()
        set_ground(Grounds.Grassland)
        move(South)

def plant_col_tree0():
    while True:
        if get_water() < 0.5:
            use_item(Items.Water)
        if can_harvest():
            harvest()
        if get_pos_y() % 2 == 0:
            plant_tree()
        else:
            plant_hay()
        
def plant_col_tree1():
    while True:
        if get_water() < 0.5:
            use_item(Items.Water)
        if can_harvest():
            harvest()
        if get_pos_y() % 2 != 0:
            plant_tree()
        else:
            plant_carrot()

def plant_col_carrot():
    for y in range(31):
        if can_harvest():
            harvest()
        if get_water()<0.5:
            use_item(Items.Water)
        plant_carrot()

def plant_col_pumpkin():
    while True:
        if get_pos_y() == 31:
            if can_harvest():
                harvest()
                plant_pumpkin()
            goto(get_pos_x(),0)
            break
        if can_harvest():
            harvest()
        if get_water()<0.5:
            use_item(Items.Water)
        plant_pumpkin()
    bad = []
    while True:
        for y in range(32):
            goto(get_pos_x(),y)
            if can_harvest():
                if y in bad:
                    bad.remove(y)
            else:
                plant_pumpkin()
                if y not in bad:
                    bad.append(y)
        if len(bad) == 0:
            break


def main1():
    change_hat(Hats.Brown_Hat)
    while True:
        goto(0,0)
        for x in range(31):
            goto(x,0)
            #spawn_drone(plant_col_hay)
            if x % 2 == 0:
                spawn_drone(plant_col_tree0)
            else:
                spawn_drone(plant_col_tree1)
        goto(31,0)
        plant_col_tree1()

def main_plant_pumpkin_32x32():
    change_hat(Hats.Brown_Hat)
    while True:
        goto(0,0)
        for x in range(31):
            goto(x,0)
            spawn_drone(plant_col_pumpkin)
        goto(31,0)
        plant_col_pumpkin()
        while True:
            if num_drones() == 1:
                move(North)
                move(East)
                goto(0,0)
                harvest()
                break

def mian_plant_sunflower():
    change_hat(Hats.Brown_Hat)
    while True:
        goto(0,0)
        for x in range(31):
            goto(x,0)
            spawn_drone(plant_col_sumflower)
        goto(31,0)
        plant_col_sumflower()

def plant_col_cactus():
    for y in range(32):
        if can_harvest():
            harvest()
        if get_water()<0.5:
            use_item(Items.Water)
        plant_cactus()
    goto(get_pos_x(),0)
    array = []
    for y in range(32):
        goto(get_pos_x(),y)
        array.append(measure())
    for y in range(32):
        swapped = False
        for yi in range(0, 32-y-1):
            if array[yi] > array[yi+1]:
                array[yi],array[yi+1]=array[yi+1],array[yi]
                goto(get_pos_x(),yi)
                swap(North)
                swapped = True
        if not swapped:
            break
def plant_row_cactus():
    array = []
    for x in range(32):
        goto(x,get_pos_y())
        array.append(measure())
    for x in range(32):
        swapped = False
        for xi in range(0, 32-x-1):
            if array[xi] > array[xi+1]:
                array[xi],array[xi+1]=array[xi+1],array[xi]
                goto(xi,get_pos_y())
                swap(East)
                swapped = True
        if not swapped:
            break

def mian_plant_cactus():
    change_hat(Hats.Brown_Hat)
    while True:
        goto(0,0)
        for x in range(31):
            goto(x,0)
            spawn_drone(plant_col_cactus)
        goto(31,0)
        plant_col_cactus()
        while True:
            if num_drones() == 1:
                break
        for y in range(31):
            goto(0,y)
            spawn_drone(plant_row_cactus)
        goto(0,31)
        plant_row_cactus()
        while True:
            if num_drones() == 1:
                break
        move(North)
        move(East)

if __name__ == '__main__':
    change_hat(Hats.Brown_Hat)
    while True:
        goto(0,0)
        for x in range(31):
            goto(x,0)
            spawn_drone(plant_col_cactus)
        goto(31,0)
        plant_col_cactus()
        while True:
            if num_drones() == 1:
                break
        for y in range(31):
            goto(0,y)
            spawn_drone(plant_row_cactus)
        goto(0,31)
        plant_row_cactus()
        while True:
            if num_drones() == 1:
                break



            plant_hay()
        

def plant_col_tree1():
    while True:
        if get_water() < 0.5:
            use_item(Items.Water)
        if can_harvest():
            harvest()
        if get_pos_y() % 2 != 0:
            plant_tree()
        else:
            plant_hay()

def plant_col_hay():
    for y in range(33):
        harvest()
        set_ground(Grounds.Grassland)
        move(North)
    for y in range(33):
        harvest()
        set_ground(Grounds.Grassland)
        move(South)

def plant_col_carrot():
    for y in range(31):
        if can_harvest():
            harvest()
        if get_water()<0.5:
            use_item(Items.Water)
        plant_carrot()

def plant_colccccc():
    for y in range(32):
        if can_harvest():
            harvest()
        if get_water()<0.5:
            use_item(Items.Water)
        plant_cactus()
    array = []
    for y in range(32):
        pass


if __name__ == '__main__':
    change_hat(Hats.Brown_Hat)
    while True:
        goto(0,0)
        for x in range(31):
            goto(x,0)
            #spawn_drone(plant_col_hay)
            
            if x % 2 == 0:
                spawn_drone(plant_col_tree0)
            else:
                spawn_drone(plant_col_tree1)
        goto(31,0)

                
