import pygame
import random
import math

class GameObject:
    def __init__(self, imgUrl, size, x, y, speed):
        self.imgUrl = imgUrl
        self.size = size
        self.x = x
        self.y = y
        self.sword_length = 50 
        self.speed = speed  
        self.direction = random.choice(["up", "down", "left", "right"])
        self.health = 100  

    def draw(self, screen):
        img = pygame.image.load(self.imgUrl)  
        screen.blit(img, (self.x, self.y))
          
    def move(self):
        if self.direction == "up":
            self.y -= 0.5
        elif self.direction == "down":
            self.y +=0.5
        elif self.direction == "left":
            self.x -= 0.5
        elif self.direction == "right":
            self.x += 0.5

        
        if random.random() < 0.001:
            self.direction = random.choice(["up", "down", "left", "right"])

        
        if self.x < 0:
            self.x = 0
        elif self.x > 800:
            self.x = 800
        if self.y < 0:
            self.y = 0
        elif self.y > 400:
            self.y = 400

    def hit(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if distance <= self.sword_length + other.size:
            return True
        return False

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Player(GameObject):
    def __init__(self, imgUrl, size, x, y, speed):
        super().__init__(imgUrl, size, x, y, speed)
    def handle_input(self, keys):
        if keys[pygame.K_UP]:
            self.y -= 0.5
        elif keys[pygame.K_DOWN]:
             self.y +=0.5
        elif keys[pygame.K_LEFT]:
            self.x -= 0.5
        elif keys[pygame.K_RIGHT]:
           self.x += 0.5

class YellowObject(GameObject):
    def __init__(self, imgUrl, size, x, y, speed):
        super().__init__(imgUrl, size, x, y, speed)

    def sense_and_move(self, player):
        if player.x < self.x:
            self.direction = "left"
        elif player.x > self.x:
            self.direction = "right"
        if player.y < self.y:
            self.direction = "up"
        elif player.y > self.y:
            self.direction = "down"


class Blood(YellowObject):
    def __init__(self, imgUrl, size, x, y, speed):
        super().__init__(imgUrl, size, x, y, speed)