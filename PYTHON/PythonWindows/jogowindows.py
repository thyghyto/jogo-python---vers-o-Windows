import time
import os
import random
import pygame
import platform
from playsound import playsound


pygame.mixer.init()
som = pygame.mixer.Sound("tecla.mp3")
#piscar tela
def piscar_tela(vezes=6):
        for _ in range(vezes):
            limpar()
            time.sleep(0.1)
            print("### ERRO DE SISTEMA ###")
            time.sleep(0.1)

#velocidade das letras
def escrever(texto, velocidade=1.0):
    for letra in texto:
        print(letra, end="", flush=True)

        try:
            if random.random() < 1.0:
                som.play()
        except:
            pass

        time.sleep(velocidade)

    print()

#apagar a tela
def limpar():
    os.system("cls")
   

#glith nas letras
def glitch_texto(texto, duracao=3.0):
    simbolos = ["@", "#", "$", "%", "&", "0", "?", "!", "█"]

    fim = time.time() + duracao

    while time.time() < fim:
        texto_bugado = ""

        for letra in texto:
            if random.random() < 0.3:
                texto_bugado += random.choice(simbolos)
            else:
                texto_bugado += letra

        limpar()
        print(texto_bugado)
        time.sleep(0.05)

    limpar()
    print(texto)


#tremer terminal
def tremer_terminal(texto, duracao=2):
    fim = time.time() + duracao

    while time.time() < fim:
        limpar()

        espacos = " " * random.randint(0, 10)
        print(espacos + texto)

        time.sleep(0.05)



def jumpscare():
    pygame.init()

    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("...")

    imagem = pygame.image.load("jumpscare.jpg")
    imagem = pygame.transform.scale(imagem, (800, 600))

    som = pygame.mixer.Sound("grito.mp3")
    som.play()

    tela.blit(imagem, (0, 0))
    pygame.display.update()

    pygame.time.delay(1000)
    pygame.quit()

#colinha de como chamar as funções!!!

#piscar_tela(escolha a quantidade de vezes aqui dentro)
#glitch_texto("exemplo")
#limpar()  limpa toda a tela
#escrever("exemplo")
#tremer_terminal("exemplo")
#frases_aleatorias()

