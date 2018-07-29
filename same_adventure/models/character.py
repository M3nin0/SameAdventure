import pygame
from abc import ABCMeta, abstractmethod
from same_adventure.models.weapon import Projectile

class Person(metaclass = ABCMeta):
    """Abstract Class to represent the main characteristics of the characters in the game
    """
    def __init__(self, x, y, width, height, vel = 5):
        """
        :param x: float: X in the pygame window
        :param y: float: Y in the pygame window
        :param width: float: Width of character
        :param height: float: height of character
        :param vel: float: Velocity of character 
        """
        self.__x = x # X in the window
        self.__y = y # Y in the window
        self.__width = width 
        self.__height = height
        self.__vel = vel 
        self.__walk_count = 0 # A index to slice in the list of movements
        self.__standing = True
        self.__walk_right = [] # List of left moviments
        self.__walk_left = [] # List of right moviments
        self.__hitbox = (self.x + 17, self.y + 11, 29, 52) # X, Y, Width, Height
        self.__health = 10
        self.__visible = True

    @abstractmethod
    def draw(self, window):
        """Method to draw in the pygame window
        :param: window: Pygame display instance
        """
        pass

    @abstractmethod
    def move(self):
        """Method to move the character
        """
        pass

    def hit(self, window):
        """A method to represent a hit in character 
        """
        self.health -= 0.1
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render('-10%', 1, (255, 0, 0))
        window.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        
    @property
    def visible(self):
        return self.__visible

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        if self.health > 0:
            self.__health = health
        else:
            self.__visible = False

    @property
    def hitbox(self):
        return self.__hitbox

    @hitbox.setter
    def hitbox(self, hitbox):
        self.__hitbox = hitbox

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
    def width(self):
        return self.__width

    @property
    def height(self): 
        return self.__height

    @property
    def vel(self):
        return self.__vel

    @vel.setter
    def vel(self, vel):
        self.__vel = vel

    @property
    def standing(self):
        return self.__standing

    @standing.setter
    def standing(self, standing):
        self.__standing = standing

    @property
    def walk_count(self): 
        return self.__walk_count

    @walk_count.setter
    def walk_count(self, walk_count):
        self.__walk_count = walk_count

    @property
    def walk_right(self):
        return self.__walk_right

    @walk_right.setter
    def walk_right(self, walk_right):
        self.__walk_right = walk_right

    @property
    def walk_left(self):
        return self.__walk_left

    @walk_left.setter
    def walk_left(self, walk_left):
        self.__walk_left = walk_left


