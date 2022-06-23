import pygame
import random

pygame.init()
altura = 300
largura = 800
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Missão Impossível")
bg = pygame.image.load("assets/background.jpg")
bg_destroy = pygame.image.load("assets/bg_preso.png")


gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()

gameIcon = pygame.image.load("assets/missao_impossivel_ico.ico")
pygameDisplay.set_icon(gameIcon)

black = (0, 0, 0)
white = (255, 255, 255)


loserSound = pygame.mixer.Sound("assets/perdeu.mp3")
loserSound.set_volume(0.5)

laserSound = pygame.mixer.Sound("assets/laser.mp3")
laserSound.set_volume(0.5)


def dead(pontos):
    gameDisplay.blit(bg_destroy, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(loserSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    texto = fonte.render(f"Você foi pego com {str(pontos)} pontos!", True, black)
    gameDisplay.blit(texto, (50, 100))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    textoContinue = fonteContinue.render("press enter to restart", True, black)
    gameDisplay.blit(textoContinue, (50, 200))

    pygameDisplay.update()


def jogo():
    jogando = True
    movimentoX = 0
    movimentoY = random.randrange(0, altura)
    velocidade = 1
    direcao = True
    posicaoXPlayer = 450
    posicaoYPlayer = 100
    movimentoXPlayer = 0
    movimentoYPlayer = 0
    pontos = 0
    laser = pygame.image.load("assets/laser.png")
    laser = pygame.transform.flip(laser, True, False)
    player = pygame.image.load("assets/player.png")
    pygame.mixer.music.load("assets/missao_impossivel.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.Sound.play(laserSound)
    larguraPlayer = 270
    alturaPlayer = 129
    larguraLaser = 138
    alturaLaser = 47
    limiar = 28
    velocidadePlayer = 10

    while True:
        # aqui será feito a leitura dos comandos
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoXPlayer = -velocidadePlayer
                elif event.key == pygame.K_RIGHT:
                    movimentoXPlayer = velocidadePlayer
                elif event.key == pygame.K_UP:
                    movimentoYPlayer = -velocidadePlayer
                elif event.key == pygame.K_DOWN:
                    movimentoYPlayer = velocidadePlayer
                elif event.key == pygame.K_RETURN:
                    jogo()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXPlayer = 0
                    movimentoYPlayer = 0

        if jogando == True:
            # Jogo

            # Controlando limites do player
            posicaoXPlayer = posicaoXPlayer + movimentoXPlayer
            if posicaoXPlayer < 0:
                posicaoXPlayer = 0
            elif posicaoXPlayer > largura - larguraPlayer:
                posicaoXPlayer = largura - larguraPlayer

            posicaoYPlayer = posicaoYPlayer + movimentoYPlayer
            if posicaoYPlayer < 0:
                posicaoYPlayer = 0
            elif posicaoYPlayer > altura - alturaPlayer:
                posicaoYPlayer = altura - alturaPlayer

            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(player, (posicaoXPlayer, posicaoYPlayer))
            gameDisplay.blit(laser, (movimentoX, movimentoY))

            if direcao == True:
                if movimentoX <= 800 - 150:
                    movimentoX = movimentoX + velocidade
                else:
                    pygame.mixer.Sound.play(laserSound)
                    direcao = False
                    pontos = pontos + 1
                    movimentoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    laser = pygame.transform.flip(laser, True, False)
            else:
                if movimentoX >= 0:
                    movimentoX = movimentoX - velocidade
                else:
                    pygame.mixer.Sound.play(laserSound)
                    direcao = True
                    pontos += 1
                    movimentoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    laser = pygame.transform.flip(laser, True, False)

            # atualização de tela
            fonte = pygame.font.Font('freesansbold.ttf', 20)
            texto = fonte.render(f"Pontos: {str(pontos)}", True, white)
            gameDisplay.blit(texto, (20, 280))

            # controle de colisão
            pixelYLaser = list(range(movimentoY, movimentoY+alturaLaser + 1))
            pixelXLaser = list(range(movimentoX, movimentoX+larguraLaser + 1))

            pixelYPlayer = list(range(posicaoYPlayer, posicaoYPlayer + alturaPlayer +1 ))
            pixelXPlayer = list(range(posicaoXPlayer, posicaoXPlayer + larguraPlayer +1 ))

            colisaoY = list( set(pixelYLaser) & set(pixelYPlayer)  )
            colisaoX = list( set(pixelXLaser) & set(pixelXPlayer)  )
            if len(colisaoY) > limiar:
                if len(colisaoX) > limiar:
                    jogando =  False
                    dead(pontos)

        pygameDisplay.update()
        clock.tick(60)
jogo()