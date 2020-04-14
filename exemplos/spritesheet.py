import pygame


class spritesheet:

    def __init__(self, arquivo):
        self.sheet = pygame.image.load(arquivo).convert()

    def imagem_em(self, rect, cor_alfa=None):
        retangulo = pygame.Rect(rect)
        imagem = pygame.Surface(retangulo.size).convert()
        imagem.blit(self.sheet, (0, 0), retangulo)
        if cor_alfa is not None:
            if cor_alfa == -1:
                cor_alfa = imagem.get_at((0, 0))
            imagem.set_colorkey(cor_alfa)
        return imagem

    def imagens_em(self, rects, cor_alfa=None):
        return [self.imagem_em(rect, cor_alfa) for rect in rects]

    def tira(self, primeiro_rect, quantidade, cor_alfa=None):
        retangulos = [(primeiro_rect[0]+primeiro_rect[2]*i, primeiro_rect[1], primeiro_rect[2], primeiro_rect[3]) for i in range(quantidade)]
        return self.imagens_em(retangulos, cor_alfa)
