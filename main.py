import pygame
import sys
import constants as C
import os
import tools
from components import mainMenu,setting,level01,game_over,success
def main():
    # 初始化
    pygame.init()
    # bgm初始化
    pygame.mixer.init()
    # 加载音效
    # 重型
    C.bang_sound = pygame.mixer.Sound(r"resource\bgm\bang.wav")
    # 轻
    C.fire_sound = pygame.mixer.Sound(r"resource\bgm\Gunfire.wav")
    C.start_sound = pygame.mixer.Sound(r"resource\bgm\start.wav")
    # 坦克摧毁
    C.blast_sound = pygame.mixer.Sound(r"resource\bgm\blast.wav")
    # 通用声效
    C.add_sound = pygame.mixer.Sound(r"resource\bgm\add.wav")
    # 中枪击声
    C.Gunfire_sound = pygame.mixer.Sound(r"resource\bgm\Gunfire.wav")
    # 中型
    C.hit_sound = pygame.mixer.Sound(r"resource\bgm\hit.wav")

    pygame.display.set_caption("坦克大战")
    # 定义屏幕
    screen = pygame.display.set_mode((C.SCREEN_WIDTH,C.SCREEN_HEIGHT))
    # 加载所有图片
    tools.GRAGHIES = tools.load_graghics('resource/images')
    # 定义时钟
    clock = pygame.time.Clock()
    # 加载所有图片进入字典

    # 状态的字典
    state_dict = {
        'mainMenu':mainMenu.MainMenu(),
        'setting' :setting.Setting(),
        'level01' :level01.Level01(),
        'gameOver':game_over.GameOver(),
        'success':success.Success()
    }
    # 将默认状态设置为主菜单
    now_state = state_dict['mainMenu']

    running = True
    while running == True:

        # 设置游戏帧率
        clock.tick(C.FPS)

        # 如果当前状态结束，则切换自下一状态
        if now_state.finished == True:
            now_state = state_dict[now_state.next]
            now_state.myinit()
            # 设置当前为未结束状态
            now_state.finished = False

        #获取键盘监听
        keys = pygame.key.get_pressed()

        now_state.update(keys,screen)
        pygame.display.flip()
        # 按下右上角退出游戏
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()







