import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    dt = 0
    score = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shot_group, updatable, drawable)

    hero = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    calipso = AsteroidField()

    font = pygame.font.Font(None, 36)

    while(True):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        
        for a in asteroids_group:
            if(hero.save_timer <= 0):
                if (hero.collision_check(a)):
                    hero.lives -= 1
                    score -= SCORE_PENALTY
                    hero.position.x = SCREEN_WIDTH/2
                    hero.position.y = SCREEN_HEIGHT/2
                    hero.save_timer = PLAYER_SAVE_TIMER

                    if(hero.lives <= 0):
                        print("Game over!")
                        return 0
        
            for s in shot_group:
                if(s.collision_check(a)):
                    score += SCORE_INCREMENT
                    a.split()
                    s.kill()

        for d in drawable:
            d.draw(screen)
        score_text = font.render(f"Score: {score} Lives: {hero.lives}", True, COLOR_WHITE)
        screen.blit(score_text, (10,10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
