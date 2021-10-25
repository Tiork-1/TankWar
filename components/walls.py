# -*- coding = utf-8 -*-
# @Time : 2021/10/21 22:26
# @Author : qiuxinhan
# @File : walls.py
# @Software : PyCharm
import pygame
import constants as C
import tools as T


class Wall(pygame.sprite.Sprite):
    def __init__(self,type,x,y,is_home):
        # 先初始化精灵类
        pygame.sprite.Sprite.__init__(self)

        self.type = type
        self.is_home = is_home
        self.image = self.wall_image(type)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # 墙体消失
        self.dead = False
        self.dead_index = -1

        # 爆炸贴图
        dead_main_image = T.GRAGHIES['explode']
        scale2 = 0.25*0.5
        self.dead_image = [T.get_image(dead_main_image, 703, 363, 350, 350, scale2),
                           T.get_image(dead_main_image, 352, 363, 350, 350, scale2),
                           T.get_image(dead_main_image, 24, 363, 350, 350, scale2),
                           T.get_image(dead_main_image, 669, 27, 350, 350, scale2),
                           T.get_image(dead_main_image, 339, 27, 350, 350, scale2),
                           T.get_image(dead_main_image, 0, 27, 350, 350, scale2)]


    def wall_image(self,type):
        image = None
        wall_scale = 2*C.WALL_SCALE
        mainImage = T.GRAGHIES['walls']
        if type == 1:
            image = T.get_image(mainImage,0,0,32,32,wall_scale)
        elif type == 2:
            image = T.get_image(mainImage,32,0,32,32,wall_scale)
        elif type == 3:
            image = T.get_image(mainImage,64,0,32,32,wall_scale)
        elif type == 4:
            image = T.get_image(mainImage,160,0,32,32,wall_scale)
        return image

    def update(self):
        if self.dead == True:
            self.dead_index+=1
            self.go_disapear(self.dead_index)
        else:
            self.dead_index = -1

    def go_disapear(self,index):
        index/=2
        index = int(index)
        if(index == 6):
            self.group.remove(self)
        else:
            self.image = self.dead_image[index%6]

    def disapear(self,group):
        if self.type == 1:
            self.dead = True
        self.group = group






