# -*- coding = utf-8 -*-
# @Time : 2021/10/21 18:15
# @Author : qiuxinhan
# @File : tools.py
# @Software : PyCharm
# tool
import pygame
import os

# 1.获得一张图片里面的子图片
def get_image(sheet,x,y,width,height,scale):
    image = pygame.Surface((width,height))
    image.blit(sheet,(0,0),(x,y,width,height)) # 0,0代表画到哪里，剩下四个代表画那一部分图片
    image = pygame.transform.scale(image,(int(width*scale),int(height*scale))) # 放缩图片
    return image


# 2.加载所有的图片
# 将指定路径的图片放到字典里返回
def load_graghics(path,accept=('.jpg','.png','.bmp','.gif')):
    graghics = {}
    for pic in os.listdir(path):
        name,ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path,pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graghics[name] = img
    return graghics

def stop(time_seg):
    time_start = pygame.time.get_ticks()
    while(True):
        time_now = pygame.time.get_ticks()
        if time_now - time_start > time_seg:
            break

# 存放所有图片的字典
GRAGHIES = None