import pygame
import time

from pygame.locals import *


resolution = [6200, 2488]
flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode(resolution, flags, 16)
#screen = pygame.display.set_mode((6200, 2488))

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
clock = pygame.time.Clock()
#image_path = '/data/data/Gnom_VS_AgrGnom.myapp/files/app'

current_scene = None
def switch_scene(scene):
    global current_scene
    current_scene = scene

def scene_menu():
    class Menu:
        def __init__(self):
            self._option_surfaces = []
            self._callbacks = []
            self._current_option_index = 0

        def append_option(self, option, callback):
            self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
            self._callbacks.append(callback)

        def switch(self, direction):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

        def select(self):
            self._callbacks[self._current_option_index]()

        def draw(self, surf, x, y, option_y_padding):
            for (i, option) in enumerate(self._option_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self._current_option_index:
                    pygame.draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)

    menu = Menu()

    menu.append_option('Играть за Элину', lambda: switch_scene(scene_menu_Elina()))
    menu.append_option('Играть за Cемена', lambda: switch_scene(scene_menu_Semen()))
    menu.append_option('Выйти', quit)

    running1 = True
    while running1:
        screen.fill((0, 0, 0))
        menu.draw(screen, 500, 250, 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                menu.switch(-1)
                # time.sleep(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                menu.switch(1)
                # time.sleep(3)

            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                menu.select()

def scene_menu_Elina():
    class Menu:
        def __init__(self):
            self._option_surfaces = []
            self._callbacks = []
            self._current_option_index = 0

        def append_option(self, option, callback):
            self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
            self._callbacks.append(callback)

        def switch(self, direction):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

        def select(self):
            self._callbacks[self._current_option_index]()

        def draw(self, surf, x, y, option_y_padding):
            for (i, option) in enumerate(self._option_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self._current_option_index:
                    pygame.draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)

    menu = Menu()

    menu.append_option('Уровень 1', lambda: switch_scene(scene1E()))
    menu.append_option('Уровень 2', lambda: scene2E())
    menu.append_option('Уровень 3', lambda: scene3E())
    menu.append_option('Выйти', quit)

    running1 = True
    while running1:
        screen.fill((0, 0, 0))
        menu.draw(screen, 500, 250, 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                menu.switch(-1)
                # time.sleep(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                menu.switch(1)
                # time.sleep(3)

            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                menu.select()

def scene_menu_Semen():
    class Menu:
        def __init__(self):
            self._option_surfaces = []
            self._callbacks = []
            self._current_option_index = 0

        def append_option(self, option, callback):
            self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
            self._callbacks.append(callback)

        def switch(self, direction):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

        def select(self):
            self._callbacks[self._current_option_index]()

        def draw(self, surf, x, y, option_y_padding):
            for (i, option) in enumerate(self._option_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self._current_option_index:
                    pygame.draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)

    menu = Menu()

    menu.append_option('Уровень 1', lambda: switch_scene(scene1S()))
    menu.append_option('Уровень 2', lambda: scene2S())
    menu.append_option('Уровень 3', lambda: scene3S())
    menu.append_option('Выйти', quit)

    running1 = True
    while running1:
        screen.fill((0, 0, 0))
        menu.draw(screen, 500, 250, 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                menu.switch(-1)
                # time.sleep(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                menu.switch(1)
                # time.sleep(3)

            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                menu.select()

def scene_proig1E():
    class Menu:
        def __init__(self):
            self._option_surfaces = []
            self._callbacks = []
            self._current_option_index = 0

        def append_option(self, option, callback):
            self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
            self._callbacks.append(callback)

        def switch(self, direction):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

        def select(self):
            self._callbacks[self._current_option_index]()

        def draw(self, surf, x, y, option_y_padding):
            for (i, option) in enumerate(self._option_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self._current_option_index:
                    pygame.draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)

    menu = Menu()

    menu.append_option('Играть снова', lambda: switch_scene(scene1E()))
    menu.append_option('Выйти', quit)

    running1 = True
    while running1:
        screen.fill((0, 0, 0))
        menu.draw(screen, 500, 250, 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                menu.switch(-1)
                # time.sleep(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                menu.switch(1)
                # time.sleep(3)

            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                menu.select()


def scene_proig2E():
    class Menu:
        def __init__(self):
            self._option_surfaces = []
            self._callbacks = []
            self._current_option_index = 0

        def append_option(self, option, callback):
            self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
            self._callbacks.append(callback)

        def switch(self, direction):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

        def select(self):
            self._callbacks[self._current_option_index]()

        def draw(self, surf, x, y, option_y_padding):
            for (i, option) in enumerate(self._option_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self._current_option_index:
                    pygame.draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)

    menu = Menu()

    menu.append_option('Играть снова', lambda: switch_scene(scene2E()))
    menu.append_option('Выйти', quit)

    running1 = True
    while running1:
        screen.fill((0, 0, 0))
        menu.draw(screen, 500, 250, 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                menu.switch(-1)
                # time.sleep(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                menu.switch(1)
                # time.sleep(3)

            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                menu.select()



def scene_proig3E():
    class Menu:
        def __init__(self):
            self._option_surfaces = []
            self._callbacks = []
            self._current_option_index = 0

        def append_option(self, option, callback):
            self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
            self._callbacks.append(callback)

        def switch(self, direction):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

        def select(self):
            self._callbacks[self._current_option_index]()

        def draw(self, surf, x, y, option_y_padding):
            for (i, option) in enumerate(self._option_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self._current_option_index:
                    pygame.draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)

    menu = Menu()

    menu.append_option('Играть снова', lambda: switch_scene(scene3E()))
    menu.append_option('Выйти', quit)

    running1 = True
    while running1:
        screen.fill((0, 0, 0))
        menu.draw(screen, 500, 250, 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                menu.switch(-1)
                # time.sleep(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                menu.switch(1)
                # time.sleep(3)

            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                menu.select()


def scene_proig1S():
    class Menu:
        def __init__(self):
            self._option_surfaces = []
            self._callbacks = []
            self._current_option_index = 0

        def append_option(self, option, callback):
            self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
            self._callbacks.append(callback)

        def switch(self, direction):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

        def select(self):
            self._callbacks[self._current_option_index]()

        def draw(self, surf, x, y, option_y_padding):
            for (i, option) in enumerate(self._option_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self._current_option_index:
                    pygame.draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)

    menu = Menu()

    menu.append_option('Играть снова', lambda: switch_scene(scene2S()))
    menu.append_option('Выйти', quit)

    running1 = True
    while running1:
        screen.fill((0, 0, 0))
        menu.draw(screen, 500, 250, 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                menu.switch(-1)
                # time.sleep(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                menu.switch(1)
                # time.sleep(3)

            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                menu.select()




def scene_proig2S():
    class Menu:
        def __init__(self):
            self._option_surfaces = []
            self._callbacks = []
            self._current_option_index = 0

        def append_option(self, option, callback):
            self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
            self._callbacks.append(callback)

        def switch(self, direction):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

        def select(self):
            self._callbacks[self._current_option_index]()

        def draw(self, surf, x, y, option_y_padding):
            for (i, option) in enumerate(self._option_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self._current_option_index:
                    pygame.draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)

    menu = Menu()

    menu.append_option('Играть снова', lambda: switch_scene(scene2S()))
    menu.append_option('Выйти', quit)

    running1 = True
    while running1:
        screen.fill((0, 0, 0))
        menu.draw(screen, 500, 250, 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                menu.switch(-1)
                # time.sleep(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                menu.switch(1)
                # time.sleep(3)

            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                menu.select()



def scene_proig3S():
    class Menu:
        def __init__(self):
            self._option_surfaces = []
            self._callbacks = []
            self._current_option_index = 0

        def append_option(self, option, callback):
            self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
            self._callbacks.append(callback)

        def switch(self, direction):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

        def select(self):
            self._callbacks[self._current_option_index]()

        def draw(self, surf, x, y, option_y_padding):
            for (i, option) in enumerate(self._option_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self._current_option_index:
                    pygame.draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)

    menu = Menu()

    menu.append_option('Играть снова', lambda: switch_scene(scene3S()))
    menu.append_option('Выйти', quit)

    running1 = True
    while running1:
        screen.fill((0, 0, 0))
        menu.draw(screen, 500, 250, 75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                menu.switch(-1)
                # time.sleep(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                menu.switch(1)
                # time.sleep(3)

            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                menu.select()



def scene1E():
    pygame.display.set_caption("Межвузовский студенческий городок")
    icon = pygame.image.load('images/monster.png').convert_alpha()
    pygame.display.set_icon(icon)

    bg1 = pygame.image.load('images/hata1.png').convert_alpha()
    bg = pygame.transform.scale(
        bg1, (bg1.get_width() // 3.5,
              bg1.get_height() // 3.3))  # уменьшение Оли(врага)
    pers = 0
    if pers == 0:

        walk_left = [
            pygame.image.load('images/elina_left/elina_left_1.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_2.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_3.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_4.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_5.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/elina_right/elina_right_1.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_2.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_3.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_4.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_5.png').convert_alpha()
        ]
    else:

        walk_left = [
            pygame.image.load('images/left/left1.png').convert_alpha(),
            pygame.image.load('images/left/left2.png').convert_alpha(),
            pygame.image.load('images/left/left3.png').convert_alpha(),
            pygame.image.load('images/left/left4.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/right/right1.png').convert_alpha(),
            pygame.image.load('images/right/right2.png').convert_alpha(),
            pygame.image.load('images/right/right3.png').convert_alpha(),
            pygame.image.load('images/right/right4.png').convert_alpha()
        ]

    ghost_list_in_game = []
    crystal_list_in_game = []
    tree_list_in_game = []

    crystal = 0
    if crystal == 0:
        walk_leftc = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]
        walk_rightc = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    else:

        walk_leftc = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

        walk_rightc = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    tree = 0
    if tree == 0:
        walk_leftt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]
        walk_rightt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    else:

        walk_leftt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

        walk_rightt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    player_anim_count = 0
    tree_anim_count = 0
    crystal_anim_count = 0
    kyler_anim_count = 0

    bg_x = 0

    Dead1 = pygame.image.load('images/Dead.jpg').convert_alpha()


    Dead = pygame.transform.scale(
        Dead1, (Dead1.get_width() // 4,
                Dead1.get_height() // 4))

    ghost_x = 2700
    ghost_y = 650

    player_speed = 2
    player_x = 200
    player_y = 600
    kyler_x = 700
    kyler_y = 600

    tree_speed = 2
    crystal_speed = 2
    crystal_cycle = 1

    crystal_go = 1
    crystal_x = 1000
    crystal_y = 600
    tree_y = 600
    tree_x = 400
    crystal_x1 = 1400
    crystal_y1 = 600
    crystal_x2 = 1900
    crystal_y2 = 600

    label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)

    restart_label = label.render("Играть заново", False, (115, 132, 148))

    restart_label_rect = restart_label.get_rect(topleft=(560, 360))

    bullet1 = pygame.image.load('images/bullet.png').convert_alpha()
    bullet = pygame.transform.scale(
        bullet1, (bullet1.get_width() // 6,
                  bullet1.get_height() // 6))
    bullets = []
    bullets1 = []

    is_jump = False
    jump_count = 9

    bg_sound = pygame.mixer.Sound('sounds/спидозные козявки 3.mp3')
    bg_sound.play()

    gameplya = True

    ghost_timer = pygame.USEREVENT + 1
    crystal_timer = pygame.USEREVENT + 1
    tree_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 16500)
    pygame.time.set_timer(crystal_timer, 16500)
    pygame.time.set_timer(tree_timer, 16500)
    bullets_left = 10
    bullets1_left = 10
    fof = 1
    fof1 = 1
    fof2 = 1
    fof3 = 1

    running = True
    while running:
        print(bg_x)

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 2400, 0))

        if gameplya:

            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

            if fof > 0:
                crystal_rect = walk_leftc[0].get_rect(topleft=(crystal_x, crystal_y))
            if fof1 > 0:
                crystal_rect1 = walk_leftc[0].get_rect(topleft=(crystal_x1, crystal_y1))
            if fof2 > 0:
                crystal_rect2 = walk_leftc[0].get_rect(topleft=(crystal_x2, crystal_y2))
            if fof3 > 0:
                tree_rect = walk_leftc[0].get_rect(topleft=(tree_x, tree_y))
            # kyler_rect = walk_leftky[0].get_rect(topleft=(kyler_x, kyler_y))

            if player_rect.colliderect(crystal_rect) and fof > 0:
                gameplya = False
            if player_rect.colliderect(crystal_rect1) and fof1 > 0:
                gameplya = False
            if player_rect.colliderect(crystal_rect2) and fof2 > 0:
                gameplya = False
            if player_rect.colliderect(tree_rect) and fof3 > 0:
                gameplya = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))

            if fof > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x, crystal_y))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x, crystal_y))
            if fof1 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x1, crystal_y1))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x1, crystal_y1))
            if fof2 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x2, crystal_y2))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x2, crystal_y2))

            if fof3 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftt[tree_anim_count], (tree_x, tree_y))
                else:
                    screen.blit(walk_rightt[tree_anim_count], (tree_x, tree_y))

            if keys[pygame.K_LEFT] and bg_x < 50:
                player_x -= player_speed * 3

                bg_x += player_speed + 1
                tree_x += player_speed + 1

            elif keys[pygame.K_RIGHT] and bg_x > -500:
                player_x += player_speed * 3

                bg_x -= player_speed + 1
                tree_x -= player_speed + 1
            if keys[pygame.K_DOWN] and player_y > 0:
                player_y += player_speed * 2
            if keys[pygame.K_UP] and player_y < 1250:
                player_y -= player_speed * 2

            if crystal_go == 1:
                crystal_x -= crystal_speed * 3
            else:
                crystal_x += crystal_speed * 3

            if crystal_go == 1:
                crystal_x1 -= crystal_speed * 3
            else:
                crystal_x1 += crystal_speed * 3

            if crystal_go == 1:
                crystal_x2 -= crystal_speed * 3
            else:
                crystal_x2 += crystal_speed * 3

            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -9:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 9

            if player_anim_count == 3:
                player_anim_count = 0
            else:
                player_anim_count += 1

            if crystal_anim_count == 3:
                crystal_anim_count = 0
            else:
                crystal_anim_count += 1

            if tree_anim_count == 3:
                tree_anim_count = 0
            else:
                tree_anim_count += 1

            if bg_x == -60280:
                bg_x = 0

            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x, el.y))
                    el.x += 4

                    if el.x > 2000:
                        bullets.pop()

                    if el.colliderect(crystal_rect) and fof > 0:
                        fof -= 1
                        bullets.pop(i)

                    if el.colliderect(crystal_rect1) and fof1 > 0:
                        fof1 -= 1
                        bullets.pop(i)

                    if el.colliderect(crystal_rect2) and fof2 > 0:
                        fof2 -= 1
                        bullets.pop(i)

                    if el.colliderect(tree_rect) and fof3 > 0:
                        fof3 -= 1
                        bullets.pop(i)

            if bullets1:
                for (i, el) in enumerate(bullets1):
                    screen.blit(bullet, (el.x, el.y))
                    el.y -= 4

                    if el.x > 2000:
                        bullets1.pop()

                        if ghost_list_in_game:
                            for (index, ghost_el) in enumerate(ghost_list_in_game):
                                if el.colliderect(ghost_el):
                                    ghost_list_in_game.pop(index)
                                    bullets1.pop(i)

                        if crystal_list_in_game:
                            for (index, crystal_el) in enumerate(crystal_list_in_game):
                                if el.colliderect(crystal_el):
                                    crystal_list_in_game.pop(index)
                                    bullets1.pop(i)

                        if tree_list_in_game:
                            for (index, tree_el) in enumerate(tree_list_in_game):
                                if el.colliderect(tree_el):
                                    tree_list_in_game.pop(index)
                                    bullets1.pop(i)

        else:
            #pygame.mixer.music.stop()
            scene_proig1E()

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplya = True
                player_x = 300
                ghost_list_in_game.clear()
                crystal_list_in_game.clear()
                bullets.clear()
                bullets_left = 8
                bullets1_left = 10
                player_speed = 2
                player_x = 200
                player_y = 600
                player_anim_count = 0
                bg_x = 0

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
                pygame.quit()
            # if event.type == ghost_timer:
            # ghost_list_in_game.append(ghost.get_rect(topleft=(1620, 600)))

            if event.type == crystal_timer:
                crystal_list_in_game.append(walk_leftc[0].get_rect(topleft=(1420, 600)))

            if event.type == tree_timer:
                tree_list_in_game.append(walk_leftt[0].get_rect(topleft=(1620, 600)))

            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
                bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y - 40)))
                bullets_left -= 1

            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_v and bullets1_left > 0:
                bullets1.append(bullet1.get_rect(topleft=(player_x, player_y - 60)))
                bullets1_left -= 1

            if -300 > bg_x >= -550 and event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                bg_sound.stop()

                switch_scene(scene2E())
                running = False

        print(player_x)
        clock.tick(15)



