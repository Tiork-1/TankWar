# -*- coding = utf-8 -*-
# @Time : 2021/10/21 21:55
# @Author : qiuxinhan
# @File : setting.py
# @Software : PyCharm

import tools as T
import constants
import pygame
class Setting():

    def __init__(self):
        self.myinit()

    def myinit(self):
        # 阶段的参数
        self.finished = False
        self.next = None
        # bgm
        self.bgm = constants.hit_sound

        # 光标贴图并设置初始位置

        self.cursor = pygame.sprite.Sprite()
        tempImage = T.GRAGHIES['cursor']
        tempImage = pygame.transform.rotate(tempImage,-90)
        tempRect = tempImage.get_rect()
        tempImage = pygame.transform.scale(tempImage,(tempRect.width*3,tempRect.height*5))
        self.cursor.image = tempImage
        self.cursor.rect = self.cursor.image.get_rect()
        # 设置光标位置和状态
        self.cursor.state = 1
        self.cursor.rect.x = 100
        self.cursor.rect.y = 210
        # 调整
        self.difficulty_state = 1
        self.select_side1()
        self.select_side2()

        # 选项
        font = pygame.font.SysFont('arial',30,True)
        font1 = pygame.font.SysFont('arial',70,True)
        # rgb
        rgb = (119,136,153)
        # 倍数
        scale1 = 1
        scale2 = 1
        # 背景音乐大小
        self.music_image = font1.render('Music',1,(255,255,255))
        self.music_rect = self.music_image.get_rect()
        self.music_image = pygame.transform.scale(self.music_image,(int(self.music_rect.width*scale2),
                                                          int(self.music_rect.height * scale2)))

        # 无声silent
        self.silent_image = font.render(' Mute ',1,rgb)
        self.silent_rect = self.silent_image.get_rect()
        self.silent_image = pygame.transform.scale(self.silent_image,(int(self.silent_rect.width*scale1),
                                                          int(self.silent_rect.height * scale1)))
        # 较小
        self.low_image = font.render('  Low ',1,rgb)
        self.low_rect = self.low_image.get_rect()
        self.low_image = pygame.transform.scale(self.low_image,(int(self.low_rect.width*scale1),
                                                          int(self.low_rect.height * scale1)))
        # 中等
        self.Medium_image = font.render('Medium',1,rgb)
        self.Medium_rect =  self.Medium_image.get_rect()
        self.Medium_image = pygame.transform.scale( self.Medium_image,(int( self.Medium_rect.width*scale1),
                                                          int( self.Medium_rect.height * scale1)))
        # 较大
        self.high_image = font.render(' High ',1,rgb)
        self.high_rect = self.high_image.get_rect()
        self.high_image = pygame.transform.scale(self.high_image,(int(self.high_rect.width*scale1),
                                                          int(self.high_rect.height * scale1)))

        # 游戏难度
        self.level_image = font1.render('Level',1,(255,255,255))
        self.level_rect = self.level_image.get_rect()
        self.level_image = pygame.transform.scale(self.level_image,(int(self.level_rect.width*scale2),
                                                          int(self.level_rect.height * scale2)))

        # 简单
        self.easy_image = font.render(' Easy ',1,rgb)
        self.easy_rect = self.easy_image.get_rect()
        self.easy_image = pygame.transform.scale(self.easy_image,(int(self.easy_rect.width*scale1),
                                                          int(self.easy_rect.height * scale1)))
        # 中等
        self.medium_image = font.render('Medium',1,rgb)
        self.medium_rect = self.medium_image.get_rect()
        self.medium_image = pygame.transform.scale(self.medium_image,(int(self.medium_rect.width*scale1),
                                                          int(self.medium_rect.height * scale1)))
        # 难
        self.hard_image = font.render(' Hard ', 1, rgb)
        self.hard_rect = self.hard_image.get_rect()
        self.hard_image = pygame.transform.scale(self.hard_image, (int(self.hard_rect.width * scale1),
                                                                       int(self.hard_rect.height * scale1)))
        # 保存
        self.save_image = font1.render('Save',1,(255,255,255))
        self.save_rect = self.save_image.get_rect()
        self.save_image = pygame.transform.scale(self.save_image,(int(self.save_rect.width*scale2),
                                                        int(self.save_rect.height * scale2)))

    def select_side1(self):
        self.cursor1 = pygame.sprite.Sprite()
        tempImage = T.GRAGHIES['side']
        tempImage = pygame.transform.rotate(tempImage, -90)
        tempRect = tempImage.get_rect()
        tempImage = pygame.transform.scale(tempImage, (tempRect.width , tempRect.height * 0.1))
        self.cursor1.image = tempImage
        self.cursor1.rect = self.cursor1.image.get_rect()
        # 设置光标位置和状态
        self.cursor1.state = constants.sound_state
        self.cursor1.rect.x = 410+(constants.sound_state-1)*150
        self.cursor1.rect.y = 225

    def select_side2(self):
        self.cursor2 = pygame.sprite.Sprite()
        tempImage = T.GRAGHIES['side']
        tempImage = pygame.transform.rotate(tempImage, -90)
        tempRect = tempImage.get_rect()
        tempImage = pygame.transform.scale(tempImage, (tempRect.width , tempRect.height * 0.1))
        self.cursor2.image = tempImage
        self.cursor2.rect = self.cursor2.image.get_rect()
        # 设置光标位置和状态
        self.cursor2.state = constants.level_state
        self.cursor2.rect.x = 410+(constants.level_state-1)*150
        self.cursor2.rect.y = 325

    def update(self,keys,surface):
        surface.fill(constants.BLACK)
        self.draw_options(surface)
        self.update_cursor(keys,surface)

    def draw_options(self,surface):
        surface.blit(self.music_image,(200,200))
        surface.blit(self.level_image,(200,300))
        surface.blit(self.save_image,(200,400))

        # music
        surface.blit(self.silent_image,(450,235))
        surface.blit(self.low_image,(600,235))
        surface.blit(self.medium_image,(750,235))
        surface.blit(self.high_image,(900,235))
        # diff
        surface.blit(self.easy_image,(450,335))
        surface.blit(self.medium_image,(600,335))
        surface.blit(self.hard_image,(750,335))


    def update_cursor(self,keys,surface):
        surface.blit(self.cursor.image,self.cursor.rect)
        surface.blit(self.cursor1.image,self.cursor1.rect)
        surface.blit(self.cursor2.image,self.cursor2.rect)

        if keys[pygame.K_UP]:
            self.bgm.play()
            if self.cursor.state > 1:
                self.cursor.state -= 1
                self.cursor.rect.y -= 100
                T.stop(200)
        elif keys[pygame.K_DOWN]:
            self.bgm.play()
            if self.cursor.state < 3:
                self.cursor.state += 1
                self.cursor.rect.y += 100
                T.stop(200)
        elif keys[pygame.K_LEFT]:
            if self.cursor.state == 1:
                if self.cursor1.state > 1:
                    self.cursor1.state -= 1
                    constants.sound_level[0] = constants.sound_level[self.cursor1.state]
                    constants.sound_state -= 1
                    self.cursor1.rect.x -= 150
            if self.cursor.state == 2:
                if self.cursor2.state > 1:
                    self.cursor2.state -= 1
                    constants.level_state -= 1
                    constants.SPEED_LOW = constants.speed_low_array[constants.level_state]
                    constants.SPEED_MID = constants.speed_mid_array[constants.level_state]
                    constants.SPEED_HIGH = constants.speed_high_array[constants.level_state]
                    constants.light_num = constants.light_num_array[constants.level_state]
                    constants.mid_num1 = constants.mid_num1_array[constants.level_state]
                    constants.mid_num2 = constants.mid_num2_array[constants.level_state]
                    self.cursor2.rect.x -= 150
            T.stop(200)
        elif keys[pygame.K_RIGHT]:
            if self.cursor.state == 1:
                if self.cursor1.state < 4:
                    self.cursor1.state += 1
                    constants.sound_level[0] = constants.sound_level[self.cursor1.state]
                    constants.sound_state += 1
                    constants.level_state += 1
                    constants.SPEED_LOW = constants.speed_low_array[constants.level_state]
                    constants.SPEED_MID = constants.speed_mid_array[constants.level_state]
                    constants.SPEED_HIGH = constants.speed_high_array[constants.level_state]
                    constants.light_num = constants.light_num_array[constants.level_state]
                    constants.mid_num1 = constants.mid_num1_array[constants.level_state]
                    constants.mid_num2 = constants.mid_num2_array[constants.level_state]
                    self.cursor1.rect.x += 150
            if self.cursor.state == 2:
                if self.cursor2.state < 3:
                    self.cursor2.state += 1
                    self.cursor2.rect.x += 150
            T.stop(200)
        elif keys[pygame.K_RETURN]:
            if self.cursor.state == 3:
                self.finished = True
                self.next = 'mainMenu'
            T.stop(200)