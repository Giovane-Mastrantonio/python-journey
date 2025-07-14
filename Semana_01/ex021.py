# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
# Ver modulos, sempre menos linhas

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer_music.play()
pygame.event.wait()
