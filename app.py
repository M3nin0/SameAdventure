import pygame; pygame.init()
from same_adventure.models.character import Player, Orc
from same_adventure.models.scenario import Scenario
from same_adventure.config.window import Window
from same_adventure.models.collision import person_collision

scenario = Scenario('res/bg.png', 'res/music.mp3')
window = Window('Same adventure', (500, 480), pygame.time.Clock(), scenario)

# Objects in window
objects = [Player(250, 400, 64, 64), Orc(100, 410, 60, 60, 450)]
kills = 0

scenario.play_music()

run = True
while run:
    window.clock.tick(45) # 60 images per second
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for obj in objects:
        if type(obj).__name__ == 'Player':
            for bullet in obj.bullets:
                if bullet not in objects:
                    objects.append(bullet)
        if type(obj).__name__ == 'Orc':
            if not obj.visible:
                objects.remove(obj); kills += 1
                for kill in range(0, kills + 1):
                    objects.append(Orc(100 + (5 * kill), 410, 60, 60, 450))

    person_collision(objects, window.display)
    window.redraw_game_window(objects)

    for obj in objects:
        if type(obj).__name__ == 'Player':
            for bullet in obj.bullets:
                if bullet.to_remove:
                    objects.remove(bullet)
                    obj.remove_bullet(bullet)
                if bullet.is_collision(objects, window.display):
                    obj.score += 1
                
pygame.quit()
