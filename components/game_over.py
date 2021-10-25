# -*- coding = utf-8 -*-
# @Time : 2021/10/21 22:01
# @Author : qiuxinhan
# @File : game_over.py
# @Software : PyCharm
import pygame.sprite

import constants
import tools as T


class GameOver():
    def __init__(self):
        self.myinit()

    def myinit(self):
        self.bgm = constants.hit_sound
        # 阶段的参数
        self.finished = False
        self.next = None

        # 加载背景图片
        self.main_image = T.GRAGHIES['game_over']
        self.main_rect = self.main_image.get_rect()
        self.main_image = pygame.transform.scale(self.main_image,(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
        # 加载选项图片

        # 光标贴图并设置初始位置
        self.cursor = pygame.sprite.Sprite()
        tempImage = T.GRAGHIES['cursor']
        tempImage = pygame.transform.rotate(tempImage,-90)
        tempRect = tempImage.get_rect()
        tempImage = pygame.transform.scale(tempImage,(tempRect.width*2,tempRect.height*2))
        self.cursor.image = tempImage
        self.cursor.rect = self.cursor.image.get_rect()
        # 设置光标位置和状态
        self.cursor.state = 1
        self.cursor.rect.x = 535
        self.cursor.rect.y = 555
        # 选项贴图
        font = pygame.font.SysFont('FixedSys.ttf',46,True)
        # 重新开始
        self.restart_image = font.render('Restart',1,(255,255,255))
        self.restart_rect = self.restart_image.get_rect()
        self.restart_image = pygame.transform.scale(self.restart_image,(int(self.restart_rect.width*1.25),
                                                          int(self.restart_rect.height * 1.25)))

        # 返回主菜单
        self.return_image = font.render('Return to the mainmenu',1,(255,255,255))
        self.return_rect = self.return_image.get_rect()
        self.return_image = pygame.transform.scale(self.return_image,(int(self.return_rect.width*1.25),
                                                          int(self.return_rect.height * 1.25)))


    def update(self,keys,surface):
        self.draw_background(surface)
        self.draw_options(surface)
        self.update_cursor(keys,surface)

    def draw_background(self,surface):
        surface.blit(self.main_image,(0,0))


    def draw_options(self,surface):
        surface.blit(self.restart_image,(600,550))
        surface.blit(self.return_image,(600,600))

    def update_cursor(self,keys,surface):
        surface.blit(self.cursor.image,self.cursor.rect)

        if keys[pygame.K_UP]:
            self.bgm.play()
            self.bgm.set_volume(constants.sound_level[0])
            if self.cursor.state == 2:
                self.cursor.state = 1
                self.cursor.rect.y -= 50
        elif keys[pygame.K_DOWN]:
            self.bgm.play()
            self.bgm.set_volume(constants.sound_level[0])
            if self.cursor.state == 1:
                self.cursor.state = 2
                self.cursor.rect.y += 50
        elif keys[pygame.K_RETURN]:
            self.bgm.play()
            self.bgm.set_volume(constants.sound_level[0])
            if self.cursor.state == 1:
                self.finished = True
                self.next = 'level01'
            if self.cursor.state == 2:
                self.finished = True
                self.next = 'mainMenu'
            T.stop(200)