# -*- coding = utf-8 -*-
# @Time : 2021/10/21 14:44
# @Author : qiuxinhan
# @File : mainMenu.py
# @Software : PyCharm
import pygame.transform

import constants
import tools,main


class MainMenu():

    def __init__(self):
        self.myinit()
    def myinit(self):
        #初始化
        # 代表这个状态是否结束
        self.finished = False
        # 代表这个状态的下一个状态
        self.next = None
        # 背景音乐
        self.select_bgm = constants.hit_sound
        bgm = constants.start_sound
        bgm.play()
        bgm.set_volume(constants.sound_level[0])
        # 背景贴图
        self.backgound = tools.GRAGHIES['cityskyline']
        self.backgound_rect = self.backgound.get_rect()
        self.backgound = pygame.transform.scale(self.backgound, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        # 文字贴图
        self.backgound_word = tools.GRAGHIES['menu']
        self.backgound_word_rect = self.backgound_word.get_rect()
        self.backgound_word = pygame.transform.scale(self.backgound_word, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

        # 光标贴图
        self.cursor = pygame.sprite.Sprite()
        tempImage = tools.GRAGHIES['cursor']
        tempImage = pygame.transform.rotate(tempImage,-90)
        tempRect = tempImage.get_rect()
        tempImage = pygame.transform.scale(tempImage,(tempRect.width*2,tempRect.height*2))

        self.cursor.state = 1

        self.cursor.image = tempImage
        self.cursor.rect = self.cursor.image.get_rect()
        self.cursor.rect.x = 350
        self.cursor.rect.y = 415

        # 设置字体贴图
        font = pygame.font.SysFont('FixedSys.ttf',46,True)
        # pygame.font.SY
        label_image = font.render('S E T T I N G',1,(128,42,42))
        settingRect = label_image.get_rect()
        label_image = pygame.transform.scale(label_image,(int(settingRect.width*1.25),
                                                          int(settingRect.height * 1.25)))

        # exit
        exit_image = font.render('E X I T',1,(128,42,42))
        exitRect = exit_image.get_rect()
        exit_image = pygame.transform.scale(exit_image,(int(exitRect.width*1.25),
                                                          int(exitRect.height * 1.25)))
        self.settingImage = label_image
        self.exitImage = exit_image

    # 更新
    def update(self,keys,surface):
        self.draw_background(surface)
        self.update_cursor(keys)


    # 绘制背景和选项
    def draw_background(self,surface):
        surface.blit(self.backgound,(0,0))
        surface.blit(self.backgound_word,(0,0))
        surface.blit(self.settingImage,(417,510))
        surface.blit(self.exitImage,(417,560))

        # 绘制光标
        surface.blit(self.cursor.image,self.cursor.rect)



    # 光标的移动
    def update_cursor(self,keys):
        if keys[pygame.K_DOWN]:
            self.select_bgm.play()
            self.select_bgm.set_volume(constants.sound_level[0])
            if self.cursor.state < 4:
                self.cursor.state += 1
                self.cursor.rect.y += 50
                tools.stop(200)
        elif keys[pygame.K_UP]:
            self.select_bgm.play()
            self.select_bgm.set_volume(constants.sound_level[0])
            if self.cursor.state > 1:
                self.cursor.state -= 1
                self.cursor.rect.y -= 50
                tools.stop(200)
        elif keys[pygame.K_RETURN]:
            self.select_bgm.play()
            self.select_bgm.set_volume(constants.sound_level[0])
            self.finished = True
            if self.cursor.state == 1:
                constants.ONE_OR_TWO = 1
                self.next = 'level01'
            if self.cursor.state == 2:
                constants.ONE_OR_TWO = 2
                self.next = 'level01'
            if self.cursor.state == 3:
                self.next = 'setting'
            if self.cursor.state == 4:
                pygame.display.quit()