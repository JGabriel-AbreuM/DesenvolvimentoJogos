import pygame

pygame.init()


altura = 600
largura = 800
tela = pygame.display.set_mode((largura, altura), 0)

x = 25
y = 25

velocidadeX = 0.5
velocidadeY = 0.5

while True:

    tecla = pygame.key.get_pressed()
    tela.fill((0, 0, 0, 0))
    pygame.draw.circle(tela, (255, 255, 0), (x, y), 25, width=0)

    if tecla[ord("w")] == 1:
        y -= velocidadeY
    
    if tecla[ord("a")] == 1:
        x -= velocidadeX

    if tecla[ord("d")] == 1:
        x += velocidadeX

    if tecla[ord("s")] == 1:
        y += velocidadeX

    if x > largura:
        x = 25
    
    elif x < 0:
        x = largura

    if y > altura:
        y = 25
    
    if y < 0:
        y = altura


    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()