def scene2E():
    pygame.display.set_caption("Межвузовский студенческий городок")
    icon = pygame.image.load('images/monster.png').convert_alpha()
    pygame.display.set_icon(icon)

    bg1 = pygame.image.load('images/hata1.png').convert_alpha()
    bg = pygame.transform.scale(
        bg1, (bg1.get_width() // 3.5,
              bg1.get_height() // 3.3))  # уменьшение Оли(врага)
    pers = 0
    if pers == 0:

        walk_left = [
            pygame.image.load('images/elina_left/elina_left_1.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_2.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_3.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_4.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_5.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/elina_right/elina_right_1.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_2.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_3.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_4.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_5.png').convert_alpha()
        ]
    else:

        walk_left = [
            pygame.image.load('images/left/left1.png').convert_alpha(),
            pygame.image.load('images/left/left2.png').convert_alpha(),
            pygame.image.load('images/left/left3.png').convert_alpha(),
            pygame.image.load('images/left/left4.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/right/right1.png').convert_alpha(),
            pygame.image.load('images/right/right2.png').convert_alpha(),
            pygame.image.load('images/right/right3.png').convert_alpha(),
            pygame.image.load('images/right/right4.png').convert_alpha()
        ]

    ghost_list_in_game = []
    crystal_list_in_game = []
    tree_list_in_game = []


    crystal = 0
    if crystal == 0:
        walk_leftc = [
            pygame.image.load('images/crystal/crystal_1.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_2.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_3.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_4.png').convert_alpha()
        ]
        walk_rightc = [
            pygame.image.load('images/crystal/crystal_1.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_2.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_3.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_4.png').convert_alpha()
        ]

    else:

        walk_leftc = [
            pygame.image.load('images/crystal/crystal_1.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_2.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_3.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_4.png').convert_alpha()
        ]

        walk_rightc = [
            pygame.image.load('images/crystal/crystal_1.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_2.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_3.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_4.png').convert_alpha()
        ]

    tree = 0
    if tree == 0:
        walk_leftt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]
        walk_rightt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    else:

        walk_leftt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

        walk_rightt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    player_anim_count = 0
    tree_anim_count = 0
    crystal_anim_count = 0
    kyler_anim_count = 0

    bg_x = 0
    ghost1 = pygame.image.load('images/olka.png').convert_alpha()
    Dead1 = pygame.image.load('images/Dead.jpg').convert_alpha()
    ghost = pygame.transform.scale(
        ghost1, (ghost1.get_width() // 8,
                 ghost1.get_height() // 8))  # уменьшение Оли(врага)

    Dead = pygame.transform.scale(
        Dead1, (Dead1.get_width() // 4,
                Dead1.get_height() // 4))

    ghost_x = 2700
    ghost_y = 650

    player_speed = 2
    player_x = 200
    player_y = 600
    kyler_x = 700
    kyler_y = 600

    tree_speed = 2
    crystal_speed = 2
    crystal_cycle = 1


    crystal_go = 1
    crystal_x = 1000
    crystal_y = 600
    tree_y = 600
    tree_x = 400
    crystal_x1 = 1400
    crystal_y1 = 600
    crystal_x2 = 1900
    crystal_y2 = 600

    label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)

    restart_label = label.render("Играть заново", False, (115, 132, 148))

    restart_label_rect = restart_label.get_rect(topleft=(560, 360))

    bullet1 = pygame.image.load('images/bullet.png').convert_alpha()
    bullet = pygame.transform.scale(
        bullet1, (bullet1.get_width() // 6,
                  bullet1.get_height() // 6))
    bullets = []
    bullets1 = []

    is_jump = False
    jump_count = 9

    #bg_sound = pygame.mixer.Sound('sounds/спидозные козявки 3.mp3')
    #bg_sound.play()

    gameplya = True

    ghost_timer = pygame.USEREVENT + 1
    crystal_timer = pygame.USEREVENT + 1
    tree_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 16500)
    pygame.time.set_timer(crystal_timer, 16500)
    pygame.time.set_timer(tree_timer, 16500)
    bullets_left = 10
    bullets1_left = 10
    fof = 1
    fof1 = 1
    fof2 = 1
    fof3 = 1


    running = True
    while running:


        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 2400, 0))

        if gameplya:


            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

            if fof > 0:
                crystal_rect = walk_leftc[0].get_rect(topleft=(crystal_x, crystal_y))
            if fof1 > 0:
                crystal_rect1 = walk_leftc[0].get_rect(topleft=(crystal_x1, crystal_y1))
            if fof2 > 0:
                crystal_rect2 = walk_leftc[0].get_rect(topleft=(crystal_x2, crystal_y2))
            if fof3 > 0:
                tree_rect = walk_leftc[0].get_rect(topleft=(tree_x, tree_y))
            #kyler_rect = walk_leftky[0].get_rect(topleft=(kyler_x, kyler_y))

            if player_rect.colliderect(crystal_rect) and fof > 0:
                gameplya = False
            if player_rect.colliderect(crystal_rect1) and fof1 > 0:
                gameplya = False
            if player_rect.colliderect(crystal_rect2) and fof2 > 0:
                gameplya = False
            if player_rect.colliderect(tree_rect) and fof3 > 0:
                gameplya = False






            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))



            if fof > 0:
                if keys[pygame.K_LEFT] :
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x, crystal_y))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x, crystal_y))
            if fof1 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x1, crystal_y1))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x1, crystal_y1))
            if fof2 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x2, crystal_y2))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x2, crystal_y2))

            if fof3 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftt[tree_anim_count], (tree_x, tree_y))
                else:
                    screen.blit(walk_rightt[tree_anim_count], (tree_x, tree_y))



            if keys[pygame.K_LEFT] and bg_x < 50:
                player_x -= player_speed * 3

                bg_x += player_speed + 1
                tree_x += player_speed + 1

            elif keys[pygame.K_RIGHT] and bg_x > -500:
                player_x += player_speed * 3

                bg_x -= player_speed + 1
                tree_x -= player_speed + 1
            if keys[pygame.K_DOWN] and player_y > 0:
                player_y += player_speed * 2
            if keys[pygame.K_UP] and player_y < 1250:
                player_y -= player_speed * 2









            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -9:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 9

            if player_anim_count == 3:
                player_anim_count = 0
            else:
                player_anim_count += 1


            if crystal_anim_count == 3:
                crystal_anim_count = 0
            else:
                crystal_anim_count += 1



            if tree_anim_count == 3:
                tree_anim_count = 0
            else:
                tree_anim_count += 1

            if bg_x == -60280:
                bg_x = 0

            if crystal_go == 1:
                crystal_x -= crystal_speed * 3
            else:
                crystal_x += crystal_speed * 3

            if crystal_go == 1:
                crystal_x1 -= crystal_speed * 3
            else:
                crystal_x1 += crystal_speed * 3

            if crystal_go == 1:
                crystal_x2 -= crystal_speed * 3
            else:
                crystal_x2 += crystal_speed * 3

            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x, el.y))
                    el.x += 4

                    if el.x > 2000:
                        bullets.pop()

                    if el.colliderect(crystal_rect) and fof > 0:

                        fof -= 1
                        bullets.pop(i)

                    if el.colliderect(crystal_rect1) and fof1 > 0:

                        fof1 -= 1
                        bullets.pop(i)

                    if el.colliderect(crystal_rect2) and fof2 > 0:

                        fof2 -= 1
                        bullets.pop(i)

                    if el.colliderect(tree_rect) and fof3 > 0:

                        fof3 -= 1
                        bullets.pop(i)




            if bullets1:
                for (i, el) in enumerate(bullets1):
                    screen.blit(bullet, (el.x, el.y))
                    el.y -= 4

                    if el.x > 2000:
                        bullets1.pop()

                        if ghost_list_in_game:
                            for (index, ghost_el) in enumerate(ghost_list_in_game):
                                if el.colliderect(ghost_el):
                                    ghost_list_in_game.pop(index)
                                    bullets1.pop(i)

                        if crystal_list_in_game:
                            for (index, crystal_el) in enumerate(crystal_list_in_game):
                                if el.colliderect(crystal_el):
                                    crystal_list_in_game.pop(index)
                                    bullets1.pop(i)

                        if tree_list_in_game:
                            for (index, tree_el) in enumerate(tree_list_in_game):
                                if el.colliderect(tree_el):
                                    tree_list_in_game.pop(index)
                                    bullets1.pop(i)

        else:
            pygame.mixer.music.stop()
            scene_proig2E()



            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplya = True
                player_x = 300
                ghost_list_in_game.clear()
                crystal_list_in_game.clear()
                bullets.clear()
                bullets_left = 8
                bullets1_left = 10
                player_speed = 2
                player_x = 200
                player_y = 600
                player_anim_count = 0
                bg_x = 0


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
                pygame.quit()
            #if event.type == ghost_timer:
                #ghost_list_in_game.append(ghost.get_rect(topleft=(1620, 600)))

            if event.type == crystal_timer:
                crystal_list_in_game.append(walk_leftc[0].get_rect(topleft=(1420, 600)))

            if event.type == tree_timer:
                tree_list_in_game.append(walk_leftt[0].get_rect(topleft=(1620, 600)))

            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
                bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y - 40)))
                bullets_left -= 1

            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_v and bullets1_left > 0:
                bullets1.append(bullet1.get_rect(topleft=(player_x, player_y - 60)))
                bullets1_left -= 1

            if -300 > bg_x >= -550 and event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                #bg_sound.stop()

                switch_scene(scene3E())
                running = False




        clock.tick(15)


