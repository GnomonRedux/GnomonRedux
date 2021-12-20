import pygame
import pygame_sandbox_objects_010 as o
import pygame_sandbox_colors_010 as c
import pygame_sandbox_dialogue_pad_010 as d


welcome_msg = 'pygame_sandbox_app_000.py open!'
print(o.buffer + welcome_msg + o.buffer)


black = c.grab_color('black').tuple
white = c.grab_color('white').tuple
red = c.grab_color('red').tuple
green = c.grab_color('green').tuple
blue = c.grab_color('blue').tuple
color_list = [black, white, red, green, blue]


win_x, win_y = 350,350
FPS = 20
win_color = blue #tuple(0,0,255)
bg_color = black


running = False
ball_size = 20
ball = o.Ball(white, ball_size, win_x, win_y)
sprite_list = [ball]
sprite_group = pygame.sprite.Group(sprite_list)


bat_size = 15
player_1 = o.Bat(blue, bat_size, win_x, win_y, 'Left')
player_2 = o.Bat(green, bat_size, win_x, win_y, 'Bottom')
player_list = [player_1]
player_group = pygame.sprite.Group(player_list)

ground_offset = 100
test_dialogue = "My name is Ozymandias, King of Kings"
test_wrap = 15
test_dialogue_group = d.make_text_frame_g(test_dialogue, test_wrap, 150,50,
                                          (win_x//2-150//2), win_y-ground_offset, FPS)


win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('pygame_sandbox_app_000')
win.fill(win_color)
pygame.display.update()



def draw_main_screen_manually():
    win.fill(bg_color)
    for item in sprite_list:
        item.update()
        win.blit(item.image, (item.rect))
    for player in player_list:
        player.update()
        win.blit(player.image, (player.rect))
    pygame.display.update()


def draw_main_screen_by_group():
    win.fill(bg_color)
    sprite_group.update() #calls .update() on each sprite
    sprite_group.draw(win)
    player_group.update()
    player_group.draw(win)

    test_dialogue_group.update()
    test_dialogue_group.draw(win)
    
    pygame.display.update()


def check_input():
    global running
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        print('ESCAPE' + (o.buffer*2))
        running = False
    if keys[pygame.K_UP]:
        #do stuff to player_1.y
        print('^ up')
    if keys[pygame.K_DOWN]:
        print('v down')
    if keys[pygame.K_LEFT]:
        print('< left')
    if keys[pygame.K_RIGHT]:
        print('> right')
    if keys[pygame.K_SPACE]:
        print('__ space')


def check_collisions():
    collide = pygame.sprite.spritecollide(player_1, sprite_group, False)
    for c in collide:
        #c.whatever()
        print('Pow!')
 

def game_app():
    global running
    pygame.init()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        check_input()
        #check_collisions()
        #draw_main_screen_manually()
        draw_main_screen_by_group()
        clock.tick(FPS)
        
    pygame.quit()



game_app()




