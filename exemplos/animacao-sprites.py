import pygame
from . import spritesheet

pygame.init()
tela = pygame.display.set_mode((100, 170))
pygame.display.set_caption("Folha de sprites do Sub-Zero")
clock = pygame.time.Clock()

arquivo = "subzero-sprites.png"
folha = spritesheet(arquivo)
pos_primero_sprite = (62, 12, 43, 104)
lista_sprites = folha.tira(pos_primero_sprite, 4, -1)

executando = True
i = 0
while executando:
    tela.fill((255, 255, 255))
    tela.blit(lista_sprites[i], (30, 30))
    i += 1
    if i == len(lista_sprites):
        i = 0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    clock.tick(8)
    pygame.display.flip()

pygame.quit()