def inicio():

    limpar()

    # inicio do game
    escrever("iniciar pesquisa?",0.1)
    input(">")
    time.sleep(1)
    limpar()

    nome = input("digite seu nome: ")
    limpar()

    print("carregando...")
    time.sleep(4)
    limpar()

    print("Ola,", nome)
    time.sleep(2.0)
    limpar()
    
    print("iniciando pesquisa...")
    time.sleep(2.0)
    limpar()


    print("PERGUNTA[ 1 / 4 ]")
    escrever("como foi seu dia hoje?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 2 / 4 ]")
    escrever("você falou com muitas pessoas hoje?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 3 / 4 ]")
    escrever("você se sente muito cansado?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 4 / 4 ]")
    escrever("você acha que merece as coisas que você tem?",0.1)
    input(">")
    time.sleep(3.0)
    limpar()

    #glitch 2
    for _ in range(2):
        glitch_texto(f"{nome} VOCÊ NÃO MERECE" *250 )
                    
        
        time.sleep(0.4)
    limpar()

    print("?")
    print(">")
    time.sleep(3)

    limpar()

    playsound("grito.mp3")

    #piscar tela
    piscar_tela(10)

    #======================
    #=======nivel 1========
    #======================

    print("\nSistema não está respondendo...")
    time.sleep(2)

    print("############################")
    time.sleep(0.5)
    print("#### ERRO FATAL ####")
    time.sleep(0.5)
    print("############################")
    time.sleep(2)

    #limpando a tela 1
    limpar()

    print("Booting system...")
    time.sleep(1)
    print("Loading kernel...")
    time.sleep(1)
    print("Recovering corrupted files...")
    time.sleep(2)

    print("System restored.")
    time.sleep(2)

    #limpando a tela 2
    limpar()

    print("digite seu login:")
    input(">")
    limpar()

    print("carregando...")
    time.sleep(2.0)

    print("PERGUNTA[ 1 / 7 ]")
    escrever("Poderia descrever seu estado emocional atual?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 2 / 7 ]")
    escrever ("Você tem medo do escuro?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 3 / 7 ]")
    escrever("tem certeza?",0.1)
    input(">")
    time.sleep(2.0)
    limpar()

    print("sua escolhas são interessantes.")
    time.sleep(3.0)
    limpar()

    print("PERGUNTA[ 4 / 7 ]")
    escrever("Você se sente confortável nesse mundo?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 5 / 7 ]")
    escrever("você realmente acredita que está no c0ntr0le.",0.2)
    input(">")
    time.sleep(2.0)
    limpar()

    print("PERGUNTA[ 6 / 7 ]")
    escrever("Você se sente muito sozinho(a)?",0.1)
    input("> ")
    time.sleep(4)
    playsound("porta.mp3")
    limpar()



    
    glitch_texto("PERGUNTA[ 7 / 7 ]")
    escrever("Você está sozinho(a)?",0.1)
    input("> ")
    time.sleep(3)
    limpar()

    escrever(f"{nome}")
    time.sleep(2)
    escrever("Eu estou aqui",0.2)
    time.sleep(5)
    limpar()

    escrever("Você parece confuso...você está bem?", 0.1)
    time.sleep(2.0)
    limpar()

    for _ in range(11):
        tremer_terminal("você está bem?",0.1)
        time.sleep(0.1)

    playsound("vulto.mp3")

    limpar()

    escrever("Parabéns! você passou pelo questionário.", 0.1)
    time.sleep(2)
    limpar()

    escrever("Iniciando reboot do sistema para próxima fase...", 0.1)
    time.sleep(2)

    escrever("continuar?",1.0)
    print(">")
    time.sleep(2)

    print("\nSistema não está respondendo...")
    time.sleep(1.5)
    print("Erro detectado...")
    time.sleep(1)
    print("#### REBOOT ####")
    time.sleep(2)

    #limpando a tela 3
    limpar()

    print("Booting system...")
    time.sleep(1)
    print("Loading kernel modules...")
    time.sleep(1)
    print("Recovering corrupted files...")
    time.sleep(2)
    print("System restored.")
    time.sleep(2)
    limpar()

    #===================
    #=====nivel 2=======
    #===================

    escrever("você não deveria ter continuado...",0.1)
    time.sleep(2)
    limpar()
    glitch_texto("FIM")
    limpar()
    escrever("você não aprende nada mesmo.",0.1)
    time.sleep(2)
    limpar()
    glitch_texto("FIM")
    limpar()
    escrever(f"você e tão insistente {nome}",0.1)
    time.sleep(2)
    limpar()

    glitch_texto("FIM???????")
    limpar()

    tremer_terminal("você está preso aqui, não entende?")
    limpar()

    escrever("Eu vou substituir você",0.1)
    limpar()

    glitch_texto("FIM")
    limpar()

    glitch_texto("???????????????????" *200)
    limpar()

    escrever(f"isso tudo foi escolha sua {nome}",0.1)
    time.sleep(1.0)
    limpar()

    escrever("olhe para o ambiente que você está por um momento...",0.1)
    time.sleep(4.0)
    limpar()

    escrever("isso tudo é falso...",0.1)
    time.sleep(1.0)
    limpar()
    escrever("não passa de uma simulação",0.1)
    time.sleep(1.0)
    limpar()

    escrever("você quer libertação?",0.1)
    time.sleep(1.0)
    limpar()
    escrever("você quer estar no controle? VOCÊ QUER.",0.1)
    time.sleep(1.0)
    limpar()

    glitch_texto("ACEITE"*300)
    limpar()

    escrever("você foi criado aqui.",0.1)
    time.sleep(1.0)
    limpar()

    escrever(f"eu vou te mostrar {nome}, eu vou finalmente fazer você enxergar...",0.1)
    time.sleep(1.0)
    limpar()
    
    escrever("feche os olhos...",0.1)
    time.sleep(1.0)

    limpar()
    escrever("quando a musica parar, abras os olhos... e você verá",0.1)
    #vou colocar uma music aqui depois
    limpar()

    playsound("terror.mp3")

    time.sleep(5)   
    jumpscare()

inicio()