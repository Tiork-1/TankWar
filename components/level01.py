# -*- coding = utf-8 -*-
# @Time : 2021/10/21 14:46
# @Author : qiuxinhan
# @File : level01.py
# @Software : PyCharm
import pygame.transform

import constants
import constants as C
import tools
from components import myTank,walls,enermyTank

class Level01():
    def __init__(self):
        self.myinit()
    def test(self):
        print("hello Test!")

    def myinit(self):
        # 游戏状态
        self.finished = False
        self.next = None
        # 游戏是否结束，赢了是一，输了是-1，未结束是0
        self.win = 0
        # 设置坦克的生命值
        C.now_enemy_tank_life = C.ENEMY_TANK_LIFE
        C.now_my_tank_life = C.MY_TANK_LIFE
        # 背景图片
        self.backgroundImage = tools.GRAGHIES['level1_background']
        self.backgroundRect = self.backgroundImage.get_rect()
        self.backgroundImage = pygame.transform.scale(self.backgroundImage,(C.SCREEN_WIDTH,C.SCREEN_HEIGHT))

        # 创建精灵组
        # 总的坦克
        self.sprite_all_tank = pygame.sprite.Group()
        # 三种坦克
        self.sprite_my_tank = pygame.sprite.Group()
        self.sprite_enemy_tank = pygame.sprite.Group()
        self.sprite_frinend_tank = pygame.sprite.Group()
        # 三种墙
        self.sprite_brick_wall = pygame.sprite.Group()
        self.sprite_stone_wall = pygame.sprite.Group()
        self.sprite_grass_wall = pygame.sprite.Group()
        # 基地和基地保护墙单独拿出来，防止自己人误伤
        self.sprite_home = pygame.sprite.Group()
        # 子弹
        self.sprite_bullet=pygame.sprite.Group()

        # 在这里面添加精灵
        self.create_sprites()


    def create_sprites(self):
        # 我方坦克
        self.tank1 = myTank.Player(672,624,5)
        # 添加进精灵组
        self.sprite_my_tank.add(self.tank1)
        self.sprite_all_tank.add(self.tank1)

        # 敌方坦克
        self.e_tank1 = enermyTank.EnemyTank(48,96,1,C.light_num,0)
        self.sprite_all_tank.add(self.e_tank1)
        self.sprite_enemy_tank.add(self.e_tank1)
        self.e_tank2 = enermyTank.EnemyTank(384,96,2,C.mid_num1,0)
        self.sprite_all_tank.add(self.e_tank2)
        self.sprite_enemy_tank.add(self.e_tank2)
        self.e_tank3 = enermyTank.EnemyTank(768,96,3,C.mid_num2,0)
        self.sprite_all_tank.add(self.e_tank3)
        self.sprite_enemy_tank.add(self.e_tank3)
        self.e_tank4 = enermyTank.EnemyTank(1104,96,2,C.ENEMY_TANK_LIFE-C.mid_num1-C.mid_num2-C.light_num,0)
        self.sprite_all_tank.add(self.e_tank4)
        self.sprite_enemy_tank.add(self.e_tank4)
        # 如果是双人模式就创建一个友方坦克
        if C.ONE_OR_TWO == 2:
            self.friend_tank = enermyTank.EnemyTank(480, 624, 2, 5, 1)
            self.sprite_my_tank.add(self.friend_tank)
            self.sprite_all_tank.add(self.friend_tank)


        # 墙
        self.create_wall()

        # 基地精灵
        self.home = pygame.sprite.Sprite()
        self.home.image = tools.GRAGHIES['home']
        scale = 1
        self.home.image = pygame.transform.scale(self.home.image,(48,48))
        self.home.rect = self.home.image.get_rect()
        self.home.rect.x = 576
        self.home.rect.y = 624


    def update(self,keys,surface):
        # 判断游戏是否应该结束
        if C.now_my_tank_life <= 0:
            self.win = -1
        if C.now_enemy_tank_life <= 0:
            self.win = 1


        # 判断游戏是否结束
        if self.win != 0:
            if self.win == -1:
                self.finished = True
                self.next = 'gameOver'
            else:
                self.finished = True
                self.next = 'success'


        self.collision_test()


        self.update_stuffs(surface)
        self.update_tanks(surface,keys)
        self.update_bullet(surface)
        self.update_walls(surface)



    def update_stuffs(self,surface):
        surface.fill(C.BLACK)
        surface.blit(self.home.image,self.home.rect)
        # surface.blit(self.backgroundImage,(0,0))
        font = pygame.font.SysFont('FixedSys.ttf',66,True)
        score_string = '  YOUR LIFE : '+str(C.now_my_tank_life) + '                 ENEMY LIFE : '+str(C.now_enemy_tank_life)
        score_image = font.render(score_string,1,(128,42,42))
        score_rect = score_image.get_rect()
        surface.blit(score_image,(10,5))

        # # 设置字体贴图
        # font = pygame.font.SysFont('FixedSys.ttf',46,True)
        # label_image = font.render('S E T T I N G',1,(128,42,42))
        # settingRect = label_image.get_rect()
        # label_image = pygame.transform.scale(label_image,(int(settingRect.width*1.25),
        #                                                   int(settingRect.height * 1.25)))

    def update_tanks(self,surface,keys):
        # 坦克精灵绘制和更新
        self.sprite_all_tank.draw(surface)
        self.sprite_all_tank.update(keys,self.sprite_bullet)




    def update_walls(self,surface):
        # 精灵组绘制
        # 砖块
        self.sprite_brick_wall.draw(surface)
        self.sprite_brick_wall.update()
        # 石头
        self.sprite_stone_wall.draw(surface)
        self.sprite_stone_wall.update()
        # 艹地
        self.sprite_grass_wall.draw(surface)
        self.sprite_grass_wall.update()

    def update_bullet(self,surface):
        self.sprite_bullet.draw(surface)
        self.sprite_bullet.update()


    def collision_test(self):

        # 所有坦克和石头
        collision2 = pygame.sprite.groupcollide(self.sprite_all_tank,self.sprite_stone_wall,False,False)

        for key in collision2.keys():
            key.rollback()
            items = collision2.get(key)

        # 所有坦克和砖块
        collision2 = pygame.sprite.groupcollide(self.sprite_all_tank,self.sprite_brick_wall,False,False)

        for key in collision2.keys():
            key.rollback()
            items = collision2.get(key)

        # 子弹和砖头
        collision3 = pygame.sprite.groupcollide(self.sprite_bullet,self.sprite_brick_wall,False,False)

        for key in collision3:
            key.disapear(self.sprite_bullet)
            items = collision3.get(key)
            for item in items:
                if key.camp == 1 and item.is_home == True:
                    pass
                else:
                    item.disapear(self.sprite_brick_wall)

        # 子弹和石头
        collision3 = pygame.sprite.groupcollide(self.sprite_bullet,self.sprite_stone_wall,False,False)

        for key in collision3:
            key.disapear(self.sprite_bullet)

        #所有坦克之间的碰撞,不管什么坦克，相互碰撞会停止
        for item1 in self.sprite_all_tank:
            for item2 in self.sprite_all_tank:
                if pygame.sprite.collide_rect(item1,item2):
                    if item1 != item2:
                        item1.rollback()
                        item2.rollback()

        # 子弹之间的碰撞,不同阵营的子弹会相互碰撞，碰撞会消失
        for item1 in self.sprite_bullet:
            for item2 in self.sprite_bullet:
                if pygame.sprite.collide_rect(item1,item2):
                    if item1 != item2:
                        if item1.camp != item2.camp:
                            item1.disapear(self.sprite_bullet)
                            item2.disapear(self.sprite_bullet)

        # 我方子弹和敌方坦克
        collision4 = pygame.sprite.groupcollide(self.sprite_enemy_tank,self.sprite_bullet,False,False)

        for key in collision4.keys():
            # 坦克受伤
            for item in collision4.get(key):
                if item.camp == 1:
                    key.get_injured()
                    # 子弹消失
                    item.disapear(self.sprite_bullet)
                    break

        # 敌方子弹和我的坦克
        collision5 = pygame.sprite.groupcollide(self.sprite_my_tank,self.sprite_bullet,False,False)

        for key in collision5:
            for item in collision5.get(key):
                if item.camp != 1:
                    key.get_injured()
                    # 子弹消失
                    item.disapear(self.sprite_bullet)
                    break

        # 敌方子弹和我方基地
        collision6 = pygame.sprite.spritecollide(self.home,self.sprite_bullet,False)

        if len(collision6)!=0:
            for item in collision6:
                if item.camp!=1:
                    print("GAME OVER")
                    self.win = -1
                    item.disapear(self.sprite_bullet)

    def create_wall(self):
        pass
        # 创造边界
        for i in range(25):
            for j in range(14):
                if i==0 or i==24 or j==0 or j==13:
                    wall = walls.Wall(2,i*48,(j+1)*48,False)
                    self.sprite_stone_wall.add(wall)

        # 创建边界内的地图
        self.map_number = [
            [0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
            [3,3,3,2,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,2,3,3,3],
            [3,3,3,2,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,2,3,3,3],
            [0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,0,0],
            [3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,1,1,3,3,3,0,0],
            [3,3,3,2,0,0,0,2,0,0,0,0,0,0,0,0,1,1,3,3,3,0,0],
            [3,3,3,2,0,2,0,2,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0],
            [0,0,0,2,0,0,0,2,0,0,1,1,1,0,0,0,0,0,3,3,3,0,0],
            [0,0,0,0,0,0,0,2,0,0,1,0,1,0,0,0,0,0,2,0,0,0,0]
        ]
        bx = 48
        by = 96
        for i in range(12):
            for j in range(23):
                if self.map_number[i][j]==1:
                    if j>=10 and j<=12 and i>=10 and i<=11:
                        wall = walls.Wall(1,j*48+bx,i*48+by,True)
                        self.sprite_brick_wall.add(wall)
                    else:
                        wall = walls.Wall(1,j*48+bx,i*48+by,False)
                        self.sprite_brick_wall.add(wall)

                elif self.map_number[i][j]==2:
                    wall = walls.Wall(2,j*48+bx,i*48+by,False)
                    self.sprite_stone_wall.add(wall)
                elif self.map_number[i][j]==3:
                    wall = walls.Wall(3,j*48+bx,i*48+by,False)
                    self.sprite_grass_wall.add(wall)
