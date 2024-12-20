def till_farm(size):
    i = 0
    while i < size: 
        i = i + 1
        j = 0
        while j < size:
            j = j + 1
            till()
            move(North)
        move(East)


def plant_row_grass(length):
    i = 0
    while i < length:
        i = i + 1
        harvest()
        move(North)

def plant_row_bush(length):
    i = 0
    while i < length:
        i = i + 1
        plant(Entities.Bush)
        if can_harvest():
            harvest()
            plant(Entities.Bush)
            move(North)
        else:
            move(North)

def plant_row_carrot(length):
    i = 0
    while i < length:
        i = i + 1
        if num_items(Items.Carrot_Seed) < 10:
            trade(Items.Carrot_Seed)
        if can_harvest():
            harvest()
        plant(Entities.Carrots)
        move(North)

def plant_row_pumpkin(length):
    i = 0
    while i < length:
        i = i + 1
        if num_items(Items.Pumpkin_Seed) < 10:
            trade(Items.Pumpkin_Seed)
        if can_harvest():
            harvest()
            plant(Entities.Pumpkin)
            move(North)
        else:
            move(North)