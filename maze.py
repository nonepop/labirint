from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))




class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

        if keys[K_DOWN] and self.rect.y < win_hight - 80:
            self.rect.y += self.speed

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed


class Enemy(GameSprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__(player_image, x, y, speed)
        self.direction = 'left'

    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'

        if self.rect.x > win_width - 80:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed



class Wall(sprite.Sprite):
    def __init__(self, c1, c2, c3, wall_width, wall_height, wall_x, wall_y):
        super().__init__()
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((c1,c2,c3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        




        
         





win_width = 700
win_hight = 500
window = display.set_mode((win_width,win_hight))
background = transform.scale(image.load("background.jpg"),(win_width,win_hight))
mixer.init()
font.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

sprite1 = Player("raketa.png",20,20,8)
sprite2 = Enemy("kala.png",win_width - 80,280,5)
sprite3 = GameSprite("kopt.png",win_width - 120,win_hight - 80,0)
sprite4 = Wall(1,20,100,20,400,100,5)
sprite5 = Wall(1,20,100,150,20,100,5)
sprite6 = Wall(1,20,100,20,370,230,125)
sprite7 = Wall(1,20,100,20,370,350,5)





font = font.Font(None, 70)
win = font.render("YOU WIN", True, (255,215,0))
lose = font.render("YOU LOSE", True, (255,0,0))
finish = False
game = True
FPS = 60
clock = time.Clock()
while game:
    


    for e in event.get():
        if e.type == QUIT:
            game = False




    if finish != True:
        window.blit(background,(0,0))
        sprite1.reset()
        sprite2.reset()
        sprite3.reset()
        sprite1.update()
        sprite2.update()
        sprite4.draw_wall()
        sprite5.draw_wall()
        sprite6.draw_wall()
        sprite7.draw_wall()
        

    if sprite.collide_rect(sprite1, sprite3):
        window.blit(win,(200,200))
        finish = True
        money.play()

    if sprite.collide_rect(sprite1, sprite2) or sprite.collide_rect(sprite1, sprite4) or sprite.collide_rect(sprite1, sprite5) or sprite.collide_rect(sprite1, sprite6) or sprite.collide_rect(sprite1, sprite7):
        window.blit(lose,(200,200))
        finish = True
        kick.play()

        

    


    display.update()
    clock.tick(FPS)