def scene3E():
    pygame.display.set_caption("Межвузовский студенческий городок")
    icon = pygame.image.load('images/monster.png').convert_alpha()
    pygame.display.set_icon(icon)

    bg1 = pygame.image.load('images/forest2.png').convert_alpha()
    bg = pygame.transform.scale(
        bg1, (bg1.get_width() // 3.5,
              bg1.get_height() // 3.3))  # уменьшение Оли(врага)
    pers = 0
    if pers == 0:


        walk_left = [
            pygame.image.load('images/elina_left/elina_left_1.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_2.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_3.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_4.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_5.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/elina_right/elina_right_1.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_2.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_3.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_4.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_5.png').convert_alpha()
        ]
    else:

        walk_left = [
            pygame.image.load('images/left/left1.png').convert_alpha(),
            pygame.image.load('images/left/left2.png').convert_alpha(),
            pygame.image.load('images/left/left3.png').convert_alpha(),
            pygame.image.load('images/left/left4.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/right/right1.png').convert_alpha(),
            pygame.image.load('images/right/right2.png').convert_alpha(),
            pygame.image.load('images/right/right3.png').convert_alpha(),
            pygame.image.load('images/right/right4.png').convert_alpha()
        ]

    ghost_list_in_game = []
    crystal_list_in_game = []
    tree_list_in_game = []

    kyler = 0
    if kyler == 0:
        walk_leftky = [
            pygame.image.load('images/кулер/кулер_1.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_2.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_3.png').convert_alpha()
        ]
        walk_rightky = [
            pygame.image.load('images/кулер/кулер_1.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_2.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_3.png').convert_alpha()
        ]

    else:

        walk_leftky = [
            pygame.image.load('images/кулер/кулер_1.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_2.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_3.png').convert_alpha()
        ]

        walk_rightky = [
            pygame.image.load('images/кулер/кулер_1.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_2.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_3.png').convert_alpha()
        ]





    boss = 0
    if boss == 0:
        walk_leftb = [
            pygame.image.load('images/boss/boss.png').convert_alpha(),
            pygame.image.load('images/boss/boss_1.png').convert_alpha(),
            pygame.image.load('images/boss/boss_3.png').convert_alpha(),
            pygame.image.load('images/boss/boss_4.png').convert_alpha()
        ]
        walk_rightb = [
            pygame.image.load('images/boss/boss.png').convert_alpha(),
            pygame.image.load('images/boss/boss_1.png').convert_alpha(),
            pygame.image.load('images/boss/boss_3.png').convert_alpha(),
            pygame.image.load('images/boss/boss_4.png').convert_alpha()
        ]

    else:

        walk_leftb = [
            pygame.image.load('images/boss/boss.png').convert_alpha(),
            pygame.image.load('images/boss/boss_1.png').convert_alpha(),
            pygame.image.load('images/boss/boss_3.png').convert_alpha(),
            pygame.image.load('images/boss/boss_4.png').convert_alpha()
        ]


        walk_right = [
            pygame.image.load('images/boss/boss.png').convert_alpha(),
            pygame.image.load('images/boss/boss_1.png').convert_alpha(),
            pygame.image.load('images/boss/boss_3.png').convert_alpha(),
            pygame.image.load('images/boss/boss_4.png').convert_alpha()
        ]






    player_anim_count = 0

    boss_anim_count = 0
    kyler_anim_count = 0

    bg_x = 0
    ghost1 = pygame.image.load('images/olka.png').convert_alpha()
    Dead1 = pygame.image.load('images/Dead.jpg').convert_alpha()
    ghost = pygame.transform.scale(
        ghost1, (ghost1.get_width() // 8,
                 ghost1.get_height() // 8))  # уменьшение Оли(врага)

    Dead = pygame.transform.scale(
        Dead1, (Dead1.get_width() // 4,
                Dead1.get_height() // 4))

    player_speed = 2
    player_x = 200
    player_y = 600
    boss_speed = 2

    boss_cycle = 1
    boss_go = 1
    boss_hp = 3

    boss_x = 400
    boss_y = 100
    kyler_x = 750
    kyler_y  = 550
    label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)

    restart_label = label.render("Играть заново", False, (115, 132, 148))

    restart_label_rect = restart_label.get_rect(topleft=(560, 360))

    bullet1 = pygame.image.load('images/bullet.png').convert_alpha()
    bullet = pygame.transform.scale(
        bullet1, (bullet1.get_width() // 6,
                  bullet1.get_height() // 6))
    bullet1 = pygame.image.load('images/line.png').convert_alpha()
    bulletv = pygame.transform.scale(
        bullet1, (bullet1.get_width() // 6,
                  bullet1.get_height() // 6))

    bullets_boss = pygame.image.load('images/bullet.png').convert_alpha()
    bullets = []
    bullets1 = []
    bullet_boss = []

    is_jump = False
    jump_count = 9

    #bg_sound = pygame.mixer.Sound('sounds/спидозные козявки 3.mp3')
    #bg_sound.play()

    gameplya = True

    ghost_timer = pygame.USEREVENT + 1
    crystal_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 16500)
    pygame.time.set_timer(crystal_timer, 16500)
    bullets_left = 10
    bullets1_left = 10
    bullets_boss1 = 10000000
    running = True
    while running:

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 2400, 0))


        if gameplya:

            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
            boss_rect = walk_leftb[0].get_rect(topleft=(boss_x, boss_y))

            kyler_rect = walk_leftky[0].get_rect(topleft=(kyler_x, kyler_y))




            keys = pygame.key.get_pressed()
            if player_rect.colliderect(kyler_rect) and keys[pygame.K_RETURN]:
                bullets_left += 1
                bullets1_left += 1



            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))

            if keys[pygame.K_LEFT]:
                screen.blit(walk_leftb[boss_anim_count], (boss_x, boss_y))
            else:
                screen.blit(walk_rightb[boss_anim_count], (boss_x, boss_y))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_leftky[kyler_anim_count], (kyler_x, kyler_y))
            else:
                screen.blit(walk_leftky[kyler_anim_count], (kyler_x, kyler_y))





            if keys[pygame.K_LEFT] and bg_x < 50:
                player_x -= player_speed * 3

                bg_x += player_speed + 1
                kyler_x += player_speed + 1
            elif keys[pygame.K_RIGHT] and bg_x > -500:
                player_x += player_speed * 3

                bg_x -= player_speed + 1
                kyler_x -= player_speed + 1
            if keys[pygame.K_DOWN] and player_y > 0:
                player_y += player_speed
            if keys[pygame.K_UP] and player_y < 1250:
                player_y -= player_speed

            if boss_go == 1:
                boss_x += boss_speed * 3
            else:
                boss_x -= boss_speed * 3





            if boss_x > 1150 and boss_cycle % 3 != 0:

                boss_go -= 1



            if boss_x < 51 and boss_cycle % 3 != 0:

                boss_go += 1




            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -9:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 9

            if player_anim_count == 3:
                player_anim_count = 0
            else:
                player_anim_count += 1

            if boss_anim_count == 3:
                boss_anim_count = 0
            else:
                boss_anim_count += 1



            if kyler_anim_count == 2:
                kyler_anim_count = 0
            else:
                kyler_anim_count += 1



            if bg_x == -60280:
                bg_x = 0

            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullets_boss, (el.x, el.y))
                    el.x += 4

                    if el.x > 20000:
                        bullets.pop()





            if bullets1:
                for (i, el) in enumerate(bullets1):
                    screen.blit(bullet, (el.x, el.y))
                    el.y -= 4

                    if el.x > 20000:
                        bullets1.pop()

                    if el.colliderect(boss_rect):

                        bullets1.pop(i)
                        boss_hp -= 1

            if bullets_boss1:
                for (i, el) in enumerate(bullet_boss):
                    screen.blit(bulletv, (el.x, el.y))
                    el.y += 4



                    #if el.colliderect(player_rect):

                        #gameplya = False




        else:
            scene_proig3E()

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplya = True
                player_x = 300
                ghost_list_in_game.clear()
                crystal_list_in_game.clear()
                bullets.clear()
                bullets_left = 8
                bullets1_left = 10
                player_speed = 2
                player_x = 200
                player_y = 600
                player_anim_count = 0
                bg_x = 0
                #bg_sound.stop()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
                pygame.quit()






            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
                bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y - 40)))
                bullets_left -= 1



            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_v and bullets1_left > 0:
                bullets1.append(bullet1.get_rect(topleft=(player_x, player_y - 60)))
                bullets1_left -= 1


            if gameplya and bullets_boss1 > 0:
                bullet_boss.append(bullets_boss.get_rect(topleft=(boss_x, boss_y + 60)))
                bullets_boss1 -= 1



            if boss_hp < 1:
                #bg_sound.stop()
                switch_scene(scene_finish())
                running = False


        #print(boss_x)

        clock.tick(15)







