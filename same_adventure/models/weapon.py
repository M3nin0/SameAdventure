import os
import pygame

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__color = color
        self.__facing = facing
        self.__vel = 8 * facing
        self.__to_remove = False

    def move(self):        
        if self.x < 500 and self.x > 0:
            self.x += self.vel
            self.__to_remove = False
        else:
            self.__to_remove = True

    def draw(self, window):
        self.move()
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def is_collision(self, objects, window):
        """Detect if the bullet in collision
        :param objects: list: List of objects in the window
        """

        for obj in objects:
            if type(obj).__name__ == 'Orc':
                # Verify if the bullet in collision
                if self.y - self.radius < obj.hitbox[1] + obj.hitbox[3] and self.y + self.radius > obj.hitbox[1]:
                    if self.x + self.radius > obj.hitbox[0] and self.x - self.radius < obj.hitbox[0] + obj.hitbox[2]:
                        obj.hit(window)
                        return True
                else:
                    return False
                     
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def color(self):
        return self.__color

    @property
    def vel(self):
        return self.__vel

    @property
    def to_remove(self):
        return self.__to_remove
