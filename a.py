import pygame

pygame.init()

screen = pygame.display.set_mode((1500,1000))
x = 750
ix =750
iy =750
y = 500
z = 50
running = True
clock = pygame.time.Clock()
delta_time = 0.1

muki_png = pygame.image.load("muki.png").convert()
muki_png.set_colorkey(muki_png.get_at((0, 0)))
JUMPING = True
Y_GRAVITY = 0.33
JUMP_HEIGHT = 30
Y_VELOCITY = JUMP_HEIGHT
JUMP_HEIGHT1 = 0
Y_VELOCITY1 = JUMP_HEIGHT1
Y_GRAVITY1 = 2.5

muki_png = pygame.transform.smoothscale(muki_png,(80,80))
font = pygame.font.Font(None, size=30)
# muki_png = pygame.transform.scale(muki_png,(200,200))
sky = pygame.image.load("sky.png").convert()
island = pygame.image.load("ISLAND.png").convert()
island.set_colorkey((255,255,255))
player_v = -10
Tile_Size = 5
island = pygame.transform.smoothscale(island,(100,100))
# class title(pygame.rect):
#     def __init__(self, x ,y , image):
#         pygame.Rect.__init__(self,x,y,Tile_Size, Tile_Size)
#         self.image = image
# def create_map() :
#     for i in range(4):
#         tile = title(x + i*Tile_Size, y + i*Tile_Size, island)
#         title.append(tile)
i1 = 100
i2 = 200
i3 =300
i4 =400
i5 =500
i6 =600
i7 =700
i8 =800
i9 =900
i10 =1000
ix1 =100
ix2 =200
ix3 =300
ix4 =400
ix5 =500
ix6 =600
ix7 =700
ix8 =800
ix9 =900
ix10 =1000
def xlevel_1():
    
    global i1
    global i1
    global i1
    global i1
    global i2
    global i3
    global i4
    global i5
    global i6
    global i7
    global i8
    global i9
    global i10
    global ix1
    global ix1
    global ix1
    global ix1
    global ix2
    global ix3
    global ix4
    global ix5
    global ix6
    global ix7
    global ix8
    global ix9
    global ix10

    i1 = 100
    i2 = 200
    i3 =300
    i4 =400
    i5 =500
    i6 =600
    i7 =700
    i8 =800
    i9 =900
    i10 =1000
    ix1 =100
    ix2 =200
    ix3 =300
    ix4 =400
    ix5 =500
    ix6 =600
    ix7 =700
    ix8 =800
    ix9 =900
    ix10 =1000
levl1_list_rect = [
island.get_rect(center=(i1,ix1- z )),
island.get_rect(center=(i2,ix2- z )),
island.get_rect(center=(i3,ix3- z )),
island.get_rect(center=(i4,ix4- z )),
island.get_rect(center=(i5,ix5- z )),
island.get_rect(center=(i6,ix6- z )),
island.get_rect(center=(i7,ix7- z )),
island.get_rect(center=(i8,ix8- z )),
island.get_rect(center=(i9,ix9- z )),
island.get_rect(center=(i10,ix10 - z))]
def level_1():
    global levl1_list_rect
    screen.blit(island, (i1,ix1))
    screen.blit(island, (i2,ix2))
    screen.blit(island, (i3,ix3))
    screen.blit(island, (i4,ix4))
    screen.blit(island, (i5,ix5))
    screen.blit(island, (i6,ix6))
    screen.blit(island, (i7,ix7))
    screen.blit(island, (i8,ix8))
    screen.blit(island, (i9,ix9))
    screen.blit(island, (i10,ix10))
    levl1_list_rect = [
    island.get_rect(center=(i1,ix1- z )),
    island.get_rect(center=(i2,ix2- z )),
    island.get_rect(center=(i3,ix3- z )),
    island.get_rect(center=(i4,ix4- z )),
    island.get_rect(center=(i5,ix5- z )),
    island.get_rect(center=(i6,ix6- z )),
    island.get_rect(center=(i7,ix7- z )),
    island.get_rect(center=(i8,ix8- z )),
    island.get_rect(center=(i9,ix9- z )),
    island.get_rect(center=(i10,ix10 - z))]

on_ground = False

def quicksand():
    for island_rect in levl1_list_rect:
        if muki_rect.colliderect(island_rect):
            Y_VELOCITY = -5
    

sky = pygame.transform.smoothscale(sky, (1500, 1000))
pillarx = 100
pillary = 100
z = 5
x_stopped = False
muki_rect = muki_png.get_rect(center=(x,y))
island_rect = island.get_rect(center=(x,y))


while running == True:
    on_ground =True
    screen.blit(sky,(0,0))
    muki_rect = muki_png.get_rect(center=(x,y))
    island_rect = island.get_rect(center=(x,y))
    old_x = x
    xlevel_1()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] :
        JUMPING= True
    if keys_pressed[pygame.K_d] :
        x = x + 7.5
    if keys_pressed[pygame.K_a] :
        x = x - 7.5
    if JUMPING == True:
        y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
    for island_rect in levl1_list_rect:
        if muki_rect.colliderect(island_rect):
            JUMPING = False
            Y_VELOCITY = JUMP_HEIGHT
    # for island_rect in levl1_list_rect:
    #     if muki_rect.colliderect(island_rect) == False:
    #         JUMPING = True
    if y == 1000:
        y = 0
    if x == 1500:
        x = 0
    if 1 == 1:
        y -= Y_VELOCITY1
        Y_VELOCITY1 -= Y_GRAVITY1
    for island_rect in levl1_list_rect:
        if muki_rect.colliderect(island_rect):
            JUMPING = False
            Y_VELOCITY1 = JUMP_HEIGHT1
    # for island_rect in levl1_list_rect:
    muki_rect = muki_png.get_rect(topleft=(x + 50, y-20))
    for island_rect in levl1_list_rect:

        if muki_rect.colliderect(island_rect):

            # moving right into wall
            if x > old_x - 50:
                x = island_rect.left - muki_rect.width

            # moving left into wall
            if x < old_x - 100:
                x = island_rect.right -50
                x = island_rect.right - 50
    screen.blit(muki_png,(x,y))
    # screen.blit(island, (ix,iy))DDW
    level_1()
    screen.blit(island, (100,100))
    for event in pygame.event.get():
        # to rener muki
        if event.type == pygame.QUIT:
            running = False
            # to be able to quit
            pygame.display.flip()
    pygame.display.flip()
    clock.tick(60)
    #to get fps
pygame.quit()