def scene1S():
    pygame.display.set_caption("Межвузовский студенческий городок")
    icon = pygame.image.load('images/monster.png').convert_alpha()
    pygame.display.set_icon(icon)

    bg1 = pygame.image.load('images/hata1.png').convert_alpha()
    bg = pygame.transform.scale(
        bg1, (bg1.get_width() // 3.5,
              bg1.get_height() // 3.3))  # уменьшение Оли(врага)
    pers = 0
    if pers == 0:

        walk_left = [
            pygame.image.load('images/left/left1.png').convert_alpha(),
            pygame.image.load('images/left/left2.png').convert_alpha(),
            pygame.image.load('images/left/left3.png').convert_alpha(),
            pygame.image.load('images/left/left4.png').convert_alpha(),
            pygame.image.load('images/left/left5.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/right/right1.png').convert_alpha(),
            pygame.image.load('images/right/right2.png').convert_alpha(),
            pygame.image.load('images/right/right3.png').convert_alpha(),
            pygame.image.load('images/right/right4.png').convert_alpha(),
            pygame.image.load('images/right/right5.png').convert_alpha()
        ]
    else:

        walk_left = [
            pygame.image.load('images/left/left1.png').convert_alpha(),
            pygame.image.load('images/left/left2.png').convert_alpha(),
            pygame.image.load('images/left/left3.png').convert_alpha(),
            pygame.image.load('images/left/left4.png').convert_alpha(),
            pygame.image.load('images/left/left5.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/right/right1.png').convert_alpha(),
            pygame.image.load('images/right/right2.png').convert_alpha(),
            pygame.image.load('images/right/right3.png').convert_alpha(),
            pygame.image.load('images/right/right4.png').convert_alpha(),
            pygame.image.load('images/right/right5.png').convert_alpha()
        ]

    ghost_list_in_game = []
    crystal_list_in_game = []
    tree_list_in_game = []

    crystal = 0
    if crystal == 0:
        walk_leftc = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]
        walk_rightc = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    else:

        walk_leftc = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

        walk_rightc = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    tree = 0
    if tree == 0:
        walk_leftt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]
        walk_rightt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    else:

        walk_leftt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

        walk_rightt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    player_anim_count = 0
    tree_anim_count = 0
    crystal_anim_count = 0
    kyler_anim_count = 0

    bg_x = 0

    Dead1 = pygame.image.load('images/Dead.jpg').convert_alpha()


    Dead = pygame.transform.scale(
        Dead1, (Dead1.get_width() // 4,
                Dead1.get_height() // 4))

    ghost_x = 2700
    ghost_y = 650

    player_speed = 2
    player_x = 200
    player_y = 600
    kyler_x = 700
    kyler_y = 600

    tree_speed = 2
    crystal_speed = 2
    crystal_cycle = 1

    crystal_go = 1
    crystal_x = 1000
    crystal_y = 600
    tree_y = 600
    tree_x = 400
    crystal_x1 = 1400
    crystal_y1 = 600
    crystal_x2 = 1900
    crystal_y2 = 600

    label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)

    restart_label = label.render("Играть заново", False, (115, 132, 148))

    restart_label_rect = restart_label.get_rect(topleft=(560, 360))

    bullet1 = pygame.image.load('images/bullet.png').convert_alpha()
    bullet = pygame.transform.scale(
        bullet1, (bullet1.get_width() // 6,
                  bullet1.get_height() // 6))
    bullets = []
    bullets1 = []

    is_jump = False
    jump_count = 9

    bg_sound = pygame.mixer.Sound('sounds/спидозные козявки 3.mp3')
    bg_sound.play()

    gameplya = True

    ghost_timer = pygame.USEREVENT + 1
    crystal_timer = pygame.USEREVENT + 1
    tree_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 16500)
    pygame.time.set_timer(crystal_timer, 16500)
    pygame.time.set_timer(tree_timer, 16500)
    bullets_left = 10
    bullets1_left = 10
    fof = 1
    fof1 = 1
    fof2 = 1
    fof3 = 1

    running = True
    while running:

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 2400, 0))

        if gameplya:

            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

            if fof > 0:
                crystal_rect = walk_leftc[0].get_rect(topleft=(crystal_x, crystal_y))
            if fof1 > 0:
                crystal_rect1 = walk_leftc[0].get_rect(topleft=(crystal_x1, crystal_y1))
            if fof2 > 0:
                crystal_rect2 = walk_leftc[0].get_rect(topleft=(crystal_x2, crystal_y2))
            if fof3 > 0:
                tree_rect = walk_leftc[0].get_rect(topleft=(tree_x, tree_y))
            # kyler_rect = walk_leftky[0].get_rect(topleft=(kyler_x, kyler_y))

            if player_rect.colliderect(crystal_rect) and fof > 0:
                gameplya = False
            if player_rect.colliderect(crystal_rect1) and fof1 > 0:
                gameplya = False
            if player_rect.colliderect(crystal_rect2) and fof2 > 0:
                gameplya = False
            if player_rect.colliderect(tree_rect) and fof3 > 0:
                gameplya = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))

            if fof > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x, crystal_y))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x, crystal_y))
            if fof1 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x1, crystal_y1))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x1, crystal_y1))
            if fof2 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x2, crystal_y2))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x2, crystal_y2))

            if fof3 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftt[tree_anim_count], (tree_x, tree_y))
                else:
                    screen.blit(walk_rightt[tree_anim_count], (tree_x, tree_y))

            if keys[pygame.K_LEFT] and bg_x < 50:
                player_x -= player_speed * 3

                bg_x += player_speed + 1
                tree_x += player_speed + 1

            elif keys[pygame.K_RIGHT] and bg_x > -500:
                player_x += player_speed * 3

                bg_x -= player_speed + 1
                tree_x -= player_speed + 1
            if keys[pygame.K_DOWN] and player_y > 0:
                player_y += player_speed * 2
            if keys[pygame.K_UP] and player_y < 1250:
                player_y -= player_speed * 2

            if crystal_go == 1:
                crystal_x -= crystal_speed * 3
            else:
                crystal_x += crystal_speed * 3

            if crystal_go == 1:
                crystal_x1 -= crystal_speed * 3
            else:
                crystal_x1 += crystal_speed * 3

            if crystal_go == 1:
                crystal_x2 -= crystal_speed * 3
            else:
                crystal_x2 += crystal_speed * 3

            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -9:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 9

            if player_anim_count == 3:
                player_anim_count = 0
            else:
                player_anim_count += 1

            if crystal_anim_count == 3:
                crystal_anim_count = 0
            else:
                crystal_anim_count += 1

            if tree_anim_count == 3:
                tree_anim_count = 0
            else:
                tree_anim_count += 1

            if bg_x == -60280:
                bg_x = 0

            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x, el.y))
                    el.x += 4

                    if el.x > 2000:
                        bullets.pop()

                    if el.colliderect(crystal_rect) and fof > 0:
                        fof -= 1
                        bullets.pop(i)

                    if el.colliderect(crystal_rect1) and fof1 > 0:
                        fof1 -= 1
                        bullets.pop(i)

                    if el.colliderect(crystal_rect2) and fof2 > 0:
                        fof2 -= 1
                        bullets.pop(i)

                    if el.colliderect(tree_rect) and fof3 > 0:
                        fof3 -= 1
                        bullets.pop(i)

            if bullets1:
                for (i, el) in enumerate(bullets1):
                    screen.blit(bullet, (el.x, el.y))
                    el.y -= 4

                    if el.x > 2000:
                        bullets1.pop()

                        if ghost_list_in_game:
                            for (index, ghost_el) in enumerate(ghost_list_in_game):
                                if el.colliderect(ghost_el):
                                    ghost_list_in_game.pop(index)
                                    bullets1.pop(i)

                        if crystal_list_in_game:
                            for (index, crystal_el) in enumerate(crystal_list_in_game):
                                if el.colliderect(crystal_el):
                                    crystal_list_in_game.pop(index)
                                    bullets1.pop(i)

                        if tree_list_in_game:
                            for (index, tree_el) in enumerate(tree_list_in_game):
                                if el.colliderect(tree_el):
                                    tree_list_in_game.pop(index)
                                    bullets1.pop(i)

        else:
            pygame.mixer.music.stop()
            scene_proig2E()

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplya = True
                player_x = 300
                ghost_list_in_game.clear()
                crystal_list_in_game.clear()
                bullets.clear()
                bullets_left = 8
                bullets1_left = 10
                player_speed = 2
                player_x = 200
                player_y = 600
                player_anim_count = 0
                bg_x = 0

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
                pygame.quit()
            # if event.type == ghost_timer:
            # ghost_list_in_game.append(ghost.get_rect(topleft=(1620, 600)))

            if event.type == crystal_timer:
                crystal_list_in_game.append(walk_leftc[0].get_rect(topleft=(1420, 600)))

            if event.type == tree_timer:
                tree_list_in_game.append(walk_leftt[0].get_rect(topleft=(1620, 600)))

            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
                bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y - 40)))
                bullets_left -= 1

            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_v and bullets1_left > 0:
                bullets1.append(bullet1.get_rect(topleft=(player_x, player_y - 60)))
                bullets1_left -= 1

            if -300 > bg_x >= -500 and event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                bg_sound.stop()

                switch_scene(scene3E())
                running = False

        clock.tick(15)



