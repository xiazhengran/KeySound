import keyboard
import pygame
import threading
import os
import random

pygame.mixer.init()
pygame.mixer.music.load('./keysound/q.mp3')
pygame.mixer.music.set_volume(1)

def play():
    pygame.mixer.music.play()


# 按下键盘
def Press(x):
    if x.event_type == 'down':
        threading.Thread(target=play).start()


# 入口函数
if __name__ == '__main__':
    keyboard.hook(Press)
    keyboard.wait()
