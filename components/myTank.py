# -*- coding = utf-8 -*-
# @Time : 2021/10/21 14:43
# @Author : qiuxinhan
# @File : myTank.py
# @Software : PyCharm
import pygame
import constants as C
import tools as T
from components import bullet


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self,_x,_y,_life):
        # 先初始化精灵类
        pygame.sprite.Sprite.__init__(self)
        self.life = _life
        self.load_image()
        self.index_now = 0
        # 音效
        self.shoot_bgm = C.Gunfire_sound
        self.dead_bgm = C.blast_sound
        # 处理死亡复活的参数
        self.dead = False
        self.relive = False
        self.index_dead = -1
        self.index_relive = -1
        # 设置精灵的默认图像
        self.image = self.up_image[0]
        # 放缩图片到自己想要的大小，第一个参数是图像本身，第二个参数是放缩后的图像大小
        # self.image = pygame.transform.scale(self.image,(32*self.tank_scale,32*self.tank_scale))  #图片的放缩
        # self.image.fill(C.GREEN)
        # rect代表的是这一个图形的矩形区域，同时也代表着这一个精灵的区域
        self.rect = self.image.get_rect()
        # 设置位置
        self.rect.x = _x
        self.rect.y = _y
        self.relive_position_x = _x
        self.relive_position_y = _y
        # 其他参数
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        self.speed = C.YOUR_SPEED
        self.role = 1
        self.pre_shoot_time = 0
        # 坦克的方向
        self.direction = 'up'
        # 子弹是否存活和子弹是否存在
        self.bullet_exist = False
        self.bullet = None

        # 设置悬浮在头顶的名字
        font = pygame.font.SysFont('arial',14,True)
        self.name_image = font.render('YOU',1,(0,255,0))
        self.name_rect = self.name_image.get_rect()


    def shoot(self):
        if self.bullet != None and self.bullet.dead != True:
            return 0
        # 两次子弹射击间隔必须大于0.6s
        timer = pygame.time.get_ticks()
        if timer - self.pre_shoot_time < 600:
            return 0
        self.shoot_bgm.play()
        self.shoot_bgm.set_volume(C.sound_level[0])
        self.pre_shoot_time = timer
        if self.direction == 'up':
            self.bullet = bullet.bullet(self.rect.x+self.rect.width/2-5,self.rect.y-20,'up',1)
        if self.direction == 'down':
            self.bullet = bullet.bullet(self.rect.x+self.rect.width/2-5,self.rect.y+self.rect.height,'down',1)
        if self.direction == 'left':
            self.bullet = bullet.bullet(self.rect.x,self.rect.y+self.rect.height/4,'left',1)
        if self.direction == 'right':
            self.bullet = bullet.bullet(self.rect.x+self.rect.width,self.rect.y+self.rect.height/4,'right',1)
        self.sprite_bullet.add(self.bullet)
        # print(self.bullet.rect.x,self.bullet.rect.y)

    def load_image(self):
        # 加载图片
        main_image = T.GRAGHIES['tank_gray']
        dead_main_image = T.GRAGHIES['explode']
        relive_main_image=T.GRAGHIES['relive']
        # 坦克本体的缩放倍数
        self.tank_scale = 2*C.SCALE
        __scale = self.tank_scale
        # 死亡图像缩放倍数
        scale2 = 0.25*C.SCALE
        # 复活图像缩放倍数
        scale3 = 0.73*C.SCALE
        # 存储各种状态下的图片
        self.down_image = [T.get_image(main_image,0,0,32,32,__scale),T.get_image(main_image,32,0,32,32,__scale),T.get_image(main_image,64,0,32,32,__scale),T.get_image(main_image,96,0,32,32,__scale)]
        self.left_image = [T.get_image(main_image,0,32,32,32,__scale),T.get_image(main_image,32,32,32,32,__scale),T.get_image(main_image,64,32,32,32,__scale),T.get_image(main_image,96,32,32,32,__scale)]
        self.right_image= [T.get_image(main_image,0,64,32,32,__scale),T.get_image(main_image,32,64,32,32,__scale),T.get_image(main_image,64,64,32,32,__scale),T.get_image(main_image,96,64,32,32,__scale)]
        self.up_image  =  [T.get_image(main_image,0,96,32,32,__scale),T.get_image(main_image,32,96,32,32,__scale),T.get_image(main_image,64,96,32,32,__scale),T.get_image(main_image,96,96,32,32,__scale)]
        # 死亡
        self.dead_image=  [T.get_image(dead_main_image,703,363,350,350,scale2),T.get_image(dead_main_image,352,363,350,350,scale2),
                           T.get_image(dead_main_image,24,363,350,350,scale2),T.get_image(dead_main_image,669,27,350,350,scale2),
                           T.get_image(dead_main_image,339,27,350,350,scale2),T.get_image(dead_main_image,0,27,350,350,scale2)]
        # 复活
        self.relive_image=[T.get_image(relive_main_image,10,0,88,88,scale3),T.get_image(relive_main_image,111,0,88,88,scale3),
                           T.get_image(relive_main_image,317,0,88,88,scale3),T.get_image(relive_main_image,108,101,88,88,scale3),
                           T.get_image(relive_main_image,212,105,88,88,scale3)]

    # rollback到上一个帧的位置
    def rollback(self):
        self.rect.x = self.old_x
        self.rect.y = self.old_y

    def update(self,keys,sprite_bullet,surface):
        # 设置自身子弹所属精灵组
        self.sprite_bullet = sprite_bullet
        # 判断坦克是否死亡
        if self.dead == True:
            self.index_dead += 1
            self.godead(self.index_dead)
            return 0
        else:
            self.index_dead = -1

        # 判断坦克是否处于复活状态
        if self.relive == True:
            self.index_relive += 1
            self.go_relive(self.index_relive)
            return 0
        else:
            self.index_relive = -1

        # 绘制头顶的名字
        surface.blit(self.name_image,(self.rect.x+6,self.rect.y-20))


        # 旧坐标，用来撤回
        self.old_x = self.rect.x
        self.old_y = self.rect.y

        # 第一个玩家
        if self.role == 1:
            if keys[pygame.K_d]:
                self.move_right(self.index_now)
            elif keys[pygame.K_w]:
                self.move_up(self.index_now)
            elif keys[pygame.K_s] :
                self.move_down(self.index_now)
            elif keys[pygame.K_a] :
                self.move_left(self.index_now)
            # elif keys[pygame.K_x]:
            #     self.dead = True
            # 按j发射子弹
            if keys[pygame.K_SPACE]:
                self.bullet_exist = True
                self.shoot()
            # index_now ++
            self.index_now +=1
            if self.index_now > 10000:
                self.index_now%=2

        # 第二个玩家
        else:
            if keys[pygame.K_RIGHT]:
                self.move_right(self.index_now)
            elif keys[pygame.K_UP]:
                self.move_up(self.index_now)
            elif keys[pygame.K_DOWN]:
                self.move_down(self.index_now)
            elif keys[pygame.K_LEFT]:
                self.move_left(self.index_now)
            # elif keys[pygame.K_c]:
            #     self.dead = True
            self.index_now += 1
            if self.index_now > 10000:
                self.index_now %= 2

        # 边界判断
        if self.rect.left > C.SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = C.SCREEN_WIDTH
        if self.rect.top > C.SCREEN_HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = C.SCREEN_HEIGHT

    def get_injured(self):
        # 复活和死亡期间不能受伤
        if self.dead == True or self.relive == True:
            return 0
        self.dead_bgm.play()
        self.dead_bgm.set_volume(C.sound_level[0])
        self.dead = True
        C.now_my_tank_life -= 1

    # 移动
    def move_up(self,index):
        self.direction = 'up'
        self.image = self.up_image[index%4]
        self.rect.y -= self.speed
    def move_down(self,index):
        self.direction = 'down'
        self.image = self.down_image[index%4]
        self.rect.y += self.speed
    def move_left(self,index):
        self.direction = 'left'
        self.image = self.left_image[index%4]
        self.rect.x -= self.speed
    def move_right(self,index):
        self.direction = 'right'
        self.image = self.right_image[index%4]
        self.rect.x += self.speed

    # 死亡
    def godead(self,index):
        index/=5
        index = int(index)
        if(index == 6):
            self.dead = False
            self.relive = True
            self.rect.x = self.relive_position_x
            self.rect.y = self.relive_position_y
        else:
            self.image = self.dead_image[index%6]

    # 复活
    def go_relive(self,index):
        index/=6
        index = int(index)
        if(index == 5):
            self.relive = False
            self.image = self.up_image[0]
        else:
            self.image = self.relive_image[index%5]