import pygame
import math
import fighting
import random
import Room
import Characters

def Start_Game():
    pygame.init()
    pygame.mixer.stop()
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 400
    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    window = pygame.display.set_mode(WINDOW_SIZE)

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Kill And Win")

    background_image = pygame.image.load("floor_black.jpg")
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    frame_width = 600
    frame_height = 400

    frame_x = (WINDOW_WIDTH - frame_width) // 2
    frame_y = (WINDOW_HEIGHT - frame_height) // 2

    frame_rect = pygame.Rect(frame_x, frame_y, frame_width, frame_height)
    font = pygame.font.Font(None, 36)

    # Define rooms
    rooms = [
        Room.Room("Living Room", "5.jpg", (frame_x + 50, frame_y + 50), 150, 150),
        Room.Room("Bathroom", "6.jpg", (frame_x + 200, frame_y + 50), 150, 150),
        Room.Room("Kitchen", "1.jpg", (frame_x + 350, frame_y + 50), 150, 150),
        Room.Room("Hall", "2.jpg", (frame_x + 50, frame_y + 200), 150, 150),
        Room.Room("Bedroom", "3.jpg", (frame_x + 200, frame_y + 200), 150, 150),
        Room.Room("Poker Room", "4.jpg", (frame_x + 350, frame_y + 200), 150, 150)
    ]
    player = Characters.Player("pablo.png", 100, 0, 100, 1) # Create an instance of the Player class

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.handle_input(keys)  

        for room in rooms:
            if room.contains_point((player.x, player.y)):
                number = random.randint(1, 2)
                fighting.Start_Game(1)

        screen.blit(background_image, (0, 0))

        for room in rooms:
            room.draw(screen, (255, 255, 255))

        player.draw(screen)

        pygame.display.flip()

    pygame.quit()

