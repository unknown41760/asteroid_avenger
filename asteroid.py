from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return 0
        angle = random.uniform(20,50)
        
        spawn_1 = Asteroid (self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        spawn_1.velocity = self.velocity.rotate(angle) * 1.2

        spawn_2 = Asteroid (self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        spawn_2.velocity = self.velocity.rotate(-angle) * 1.2