def scene2S():
    pygame.display.set_caption("Межвузовский студенческий городок")
    icon = pygame.image.load('images/monster.png').convert_alpha()
    pygame.display.set_icon(icon)

    bg1 = pygame.image.load('images/hata1.png').convert_alpha()
    bg = pygame.transform.scale(
        bg1, (bg1.get_width() // 3.5,
              bg1.get_height() // 3.3))  # уменьшение Оли(врага)
    pers = 0
    if pers == 0:

        walk_left = [
            pygame.image.load('images/elina_left/elina_left_1.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_2.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_3.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_4.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_5.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/elina_right/elina_right_1.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_2.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_3.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_4.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_5.png').convert_alpha()
        ]
    else:

        walk_left = [
            pygame.image.load('images/left/left1.png').convert_alpha(),
            pygame.image.load('images/left/left2.png').convert_alpha(),
            pygame.image.load('images/left/left3.png').convert_alpha(),
            pygame.image.load('images/left/left4.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/right/right1.png').convert_alpha(),
            pygame.image.load('images/right/right2.png').convert_alpha(),
            pygame.image.load('images/right/right3.png').convert_alpha(),
            pygame.image.load('images/right/right4.png').convert_alpha()
        ]

    ghost_list_in_game = []
    crystal_list_in_game = []
    tree_list_in_game = []


    crystal = 0
    if crystal == 0:
        walk_leftc = [
            pygame.image.load('images/crystal/crystal_1.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_2.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_3.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_4.png').convert_alpha()
        ]
        walk_rightc = [
            pygame.image.load('images/crystal/crystal_1.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_2.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_3.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_4.png').convert_alpha()
        ]

    else:

        walk_leftc = [
            pygame.image.load('images/crystal/crystal_1.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_2.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_3.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_4.png').convert_alpha()
        ]

        walk_rightc = [
            pygame.image.load('images/crystal/crystal_1.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_2.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_3.png').convert_alpha(),
            pygame.image.load('images/crystal/crystal_4.png').convert_alpha()
        ]

    tree = 0
    if tree == 0:
        walk_leftt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]
        walk_rightt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    else:

        walk_leftt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

        walk_rightt = [
            pygame.image.load('images/tree/tree_1.png').convert_alpha(),
            pygame.image.load('images/tree/tree_2.png').convert_alpha(),
            pygame.image.load('images/tree/tree_3.png').convert_alpha(),
            pygame.image.load('images/tree/tree_4.png').convert_alpha()
        ]

    player_anim_count = 0
    tree_anim_count = 0
    crystal_anim_count = 0
    kyler_anim_count = 0

    bg_x = 0
    ghost1 = pygame.image.load('images/olka.png').convert_alpha()
    Dead1 = pygame.image.load('images/Dead.jpg').convert_alpha()
    ghost = pygame.transform.scale(
        ghost1, (ghost1.get_width() // 8,
                 ghost1.get_height() // 8))  # уменьшение Оли(врага)

    Dead = pygame.transform.scale(
        Dead1, (Dead1.get_width() // 4,
                Dead1.get_height() // 4))

    ghost_x = 2700
    ghost_y = 650

    player_speed = 2
    player_x = 200
    player_y = 600
    kyler_x = 700
    kyler_y = 600

    tree_speed = 2
    crystal_speed = 2
    crystal_cycle = 1


    crystal_go = 1
    crystal_x = 1000
    crystal_y = 600
    tree_y = 600
    tree_x = 400
    crystal_x1 = 1400
    crystal_y1 = 600
    crystal_x2 = 1900
    crystal_y2 = 600

    label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)

    restart_label = label.render("Играть заново", False, (115, 132, 148))

    restart_label_rect = restart_label.get_rect(topleft=(560, 360))

    bullet1 = pygame.image.load('images/bullet.png').convert_alpha()
    bullet = pygame.transform.scale(
        bullet1, (bullet1.get_width() // 6,
                  bullet1.get_height() // 6))
    bullets = []
    bullets1 = []

    is_jump = False
    jump_count = 9

    bg_sound = pygame.mixer.Sound('sounds/спидозные козявки 3.mp3')
    bg_sound.play()

    gameplya = True

    ghost_timer = pygame.USEREVENT + 1
    crystal_timer = pygame.USEREVENT + 1
    tree_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 16500)
    pygame.time.set_timer(crystal_timer, 16500)
    pygame.time.set_timer(tree_timer, 16500)
    bullets_left = 10
    bullets1_left = 10
    fof = 1
    fof1 = 1
    fof2 = 1
    fof3 = 1


    running = True
    while running:

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 2400, 0))

        if gameplya:


            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

            if fof > 0:
                crystal_rect = walk_leftc[0].get_rect(topleft=(crystal_x, crystal_y))
            if fof1 > 0:
                crystal_rect1 = walk_leftc[0].get_rect(topleft=(crystal_x1, crystal_y1))
            if fof2 > 0:
                crystal_rect2 = walk_leftc[0].get_rect(topleft=(crystal_x2, crystal_y2))
            if fof3 > 0:
                tree_rect = walk_leftc[0].get_rect(topleft=(tree_x, tree_y))
            #kyler_rect = walk_leftky[0].get_rect(topleft=(kyler_x, kyler_y))

            if player_rect.colliderect(crystal_rect) and fof > 0:
                gameplya = False
            if player_rect.colliderect(crystal_rect1) and fof1 > 0:
                gameplya = False
            if player_rect.colliderect(crystal_rect2) and fof2 > 0:
                gameplya = False
            if player_rect.colliderect(tree_rect) and fof3 > 0:
                gameplya = False






            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))



            if fof > 0:
                if keys[pygame.K_LEFT] :
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x, crystal_y))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x, crystal_y))
            if fof1 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x1, crystal_y1))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x1, crystal_y1))
            if fof2 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftc[crystal_anim_count], (crystal_x2, crystal_y2))
                else:
                    screen.blit(walk_rightc[crystal_anim_count], (crystal_x2, crystal_y2))

            if fof3 > 0:
                if keys[pygame.K_LEFT]:
                    screen.blit(walk_leftt[tree_anim_count], (tree_x, tree_y))
                else:
                    screen.blit(walk_rightt[tree_anim_count], (tree_x, tree_y))



            if keys[pygame.K_LEFT] and bg_x < 50:
                player_x -= player_speed * 3

                bg_x += player_speed + 1
                tree_x += player_speed + 1

            elif keys[pygame.K_RIGHT] and bg_x > -500:
                player_x += player_speed * 3

                bg_x -= player_speed + 1
                tree_x -= player_speed + 1
            if keys[pygame.K_DOWN] and player_y > 0:
                player_y += player_speed * 2
            if keys[pygame.K_UP] and player_y < 1250:
                player_y -= player_speed * 2









            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -9:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 9

            if player_anim_count == 3:
                player_anim_count = 0
            else:
                player_anim_count += 1


            if crystal_anim_count == 3:
                crystal_anim_count = 0
            else:
                crystal_anim_count += 1



            if tree_anim_count == 3:
                tree_anim_count = 0
            else:
                tree_anim_count += 1

            if bg_x == -60280:
                bg_x = 0

            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x, el.y))
                    el.x += 4

                    if el.x > 2000:
                        bullets.pop()

                    if el.colliderect(crystal_rect) and fof > 0:

                        fof -= 1
                        bullets.pop(i)

                    if el.colliderect(crystal_rect1) and fof1 > 0:

                        fof1 -= 1
                        bullets.pop(i)

                    if el.colliderect(crystal_rect2) and fof2 > 0:

                        fof2 -= 1
                        bullets.pop(i)

                    if el.colliderect(tree_rect) and fof3 > 0:

                        fof3 -= 1
                        bullets.pop(i)




            if bullets1:
                for (i, el) in enumerate(bullets1):
                    screen.blit(bullet, (el.x, el.y))
                    el.y -= 4

                    if el.x > 2000:
                        bullets1.pop()

                        if ghost_list_in_game:
                            for (index, ghost_el) in enumerate(ghost_list_in_game):
                                if el.colliderect(ghost_el):
                                    ghost_list_in_game.pop(index)
                                    bullets1.pop(i)

                        if crystal_list_in_game:
                            for (index, crystal_el) in enumerate(crystal_list_in_game):
                                if el.colliderect(crystal_el):
                                    crystal_list_in_game.pop(index)
                                    bullets1.pop(i)

                        if tree_list_in_game:
                            for (index, tree_el) in enumerate(tree_list_in_game):
                                if el.colliderect(tree_el):
                                    tree_list_in_game.pop(index)
                                    bullets1.pop(i)

        else:
            pygame.mixer.music.stop()
            scene_proig2E()



            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplya = True
                player_x = 300
                ghost_list_in_game.clear()
                crystal_list_in_game.clear()
                bullets.clear()
                bullets_left = 8
                bullets1_left = 10
                player_speed = 2
                player_x = 200
                player_y = 600
                player_anim_count = 0
                bg_x = 0


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
                pygame.quit()
            #if event.type == ghost_timer:
                #ghost_list_in_game.append(ghost.get_rect(topleft=(1620, 600)))

            if event.type == crystal_timer:
                crystal_list_in_game.append(walk_leftc[0].get_rect(topleft=(1420, 600)))

            if event.type == tree_timer:
                tree_list_in_game.append(walk_leftt[0].get_rect(topleft=(1620, 600)))

            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
                bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y - 40)))
                bullets_left -= 1

            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_v and bullets1_left > 0:
                bullets1.append(bullet1.get_rect(topleft=(player_x, player_y - 60)))
                bullets1_left -= 1

            if -300 > bg_x >= -500 and event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                bg_sound.stop()

                switch_scene(scene3E())
                running = False



        clock.tick(15)


