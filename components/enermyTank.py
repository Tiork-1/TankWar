# -*- coding = utf-8 -*-
# @Time : 2021/10/21 14:46
# @Author : qiuxinhan
# @File : enermyTank.py
# @Software : PyCharm
import random

import pygame.sprite
from components import bullet
import tools as T
import constants as C

class EnemyTank(pygame.sprite.Sprite):
    # 前两个参数是开始默认坐标，也是复活坐标
    def __init__(self,_x,_y,_type,_life,_camp):
        # 先初始化精灵类
        pygame.sprite.Sprite.__init__(self)
        # 设置阵营
        self.camp = _camp
        # 设置生命数，也就是复活次数
        self.life = _life
        # 音效
        self.bgm = None
        self.dead_bgm = C.blast_sound
        if _type == 1:
            self.bgm = C.fire_sound
        elif _type == 2:
            self.bgm = C.Gunfire_sound
        elif _type == 3:
            self.bgm = C.bang_sound
        # 设置复活地点
        self.relive_position_x = _x
        self.relive_position_y = _y
        # 先设置坦克的类型
        self.type = _type
        # 加载坦克该类型下的贴图
        self.load_image()
        self.index_now = 0
        # 处理死亡复活的参数
        self.pre_get_injured = 0
        self.dead = False
        self.relive = False
        self.index_dead = -1
        self.index_relive = -1
        # 设置精灵的默认图像
        if _type==1:
            self.image = self.up_image[0]
        if _type==2:
            self.image = self.up_image[0]
        if _type==3:
            self.image = self.up_image[0]

        # rect代表的是这一个图形的矩形区域，同时也代表着这一个精灵的区域
        self.rect = self.image.get_rect()
        self.rect.x = _x
        self.rect.y = _y

        # 其他参数
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        self.knock_on_wall = False
        self.go_state = 'none'
        # 坦克的方向
        self.direction = 'up'
        # 子弹是否存活和子弹是否存在
        self.bullet_exist = False
        self.bullet = None
        # 设置速度,和血量
        if self.type == 1:
            self.speed = C.SPEED_HIGH
            self.blood = 1
        elif self.type == 2:
            self.speed = C.SPEED_MID
            self.blood = 2
        elif self.type == 3:
            self.speed = C.SPEED_LOW
            self.blood = 3
        if _camp==1:
            self.speed = C.YOUR_SPEED

    def shoot(self):
        if self.bullet != None and self.bullet.dead != True:
            return 0
        self.bgm.play()
        self.bgm.set_volume(C.sound_level[0])
        if self.direction == 'up':
            self.bullet = bullet.bullet(self.rect.x+self.rect.width/2-5,self.rect.y-20,'up',self.camp)
        if self.direction == 'down':
            self.bullet = bullet.bullet(self.rect.x+self.rect.width/2-5,self.rect.y+self.rect.height,'down',self.camp)
        if self.direction == 'left':
            self.bullet = bullet.bullet(self.rect.x,self.rect.y+self.rect.height/4,'left',self.camp)
        if self.direction == 'right':
            self.bullet = bullet.bullet(self.rect.x+self.rect.width,self.rect.y+self.rect.height/4,'right',self.camp)
        self.sprite_bullet.add(self.bullet)
        # print(self.bullet.rect.x,self.bullet.rect.y)


    def get_injured(self):
        # 设置两次受到伤害的时延，防止连续受到多次伤害
        timer = pygame.time.get_ticks()
        if timer-self.pre_get_injured < 500:
            return 0
        self.pre_get_injured = timer
        self.blood -= 1
        if self.blood <= 0:
            # 血量为零，生命值减一
            self.dead_bgm.play()
            self.dead_bgm.set_volume(C.sound_level[0])
            self.life -= 1
            C.now_enemy_tank_life -= 1
            self.dead = True
            # 将血量恢复成最初的样子
            self.blood = self.type

    def load_image(self):
        # 加载图片
        main_image1 = T.GRAGHIES['enemy_tank1']
        main_image2 = T.GRAGHIES['enemy_tank2']
        main_image3 = T.GRAGHIES['enemy_tank3']
        # 死亡
        dead_main_image = T.GRAGHIES['explode']
        # 复活
        relive_main_image=T.GRAGHIES['relive']
        # 坦克本体的缩放倍数
        self.tank_scale = 2*C.SCALE
        __scale = self.tank_scale
        # 死亡图像缩放倍数
        scale2 = 0.25*C.SCALE
        # 复活图像缩放倍数
        scale3 = 0.73*C.SCALE
        # 设置坦克图片的四个集合
        self.up_image = None
        self.left_image = None
        self.right_image = None
        self.down_image = None
        # 第一种
        if self.type==1:
            self.up_image = [T.get_image(main_image1,0,96,32,32,__scale),T.get_image(main_image1,32,96,32,32,__scale)]
            self.down_image = [T.get_image(main_image1,0,0,32,32,__scale),T.get_image(main_image1,32,0,32,32,__scale)]
            self.left_image = [T.get_image(main_image1,0,32,32,32,__scale),T.get_image(main_image1,32,32,32,32,__scale)]
            self.right_image = [T.get_image(main_image1,0,64,32,32,__scale),T.get_image(main_image1,32,64,32,32,__scale)]
        # 第二种
        elif self.type==2:
            self.up_image = [T.get_image(main_image2,0,96,32,32,__scale),T.get_image(main_image2,32,96,32,32,__scale)]
            self.down_image = [T.get_image(main_image2,0,0,32,32,__scale),T.get_image(main_image2,32,0,32,32,__scale)]
            self.left_image = [T.get_image(main_image2,0,32,32,32,__scale),T.get_image(main_image2,32,32,32,32,__scale)]
            self.right_image = [T.get_image(main_image2,0,64,32,32,__scale),T.get_image(main_image2,32,64,32,32,__scale)]
        # 第三种
        else:
            self.up_image = [T.get_image(main_image3,0,96,32,32,__scale),T.get_image(main_image3,32,96,32,32,__scale)]
            self.down_image = [T.get_image(main_image3,0,0,32,32,__scale),T.get_image(main_image3,32,0,32,32,__scale)]
            self.left_image = [T.get_image(main_image3,0,32,32,32,__scale),T.get_image(main_image3,32,32,32,32,__scale)]
            self.right_image = [T.get_image(main_image3,0,64,32,32,__scale),T.get_image(main_image3,32,64,32,32,__scale)]

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
        self.knock_on_wall = True
        self.rect.x = self.old_x
        self.rect.y = self.old_y

    def update(self,keys,sprite_bullet):
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


        # 旧坐标，用来撤回
        self.old_x = self.rect.x
        self.old_y = self.rect.y

        # 决策
        choose = self.choose_direction()
        if choose == 'up':
            self.index_now += 1
            self.move_up(self.index_now)
        elif choose == 'down':
            self.index_now += 1
            self.move_down(self.index_now)
        elif choose == 'left':
            self.index_now += 1
            self.move_left(self.index_now)
        elif choose == 'right':
            self.index_now += 1
            self.move_right(self.index_now)
        elif choose == 'shoot':
            self.shoot()
        if self.index_now > 1000:
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



    # 移动
    def move_up(self,index):
        index/=2
        index = int(index)
        self.direction = 'up'
        self.image = self.up_image[index%2]
        self.rect.y -= self.speed
    def move_down(self,index):
        index/=2
        index = int(index)
        self.direction = 'down'
        self.image = self.down_image[index%2]
        self.rect.y += self.speed
    def move_left(self,index):
        index/=2
        index = int(index)
        self.direction = 'left'
        self.image = self.left_image[index%2]
        self.rect.x -= self.speed
    def move_right(self,index):
        index/=2
        index = int(index)
        self.direction = 'right'
        self.image = self.right_image[index%2]
        self.rect.x += self.speed

    # 死亡
    def godead(self,index):
        index/=5
        index = int(index)
        if(index == 6):
            self.dead = False
            self.rect.x = self.relive_position_x
            self.rect.y = self.relive_position_y
            if self.life > 0:
                self.relive = True
            else:
                self.kill()
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

    def choose_direction(self):
        #撞墙之后采取的决策
        if self.knock_on_wall == True:
            self.knock_on_wall = False
            rd = random.randint(0,4)
            if rd == 1:
                self.go_state='left'
                return 'left'
            elif rd == 2:
                self.go_state='right'
                return 'right'
            elif rd == 3:
                self.go_state='up'
                return 'up'
            elif rd == 4:
                self.go_state = 'down'
                return 'down'
            elif rd == 3:
                return 'shoot'
        # 没有撞墙
        rd = random.randint(1,300)
        if rd == 1:
            self.go_state = 'up'
            return 'up'
        elif rd == 2:
            self.go_state = 'down'
            return 'down'
        elif rd == 3:
            self.go_state = 'left'
            return 'left'
        elif rd == 4:
            self.go_state = 'right'
            return 'right'
        if rd > 10 and rd < 16:
            return 'shoot'

        return self.go_state