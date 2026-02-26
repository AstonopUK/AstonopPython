import pygame
pygame.init()

screen = pygame.display.set_mode([1280,720])
x = 0
y = 0
colour = (0, 255, 255)
direction = ''
screen.fill((255,255,255))
pygame.display.set_caption('Game Test')
font = pygame.font.Font('freesansbold.ttf', 32)
editableText = "Shot ready"
textColour = (0, 255, 0, 255)
text = font.render(editableText, True, textColour)
textRect = text.get_rect()
textRect.center = (100, 20)

def fireLoop():
    boolFire = False
    if boolFire == False:
        boolFire = True
        editableText = "Reloading"
        textColour = (255, 0, 0, 255)
        localx = x
        localy = y
    elif boolFire == True:
        timeCircle = pygame.time.get_ticks()
        match direction:
            case 'r':
                print("FIRING" + str(pygame.time.get_ticks()))
                if (pygame.time.get_ticks() < timeCircle + 100):
                    localx -= 2
                    pygame.draw.circle(screen, (255,0,0), (localy,localx), 10)
                else:
                    boolFire = False
                    textColour = (0, 255, 0, 255)
                    editableText = "Shot ready"
            case 'l':
                print("FIRING" + str(pygame.time.get_ticks()))
                if (pygame.time.get_ticks() < timeCircle + 100):
                    localx -= 2
                    pygame.draw.circle(screen, (255,0,0), (localy,localx), 10)
                else:
                    boolFire = False
                    textColour = (0, 255, 0, 255)
                    editableText = "Shot ready"
            case 'u':
                print("FIRING" + str(pygame.time.get_ticks()))
                if (pygame.time.get_ticks() < timeCircle + 100):
                    localx -= 2
                    pygame.draw.circle(screen, (255,0,0), (localy,localx), 10)
                else:
                    boolFire = False
                    textColour = (0, 255, 0, 255)
                    editableText = "Shot ready"
            case 'd':
                print("FIRING" + str(pygame.time.get_ticks()))
                print(pygame.time.get_ticks() & timeCircle)
                if (pygame.time.get_ticks() < timeCircle + 100):
                    localx -= 2
                    pygame.draw.circle(screen, (255,0,0), (localy,localx), 10)
                else:
                    boolFire = False
                    textColour = (0, 255, 0, 255)
                    editableText = "Shot ready"
            case _:
                print("Catch case")

running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        x -= 0.5
    if keys[pygame.K_DOWN]:
        x += 0.5
    if keys[pygame.K_LEFT]:
        y -= 0.5
    if keys[pygame.K_RIGHT]:
        y += 0.5
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                direction = 'r'
                fireLoop()
            elif event.key == pygame.K_s:
                direction = 'd'
                fireLoop()
            elif event.key == pygame.K_a:
                direction = 'l'
                fireLoop()
            elif event.key == pygame.K_w:
                direction = 'u'
                fireLoop()
    
    pygame.draw.circle(screen, colour, (y,x), 50)
    
    text = font.render(editableText, True, textColour)
    screen.blit(text, textRect)
    
    pygame.display.flip()
    
pygame.quit()