def scene3S():
    pygame.display.set_caption("Межвузовский студенческий городок")
    icon = pygame.image.load('images/monster.png').convert_alpha()
    pygame.display.set_icon(icon)

    bg1 = pygame.image.load('images/forest2.png').convert_alpha()
    bg = pygame.transform.scale(
        bg1, (bg1.get_width() // 3.5,
              bg1.get_height() // 3.3))  # уменьшение Оли(врага)
    pers = 0
    if pers == 0:


        walk_left = [
            pygame.image.load('images/elina_left/elina_left_1.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_2.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_3.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_4.png').convert_alpha(),
            pygame.image.load('images/elina_left/elina_left_5.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/elina_right/elina_right_1.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_2.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_3.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_4.png').convert_alpha(),
            pygame.image.load('images/elina_right/elina_right_5.png').convert_alpha()
        ]
    else:

        walk_left = [
            pygame.image.load('images/left/left1.png').convert_alpha(),
            pygame.image.load('images/left/left2.png').convert_alpha(),
            pygame.image.load('images/left/left3.png').convert_alpha(),
            pygame.image.load('images/left/left4.png').convert_alpha()
        ]

        walk_right = [
            pygame.image.load('images/right/right1.png').convert_alpha(),
            pygame.image.load('images/right/right2.png').convert_alpha(),
            pygame.image.load('images/right/right3.png').convert_alpha(),
            pygame.image.load('images/right/right4.png').convert_alpha()
        ]

    ghost_list_in_game = []
    crystal_list_in_game = []
    tree_list_in_game = []

    kyler = 0
    if kyler == 0:
        walk_leftky = [
            pygame.image.load('images/кулер/кулер_1.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_2.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_3.png').convert_alpha()
        ]
        walk_rightky = [
            pygame.image.load('images/кулер/кулер_1.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_2.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_3.png').convert_alpha()
        ]

    else:

        walk_leftky = [
            pygame.image.load('images/кулер/кулер_1.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_2.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_3.png').convert_alpha()
        ]

        walk_rightky = [
            pygame.image.load('images/кулер/кулер_1.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_2.png').convert_alpha(),
            pygame.image.load('images/кулер/кулер_3.png').convert_alpha()
        ]





    boss = 0
    if boss == 0:
        walk_leftb = [
            pygame.image.load('images/boss/boss.png').convert_alpha(),
            pygame.image.load('images/boss/boss_1.png').convert_alpha(),
            pygame.image.load('images/boss/boss_3.png').convert_alpha(),
            pygame.image.load('images/boss/boss_4.png').convert_alpha()
        ]
        walk_rightb = [
            pygame.image.load('images/boss/boss.png').convert_alpha(),
            pygame.image.load('images/boss/boss_1.png').convert_alpha(),
            pygame.image.load('images/boss/boss_3.png').convert_alpha(),
            pygame.image.load('images/boss/boss_4.png').convert_alpha()
        ]

    else:

        walk_leftb = [
            pygame.image.load('images/boss/boss.png').convert_alpha(),
            pygame.image.load('images/boss/boss_1.png').convert_alpha(),
            pygame.image.load('images/boss/boss_3.png').convert_alpha(),
            pygame.image.load('images/boss/boss_4.png').convert_alpha()
        ]


        walk_right = [
            pygame.image.load('images/boss/boss.png').convert_alpha(),
            pygame.image.load('images/boss/boss_1.png').convert_alpha(),
            pygame.image.load('images/boss/boss_3.png').convert_alpha(),
            pygame.image.load('images/boss/boss_4.png').convert_alpha()
        ]






    player_anim_count = 0

    boss_anim_count = 0
    kyler_anim_count = 0

    bg_x = 0
    ghost1 = pygame.image.load('images/olka.png').convert_alpha()
    Dead1 = pygame.image.load('images/Dead.jpg').convert_alpha()
    ghost = pygame.transform.scale(
        ghost1, (ghost1.get_width() // 8,
                 ghost1.get_height() // 8))  # уменьшение Оли(врага)

    Dead = pygame.transform.scale(
        Dead1, (Dead1.get_width() // 4,
                Dead1.get_height() // 4))

    player_speed = 2
    player_x = 200
    player_y = 600
    boss_speed = 2

    boss_cycle = 1
    boss_go = 1
    boss_hp = 3

    boss_x = 400
    boss_y = 100
    kyler_x = 750
    kyler_y  = 550
    label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)

    restart_label = label.render("Играть заново", False, (115, 132, 148))

    restart_label_rect = restart_label.get_rect(topleft=(560, 360))

    bullet1 = pygame.image.load('images/bullet.png').convert_alpha()
    bullet = pygame.transform.scale(
        bullet1, (bullet1.get_width() // 6,
                  bullet1.get_height() // 6))
    bullets_boss = pygame.image.load('images/line.png').convert_alpha()
    bullets = []
    bullets1 = []
    bullet_boss = []

    is_jump = False
    jump_count = 9

    bg_sound = pygame.mixer.Sound('sounds/спидозные козявки 3.mp3')
    bg_sound.play()

    gameplya = True

    ghost_timer = pygame.USEREVENT + 1
    crystal_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 16500)
    pygame.time.set_timer(crystal_timer, 16500)
    bullets_left = 10
    bullets1_left = 10
    bullets_boss1 = 10000000
    running = True
    while running:

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 2400, 0))


        if gameplya:

            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
            boss_rect = walk_leftb[0].get_rect(topleft=(boss_x, boss_y))

            kyler_rect = walk_leftky[0].get_rect(topleft=(kyler_x, kyler_y))




            keys = pygame.key.get_pressed()
            if player_rect.colliderect(kyler_rect) and keys[pygame.K_RETURN]:
                bullets_left += 1
                bullets1_left += 1



            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))

            if keys[pygame.K_LEFT]:
                screen.blit(walk_leftb[boss_anim_count], (boss_x, boss_y))
            else:
                screen.blit(walk_rightb[boss_anim_count], (boss_x, boss_y))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_leftky[kyler_anim_count], (kyler_x, kyler_y))
            else:
                screen.blit(walk_leftky[kyler_anim_count], (kyler_x, kyler_y))





            if keys[pygame.K_LEFT] and bg_x < 50:
                player_x -= player_speed * 3

                bg_x += player_speed + 1
                kyler_x += player_speed + 1
            elif keys[pygame.K_RIGHT] and bg_x > -500:
                player_x += player_speed * 3

                bg_x -= player_speed + 1
                kyler_x -= player_speed + 1
            if keys[pygame.K_DOWN] and player_y > 0:
                player_y += player_speed
            if keys[pygame.K_UP] and player_y < 1250:
                player_y -= player_speed

            if boss_go == 1:
                boss_x += boss_speed * 3
            else:
                boss_x -= boss_speed * 3





            if boss_x > 1150 and boss_cycle % 3 != 0:

                boss_go -= 1



            if boss_x < 51 and boss_cycle % 3 != 0:

                boss_go += 1




            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -9:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 9

            if player_anim_count == 3:
                player_anim_count = 0
            else:
                player_anim_count += 1

            if boss_anim_count == 3:
                boss_anim_count = 0
            else:
                boss_anim_count += 1



            if kyler_anim_count == 2:
                kyler_anim_count = 0
            else:
                kyler_anim_count += 1



            if bg_x == -60280:
                bg_x = 0

            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullets_boss, (el.x, el.y))
                    el.x += 4

                    if el.x > 20000:
                        bullets.pop()





            if bullets1:
                for (i, el) in enumerate(bullets1):
                    screen.blit(bullet, (el.x, el.y))
                    el.y -= 4

                    if el.x > 20000:
                        bullets1.pop()

                    if el.colliderect(boss_rect):

                        bullets1.pop(i)
                        boss_hp -= 1

            if bullets_boss1:
                for (i, el) in enumerate(bullet_boss):
                    screen.blit(bullet, (el.x, el.y))
                    el.y += 4



                    if el.colliderect(player_rect):

                        gameplya = False




        else:
            scene_proig3E()

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplya = True
                player_x = 300
                ghost_list_in_game.clear()
                crystal_list_in_game.clear()
                bullets.clear()
                bullets_left = 8
                bullets1_left = 10
                player_speed = 2
                player_x = 200
                player_y = 600
                player_anim_count = 0
                bg_x = 0
                bg_sound.stop()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
                pygame.quit()






            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
                bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y - 40)))
                bullets_left -= 1



            if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_v and bullets1_left > 0:
                bullets1.append(bullet1.get_rect(topleft=(player_x, player_y - 60)))
                bullets1_left -= 1


            if gameplya and bullets_boss1 > 0:
                bullet_boss.append(bullets_boss.get_rect(topleft=(boss_x, boss_y + 60)))
                bullets_boss1 -= 1



            if boss_hp < 1:
                bg_sound.stop()
                switch_scene(scene_finish())
                running = False


        #print(boss_x)

        clock.tick(15)

def scene_finish():
    pygame.display.set_caption("Межвузовский студенческий городок")
    icon = pygame.image.load('images/monster.png').convert_alpha()
    pygame.display.set_icon(icon)

    bg1 = pygame.image.load('images/win.jpg').convert_alpha()
    bg = pygame.transform.scale(
        bg1, (bg1.get_width() * 1.4,
              bg1.get_height() * 1.9))
    bg_x = 0

    bg_sound = pygame.mixer.Sound('sounds/mi.mp3')
    bg_sound.play()


    running = True
    while running:

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 2400, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
                pygame.quit()

        #print(bg_x)
        clock.tick(15)



switch_scene(scene_menu())
while current_scene is not None:
    current_scene()