import pygame


pygame.init()
clock = pygame.time.Clock()
image_path = '/data/data/Gnom_VS_AgrGnom.myapp/files/app'

screen = pygame.display.set_mode((1400, 788))
pygame.display.set_caption("Межвузовский студенческий городок")
icon = pygame.image.load('images/Vampir.Jpg').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load('images/forest.png').convert_alpha()
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

player_anim_count = 0
bg_x = 0
ghost1 = pygame.image.load('images/olka.png').convert_alpha()
Dead1 = pygame.image.load('images/Dead.jpg').convert_alpha()
ghost = pygame.transform.scale(
    ghost1, (ghost1.get_width() // 8,
               ghost1.get_height() // 8)) #уменьшение Оли(врага)

Dead = pygame.transform.scale(
    Dead1, (Dead1.get_width() // 4,
               Dead1.get_height() // 4))

ghost_x = 2700
ghost_y = 650

player_speed = 2
player_x = 300
player_y = 650
label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
lose_label = label.render('Вы проиграли!', False, (193, 196, 199))
restart_label = label.render("Играть заново", False, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(560, 360))

bullet1 = pygame.image.load('images/bullet.png').convert_alpha()
bullet = pygame.transform.scale(
    bullet1, (bullet1.get_width() // 6,
               bullet1.get_height() // 6))
bullets = []

is_jump = False
jump_count = 9

bg_sound = pygame.mixer.Sound('sounds/moon.mp3')
#bg_sound.play()

gameplya = True

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 5500)
bullets_left = 8

start_label = label.render("Начать игру", False, (115, 132, 148))
start_label_rect = start_label.get_rect(topleft=(560, 360))




'''while menu:

    screen.fill((218, 31, 224))
    screen.blit(start_label, start_label_rect)

    mouse = pygame.mouse.get_pos()
    if start_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:



    pygame.display.update()
'''

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(label.render(option, True, (115, 132, 148)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index =max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)

menu = Menu()
menu.append_option('Hello', lambda: print(a))
menu.append_option('Quit', quit)


running = True
while running:
    screen.fill((0, 0, 0))
    menu.draw(screen, 100, 100, 75)

    if a == 1:




        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 1400, 0))

        if gameplya:


            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

            if ghost_list_in_game:
                for (i,el) in enumerate(ghost_list_in_game):
                    screen.blit(ghost, el)
                    el.x -= 10

                    if el.x < -100:
                        ghost_list_in_game.pop()

                    if player_rect.colliderect(el):
                        gameplya = False


            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))

            if keys[pygame.K_LEFT] and player_x > 50:
                player_x -= player_speed
            elif keys[pygame.K_RIGHT] and player_x < 250:
                player_x += player_speed

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

            bg_x -= 12
            if bg_x == -1380:
                bg_x = 0




            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x, el.y))
                    el.x += 4

                    if el.x > 2000:
                        bullets.pop()

                    if ghost_list_in_game:
                        for (index, ghost_el) in enumerate(ghost_list_in_game):
                            if el.colliderect(ghost_el):
                                ghost_list_in_game.pop(index)
                                bullets.pop(i)

        else:
            screen.fill((87, 88, 89))
            screen.blit(lose_label, (560, 220))
            #screen.blit(Dead, (560, 350))
            screen.blit(restart_label, restart_label_rect)

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplya = True
                player_x = 300
                ghost_list_in_game.clear()
                bullets.clear()
                bullets_left = 8





    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            menu.switch(-1)
        elif keys[pygame.K_s]:
            menu.switch(1)
        elif keys[pygame.K_e]:
            menu.select()


        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1620, 600)))

        if gameplya and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 10, player_y - 40)))
            bullets_left -= 1

    clock.tick(7)

