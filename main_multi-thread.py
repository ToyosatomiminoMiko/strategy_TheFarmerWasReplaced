from f0 import *

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

                
