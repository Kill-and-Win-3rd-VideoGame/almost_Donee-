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
            self.y += 0.5
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
        self.sword_fighting_sound = pygame.mixer.Sound("sword_fighting.mp3")

    def handle_input(self, keys):
        if keys[pygame.K_UP]:
            self.y -= 0.5
        elif keys[pygame.K_DOWN]:
             self.y += 0.5
        elif keys[pygame.K_LEFT]:
            self.x -= 0.5
        elif keys[pygame.K_RIGHT]:
           self.x += 0.5

    def hit(self, other):
        hit_result = super().hit(other)
        if hit_result:
            self.sword_fighting_sound.play()
        return hit_result

class YellowObject(GameObject):
    sound_playing = False  # Static variable to track sound state

    def __init__(self, imgUrl, size, x, y, speed):
        super().__init__(imgUrl, size, x, y, speed)
        self.sword_fighting_sound = pygame.mixer.Sound("sword_fighting.mp3")

    def sense_and_move(self, player):
        if player.x < self.x:
            self.direction = "left"
        elif player.x > self.x:
            self.direction = "right"
        if player.y < self.y:
            self.direction = "up"
        elif player.y > self.y:
            self.direction = "down"

    # def hit(self, other):
    #     hit_result = super().hit(other)
    #     if hit_result and not YellowObject.sound_playing:  # Play sound only if not already playing
    #         self.sword_fighting_sound.play()
    #         YellowObject.sound_playing = True
    #     return hit_result


class Blood(YellowObject):
    def __init__(self, imgUrl, size, x, y, speed):
        super().__init__(imgUrl, size, x, y, speed)
        self.hit_sound = pygame.mixer.Sound("sword_fighting.mp3")
        self.sound_channel = None  # Store the sound channel for controlling playback

    def hit(self, other):
        hit_result = super().hit(other)
        if hit_result:  # If hit is successful
        #  self.sound_channel = self.hit_sound.play()  # Play the hit sound and store the channel
         return hit_result

