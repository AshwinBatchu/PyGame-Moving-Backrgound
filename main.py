import pygame

pygame.init()

black = pygame.color.Color('#000000')
white = pygame.color.Color('#ffffff')


screen = pygame.display.set_mode((1000,700))
run = True

backgro = pygame.image.load("media/bACKGRo.jpg")
rescaled = pygame.transform.scale(backgro,(1000,700))

def displayText(string1,x,y):
    font = pygame.font.Font("media/LeviReBrushed.ttf",40)
    text1 = font.render(string1,True,white)
    screen.blit(text1,(x,y))
wid = 1000
i = 0
while run :
    
    
    
    screen.fill(black)
    screen.blit(rescaled,(i,0))
    screen.blit(rescaled,(wid+i,0))
   
    if i == -wid:
        screen.blit(rescaled,(wid+i,0))
        i = 0 
    i = i-1
    displayText("Start Game",400,250)
    displayText("Settings",400,350)
    displayText("Quit Game",400,450)
    pygame.display.update()              
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
