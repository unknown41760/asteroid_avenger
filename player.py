from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.lives = PLAYER_LIVES
        self.save_timer = PLAYER_SAVE_TIMER
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, COLOR_WHITE, self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward_vector * PLAYER_SPEED * dt

    def shoot(self):
        if (self.timer <= 0):
            s = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            s.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        if(self.timer > 0):
            self.timer -= dt
        if(self.save_timer > 0):
            self.save_timer -= dt
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
