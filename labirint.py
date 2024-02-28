# Create your game in this file!
from pygame import *
window = display.set_mode((700,500))
display.set_caption('Labirin')

class GameSprite(sprite.Sprite):
    def __init__ (self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

wall_1 = GameSprite('net (2).png', 200, 100, 200, 350)
wall_2 = GameSprite('net (2).png', 200,100, 200, 50)
wall_3 = GameSprite('netttttt.png', 100,250, 366, 125)
barriers = sprite.Group()
barriers.add(wall_1)
barriers.add(wall_2)
barriers.add(wall_3)
last = GameSprite('pink.png', 70,70,600,400)
gun = sprite.Group()
monsters = sprite.Group()

class Player(GameSprite):
    def __init__ (self,picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self,barriers, False)
        if self.x_speed > 0 :
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self,barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        if self.rect.x > 650:
            self.rect.x = 650
        elif self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 470:
            self.rect.y = 470
        elif self.rect.y <- 10:
            self.rect.y = -10
    def fire(self):
        peluru = Bullet('badminton.png' ,20,20,self.rect.right,self.rect.centery - 20,3)
        gun.add(peluru)

player = Player('dinosaur.png',60,60,5,400,0,0)

class Enemy(GameSprite):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture,w,h,x,y)
        self.speed = speed 
    def update(self):
        if self.rect.x <= 470:
            self.direction = "kanan"
        if self.rect.x >= 700 - 85:
            self.direction = "kiri"
        if self.direction == 'kiri':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

monster = Enemy('dinosaur (1).png', 60,60,650,270,2)
monsters.add(monster)

class Bullet(GameSprite):
    def __init__(self, picture, w,h,x,y,speed):
        super().__init__(picture,w,h,x,y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 700 + 10:
            self.kill()

final = transform.scale(image.load('bckground.jpg'), (700,500))
font.init()
font = font.SysFont('Kristen ITC', 55)
win = font.render('MENANG', True, (0,0,0))
lose = font.render('KALAH', True, (0,0,0))

run = True
finish = False
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                player.x_speed -= 5
            elif e.key == K_RIGHT:
                player.x_speed += 5
            elif e.key == K_UP:
                player.y_speed -= 5
            elif e.key == K_DOWN:
                player.y_speed += 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                player.x_speed = 0
            elif e.key == K_RIGHT:
                player.x_speed = 0
            elif e.key == K_UP:
                player.y_speed = 0
            elif e.key == K_DOWN:
                player.y_speed = 0
            elif e.key == K_SPACE:
                player.fire()
    
    if finish != True:
        window.fill((233,205,208))
        barriers.update()
        barriers.draw(window)
        last.reset()
        player.update() 
        player.reset()
        monsters.update()
        monsters.draw(window)
        gun.update()
        gun.draw(window)
        sprite.groupcollide(gun, barriers, True,False)
        sprite.groupcollide(gun, monsters, True, True)
        if sprite.collide_rect(player,last):
            finish = True
            window.blit(final, (0,0))
            window.blit(win, (210,220))
        if sprite.spritecollide(player,monsters, False):
            finish = True
            window.blit(final, (0,0))
            window.blit(lose, (210,220))
    display.update()