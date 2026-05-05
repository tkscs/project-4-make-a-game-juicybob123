import pygame

pygame.init()

screen = pygame.display.set_mode((1000,1000))
x = 100
IBx =200
Iby =200
y = 100
running = True
clock = pygame.time.Clock()
delta_time = 0.1
IB = pygame.image.load("IB.JPG").convert()
muki_png = pygame.image.load("muki.png").convert()
muki_png.set_colorkey(muki_png.get_at((0, 0)))
IB.set_colorkey(IB.get_at((0, 0)))
font = pygame.font.Font(None, size=30)
muki_png = pygame.transform.scale(muki_png,(200,200))
def check_movement():
    global y
    global x
    i = 0
    
    if event.type == pygame.KEYDOWN and y<800:
        if event.key == pygame.K_s:
                y = y +20
    if event.type == pygame.KEYDOWN and x<800 :
        if event.key == pygame.K_d:
                x = x +20
    if event.type == pygame.KEYDOWN and x>-20:
        if event.key == pygame.K_a:
                x = x -20
    if event.type == pygame.KEYDOWN and y>0:
        if event.key == pygame.K_w:
                y = y -20
def check_movement1():
    global Iby
    global IBx
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and y<800:
                Iby = Iby +20
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and x<800:
                IBx = IBx +20
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and x>-20:
                IBx = IBx -20
    if event.type == pygame.KEYDOWN  and y>0:
        if event.key == pygame.K_UP:
                Iby = Iby -20

while running == True:
    screen.fill((0,0,255))
    pygame.transform.scale(muki_png, (0.5,0.5))
    screen.blit(IB,(IBx,Iby))    
    screen.blit(muki_png,(x,y))
    screen.blit(muki_png,(x,y))
    text = font.render("Hello world", True, (0,0,0))
    for event in pygame.event.get():
        check_movement()
        check_movement1()
        # to rener muki
        if event.type == pygame.QUIT:
            running = False
            # to be able to quit
        pygame.display.flip()
    clock.tick(60)
    #to get fps
pygame.quit()
























# # import pygame
# import pygame
# from pygame import *
# pygame.init()
# color1 = pygame.Color(0, 0, 0)         # Black
# color2 = pygame.Color(255, 255, 255)   # White
# color3 = pygame.Color(128, 128, 128)   # Grey
# color4 = pygame.Color(255, 0, 0)       # red
# #Game loop begins
# DISPLAYSURF = pygame.display.set_mode((1000,1000))
# FPS = pygame.time.Clock()
# FPS.tick(30)
# def update(self):
#     if key.get_just_pressed(K_DOWN):
#         self.rect.move(-5,0)
        
# while True:
#     object1 = pygame.Rect((20, 50), (50, 100))
#     object2 = pygame.Rect((10, 10), (100, 100))
    
#     print(object1.colliderect(object2))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             pygame.sys.exit()
#     pygame.display.update()