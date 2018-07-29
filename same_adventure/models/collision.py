def person_collision(objects, window):
    """Function to make a collision system
    """

    for obj_1 in objects:
        for obj_2 in objects:
            if type(obj_1).__name__ == 'Player' and type(obj_2).__name__ == 'Orc':
                if obj_1.hitbox[1] < obj_2.hitbox[1] + obj_2.hitbox[3] and obj_1.hitbox[1] + obj_1.hitbox[3] > obj_2.hitbox[1]:
                        if obj_1.hitbox[0] + obj_1.hitbox[2] > obj_2.hitbox[0] and obj_1.hitbox[0] < obj_2.hitbox[0] + obj_2.hitbox[2]:
                            obj_1.hit(window)
