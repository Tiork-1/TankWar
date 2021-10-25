# -*- coding = utf-8 -*-
# @Time : 2021/10/22 22:54
# @Author : qiuxinhan
# @File : bullet.py
# @Software : PyCharm
import pygame.sprite

import constants
import tools as T


class bullet(pygame.sprite.Sprite):
    # 创建子弹必须指定x,y,方向，阵营
    def __init__(self,x,y,_direction,_camp):
        pygame.sprite.Sprite.__init__(self)
        # 加载图片
        self.load_image()
        # 初始化参数
        self.image = self.up_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dead = False

        # 设置飞行的参数
        self.speed = 10
        self.direction = _direction
        if _direction == 'up':
            self.image = self.up_image
        elif _direction == 'right':
            self.image = self.right_image
        elif _direction == 'left':
            self.image = self.left_image
        elif _direction == 'down':
            self.image = self.down_image
        # 阵营，1代表右方
        self.camp = _camp

    # 加载图片
    def load_image(self):
        bullet_main_image = T.GRAGHIES['bullet']
        bullet_main_rect = bullet_main_image.get_rect()
        self.bullet_scale = 1
        bullet_main_image = pygame.transform.scale(bullet_main_image,
                                                   (bullet_main_rect.width * self.bullet_scale,
                                                    bullet_main_rect.height*self.bullet_scale))

        self.up_image = bullet_main_image
        self.right_image = pygame.transform.rotate(bullet_main_image,-90)
        self.left_image = pygame.transform.rotate(bullet_main_image,90)
        self.down_image = pygame.transform.rotate(bullet_main_image,180)

    # 更新
    def update(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'down':
            self.rect.y += self.speed

    # 消失
    def disapear(self,group):
        self.dead = True

        group.remove(self)