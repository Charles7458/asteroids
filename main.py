# this allows us to use code from 
# the open-source pygame library
# throughout this file

import pygame
from constants import * 
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    shots =  pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroidField = AsteroidField()
    PLAYER = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    score = 0
    kills = 0
    font = pygame.font.SysFont(None, 24, True)
    # text = font.render(f"Score: {score}", True, (255,255,255))

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # closes the screen when the X button is clicked
                return
            
        screen.fill("black")
        
        text = font.render(f"Score: {int(score)}", True, (255,255,255))
        text2 = font.render(f"Asteroids destroyed: {kills}", True, (255, 255, 255))
        
        screen.blit(text, (20, 20))
        screen.blit(text2, (20, 50))
        
        for item in drawable:
            item.draw(screen)
            
        updatable.update(dt)
        
        for aster in asteroids:
            for bullet in shots:
                if aster.collision_check(bullet):
                    aster.split()
                    bullet.kill()
                    kills+=1
        
        for i in asteroids:
            if i.collision_check(PLAYER):
                print("Game Over")
                print(f"Score: {int(score)}s")
                print(f"Asteroids destroyed: {kills}")
                exit()
            
        #last step
        pygame.display.flip()
        
        dt = clock.tick(60)/1000 #limits fps to 60fps
        score += dt
        

if __name__=='__main__':
    main()
