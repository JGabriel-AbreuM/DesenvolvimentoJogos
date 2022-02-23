
import pygame 

pygame.init()

#cria tela
altura = 600
largura = 800
tela = pygame.display.set_mode((largura, altura), 0)

while True:
    pygame.draw.line(tela, (255, 0, 0), (40, 300), (400, 0), 3)
    pygame.draw.line(tela, (255, 0, 0), (400, 0), (760, 300), 3)
    pygame.draw.rect(tela, (0, 0, 255), pygame.Rect(40, altura*1/2, largura*9/10, 200), 4)
    pygame.display.update()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()