class Player(Person):
    """Character of player
    """

    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)

        self.__is_jump = False
        self.__jump_count = 10
        self.__left = False
        self.__right = False
        # List of image per moviment
        self.walk_right = [pygame.image.load('res/R1.png'), pygame.image.load('res/R2.png'), 
                            pygame.image.load('res/R3.png'),  pygame.image.load('res/R4.png'), 
                            pygame.image.load('res/R5.png'),  pygame.image.load('res/R6.png'),
                            pygame.image.load('res/R7.png'),  pygame.image.load('res/R8.png'), 
                            pygame.image.load('res/R9.png') ]
        self.walk_left = [pygame.image.load('res/L1.png'),  pygame.image.load('res/L2.png'), 
                            pygame.image.load('res/L3.png'),  pygame.image.load('res/L4.png'), 
                            pygame.image.load('res/L5.png'),  pygame.image.load('res/L6.png'), 
                            pygame.image.load('res/L7.png'),  pygame.image.load('res/L8.png'), 
                            pygame.image.load('res/L9.png') ]
        self.__character_image = pygame.image.load('res/standing.png')
        self.__bullets = []
        self.__score = 0
    
    def move(self):
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                if self.left:
                    facing = -1
                elif self.right:
                    facing = 1
                else:
                    facing = 1
                if len(self.__bullets) < 5:
                    self.__bullets.append(Projectile(self.x + self.width // 2, round(self.y + self.height // 2), 6, (0, 0, 0), facing))

            # Controle das posições do usuário
            if keys[pygame.K_LEFT] and self.x > self.vel:
                self.x -= self.vel
                self.left = True
                self.right = False
                self.standing = False
            elif keys[pygame.K_RIGHT] and self.x < 500 - self.width - self.vel:
                self.x += self.vel
                self.right = True
                self.left = False
                self.standing = False
            else:
                self.standing = True
                self.walk_count = 0

            if not (self.is_jump):
                if keys[pygame.K_UP]:
                    self.is_jump = True
                    self.right = False
                    self.left = False
                    self.walk_count = 0
            else:
                if self.jump_count >= -10:
                    neg = 1
                    if self.jump_count < 0:
                        neg = -1
                    self.y -= (self.jump_count ** 2) * 0.5 * neg
                    self.jump_count -= 1
                else:
                    self.is_jump = False
                    self.jump_count = 10
    
    def draw(self, window):
        if self.health > 0:
            self.move()

            if self.walk_count + 1 >= 27:
                self.walk_count = 0
                    
            if not (self.standing):
                # To draw the correct moviments
                if self.left:
                    window.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
                    self.walk_count += 1
                elif self.right:
                    window.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
                    self.walk_count += 1
            else:
                if self.right:
                    window.blit(self.walk_right[0], (self.x, self.y))
                else:
                    window.blit(self.walk_left[0], (self.x, self.y))
            self.hitbox = (self.x + 17, self.y + 11, 29, 52) # Move the hitbox
            # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2) # Draw a rect in character

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def is_jump(self):
        return self.__is_jump
    
    @is_jump.setter
    def is_jump(self, is_jump):
        self.__is_jump = is_jump

    @property
    def jump_count(self):
        return self.__jump_count

    @jump_count.setter
    def jump_count(self, value):
        self.__jump_count = value

    @property
    def character_image(self):
        return self.__character_image

    @property
    def bullets(self):
        return self.__bullets
    
    def remove_bullet(self, bullet):
        self.__bullets.remove(bullet) 

class Orc(Person):
    def __init__(self, x, y, width, height, end):
        super(Orc, self).__init__(x, y, width, height, 3)
        
        self.walk_right = [pygame.image.load('res/R1E.png'),   pygame.image.load('res/R2E.png'), 
                            pygame.image.load('res/R3E.png'),  pygame.image.load('res/R4E.png'), 
                            pygame.image.load('res/R5E.png'),  pygame.image.load('res/R6E.png'),
                            pygame.image.load('res/R7E.png'),  pygame.image.load('res/R8E.png'), 
                            pygame.image.load('res/R9E.png'),  pygame.image.load('res/R10E.png'),
                            pygame.image.load('res/R11E.png')]
        self.walk_left = [pygame.image.load('res/L1E.png'),    pygame.image.load('res/L2E.png'), 
                            pygame.image.load('res/L3E.png'),  pygame.image.load('res/L4E.png'), 
                            pygame.image.load('res/L5E.png'),  pygame.image.load('res/L6E.png'), 
                            pygame.image.load('res/L7E.png'),  pygame.image.load('res/L8E.png'), 
                            pygame.image.load('res/L9E.png'),  pygame.image.load('res/L10E.png'),
                            pygame.image.load('res/L11E.png') ]
        self.__end = end
        self.__path = [self.x, self.__end]

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.__path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.__path[0]:
                self.x += self.vel
            else: 
                self.vel = self.vel * -1
                self.walk_count = 0

    def draw(self, window):

        if self.health > 0:
            self.move()

            # The limit of walk count (Verify the limit)
            if self.walk_count + 1 >= 33:
                self.walk_count = 0

            if self.vel > 0:
                window.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            else:
                window.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1

            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

            self.hitbox =  (self.x + 17, self.y + 2, 31, 57)
