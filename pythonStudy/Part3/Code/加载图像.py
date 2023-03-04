'''
File    :   加载图像.py
Time    :   2023/03/04 19:26:33
Author  :   Z-JUNYE 
Version :   1.0
Comment :   加载图像
'''

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((255,255,255))
    ball_image = pygame.image.load('./images/ball.png')
    screen.blit(ball_image,(50,50))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
