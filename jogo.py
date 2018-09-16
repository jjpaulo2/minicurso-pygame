import pygame

pygame.init()

# CORES
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (150, 150, 150)

# DIMENSÕES DA TELA
ALTURA = 600
LARGURA = 800

# DEFINIÇÕES DA JANELA
tela = pygame.display.set_mode([LARGURA, ALTURA])
tela.fill(CINZA)
pygame.display.set_caption("Minha primeira tela")

# CLOCK DO JOGO
clock = pygame.time.Clock()

# SUPERFÍCIES
superficie = pygame.Surface([760, 560])
superficie.fill(BRANCO)

# RETÂNGULOS
quadrado = pygame.Rect(100, 100, 50, 50)

# LOOP DO JOGO
executando = True
while executando:

	# VERIFICANDO EVENTOS
	for evento in pygame.event.get():

		# EVENTO DE FECHAR A TELA
		if evento.type == pygame.QUIT:
			executando = False

		# EVENTOS DE TECLA PRESSIONADA
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_DOWN:
				quadrado.move_ip([0, 20])
			if evento.key == pygame.K_UP:
				quadrado.move_ip([0, -20])
			if evento.key == pygame.K_LEFT:
				quadrado.move_ip([-20, 0])
			if evento.key == pygame.K_RIGHT:
				quadrado.move_ip([20, 0])

	# ELEMENTOS DA TELA
	tela.blit(superficie, [20, 20])
	pygame.draw.rect(tela, VERMELHO, quadrado)

	# CONFIGURAÇÃO DE QUADROS
	clock.tick(27)
	pygame.display.update()

pygame.quit()