'''
■ 미션
  - 산타와 썰매의 이동을 조금 더 다이내믹하게 해 주세요.
  - 눈이 내리는 멋진 배경을 추가해 주세요. 
  - Charitmas 네온사인 글자가 화면에 나타나게 해 주세요. 

■ 라이센스
we-wish-you-a-merry-christmas-126685.mp3 라이센스
- https://pixabay.com/music/search/genre/christmas/
'''

import pygame as pg
import time, random 

Width = 800
Height = 600

pg.init()
pg.display.set_caption("크리스마스게임")
Screen = pg.display.set_mode( (Width, Height))

Bg = pg.image.load("res/크리스마스세트배경.png")  # lec/res/player.png
Player = pg.image.load("res/산타와썰매.png")    # 500x128
# FireSnd = pg.mixer.Sound("res/레이저소리.mp3")
pg.mixer.music.load("res/we-wish-you-a-merry-christmas-126685.mp3")
pg.mixer.music.play(-1)

Px = -128
Py = 200
Spd = 2

Running = True
# 게임의 메인루프
while Running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Running = False
    
    # 배경 그리기
    Screen.blit(Bg, (0, 0))

    # 산타 그리기 
    Screen.blit(Player, (Px, Py))

    # 오브젝트 재계산
    Px += Spd 
    if Px > Width:
        Px = -128
    
    pg.display.update()
    time.sleep(0.03)
    # Count += 1
pg.quit()



