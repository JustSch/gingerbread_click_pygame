import pygame
import button

pygame.init()#needed to initialize font

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Cookie Clicker')

cookie_img = pygame.image.load('clicker_images/cookie.png').convert_alpha()
cookie_button = button.Button(100, 300, cookie_img, 5)


gingerbeadman_img = pygame.image.load('clicker_images/gingerbread_man.png').convert_alpha()
gingerbeadman_button = button.Button(300, 300, gingerbeadman_img, 3)
gingerbread_effect_active = False
warning_end = 0
gingerbreadman_event = pygame.USEREVENT + 1
gingerbreadman_warning_event  = pygame.USEREVENT + 2
effect_event = pygame.USEREVENT + 3

show_gingerbread_warning = False

gingerbread_powerup_started = False
gingerbreadman_powerup_not_active = True
effect_toggle = False

points = 0
clock = pygame.time.Clock()

text_font = pygame.font.SysFont(None, 30,bold = True, italic=True)
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

run = True
while run:
    
    screen.fill((202, 228, 241))
    clock.tick(60)
    if gingerbread_powerup_started and gingerbreadman_powerup_not_active:
        pygame.time.set_timer(gingerbreadman_event, 5000) #wait 5 seconds
        pygame.time.set_timer(effect_event, 1000) #wait 1 seconds
        gingerbreadman_powerup_not_active = False
        gingerbread_effect_active = True

    if show_gingerbread_warning:
        if warning_end > pygame.time.get_ticks():
            draw_text("you may not use the gingerbread man yet",text_font,(0,0,0),100,100)
        else:
             show_gingerbread_warning = False

    draw_text("Points: "+str(points),text_font,(0,0,0),0,0)
    if cookie_button.draw(screen):
            points +=1 
            print("cookie clicked")

        
    if gingerbeadman_button.draw(screen):
        if points >= 5 and gingerbread_powerup_started == False:
                print("gingerbread clicked")
                gingerbread_powerup_started = True
                
        else:
            if gingerbreadman_powerup_not_active:
                print("you may not use the gingerbread man yet")
                pygame.event.post(pygame.event.Event(gingerbreadman_warning_event))

    for event in pygame.event.get():
        if event.type == effect_event:
             if gingerbread_effect_active:
                if effect_toggle:
                    gingerbeadman_button = button.Button(300, 300, gingerbeadman_img, 2)
                    effect_toggle = False
                else:
                    gingerbeadman_button = button.Button(300, 300, gingerbeadman_img, 3)
                    effect_toggle = True
                  
        if event.type == gingerbreadman_event:
            points += 5

        if event.type == gingerbreadman_warning_event:
            show_gingerbread_warning = True
            warning_end = pygame.time.get_ticks() + 2000

        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()