# -*- coding = utf-8 -*-
# @Time : 2021/10/21 11:50
# @Author : qiuxinhan
# @File : constants.py
# @Software : PyCharm
# 基本属性
# 屏幕的高和宽
SCREEN_WIDTH,SCREEN_HEIGHT = 1200,720
# 帧率
FPS = 55

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ONE_OR_TWO = 1

# 坦克速度
SPEED_HIGH = 3
SPEED_MID = 2
SPEED_LOW = 1
YOUR_SPEED = 2

# 倍数
SCALE = 0.70
WALL_SCALE = 0.75
# 关卡信息
MY_TANK_LIFE = 3
ENEMY_TANK_LIFE = 20
now_enemy_tank_life = 20
now_my_tank_life = 20

# 音效
bang_sound = None
fire_sound = None
start_sound = None
blast_sound = None
add_sound = None
Gunfire_sound = None
hit_sound = None

# 音量
sound_level = [0.5,0,0.1,0.5,1]
sound_state = 3
# 难度
level_state = 2
light_num = 7
mid_num1 = 5
mid_num2 = 5
speed_low_array = [0,0.5,1,2]
speed_mid_array = [0,1,2,3]
speed_high_array = [0,2,3,5]
light_num_array = [0,8,7,5]
mid_num1_array = [0,6,5,4]
mid_num2_array = [0,5,5,4]

# 上一局游戏进行时长
LAST_PLAY_TIME = 0
