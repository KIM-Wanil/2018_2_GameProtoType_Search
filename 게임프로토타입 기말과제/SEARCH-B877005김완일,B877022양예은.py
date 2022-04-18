#완성
#SEARCH
#B877005 김완일 B877022 양예은
import pygame,sys,time,random
from pygame.locals import *
#from PIL import Image
pygame.init()

gameover1Sound=pygame.mixer.Sound('gameover1.wav')
jumpSound=pygame.mixer.Sound('jump.wav')
jumpSound.set_volume(10.0)
#gameover2Sound=pygame.mixer.Sound('gameover2.wav')                       
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

displayWidth=600
displayHeight=400
screen = pygame.display.set_mode((displayWidth,displayHeight))
screen.fill((255,255,255))

title=pygame.image.load("title.png")
explainScreen=pygame.image.load("explain_screen.png")
shopScreen=pygame.image.load("shop_screen.png")

startButton = pygame.image.load("start_button.png")
startButtonOver = pygame.image.load("start_button_over.png")
tutorialButton = pygame.image.load("tutorial_button.png")
tutorialButtonOver = pygame.image.load("tutorial_button_over.png")
shopButton = pygame.image.load("shop_button.png")
shopButtonOver = pygame.image.load("shop_button_over.png")
reButton=pygame.image.load("re_button.png")
reButtonOver=pygame.image.load("re_button_over.png")
backButton=pygame.image.load("back_button.png")
backButtonOver=pygame.image.load("back_button_over.png")
mainButton=pygame.image.load("main_button.png")
mainButtonOver=pygame.image.load("main_button_over.png")
choiceButton=pygame.image.load("choice_button.png")
choiceButtonOver=pygame.image.load("choice_button_over.png")

mainBackgroundImage=pygame.image.load("main_background.jpg") 

characterImage=pygame.image.load("character.png")
fishImage=pygame.image.load("fish.png")
glacierImage=pygame.image.load("glacier.png")
brokenGlacierImage=pygame.image.load("broken_glacier.png")
mainBackgroundImage=pygame.image.load("main_background.jpg")


score=0
coin=0

x=0
y=0
sf=pygame.font.SysFont("Times", 24)
se=pygame.font.SysFont("Times", 30)
text=sf.render("Points: " + str(score), True, (0,0,0))
gameOverText=sf.render("GameOver" ,True, (0,0,0))
IMAGE=2
begin=False
onExplain=False
chWidth=66
chHeight=110
fHeight=60
character={'rect':pygame.Rect((displayWidth-chWidth)/2,displayHeight-chHeight, chWidth,chHeight),'color':(0,255,0),'dir':1}
rect0={'rect':pygame.Rect(180,displayHeight-fHeight, 60,fHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'1-1','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect1={'rect':pygame.Rect(0,displayHeight-fHeight, 60,fHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'1-2','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect2={'rect':pygame.Rect(0,displayHeight-fHeight*2, 60,fHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'1-3','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}

rect3={'rect':pygame.Rect(0,displayHeight-fHeight*2, 60,fHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'2-1','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect4={'rect':pygame.Rect(0,displayHeight-fHeight*3, 60,fHeight),'color' :(255,0,0),'dir':1,'speed':None,'num':'2-2','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect5={'rect':pygame.Rect(0,displayHeight-fHeight*3, 60,fHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'2-3','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}

rect6={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'3-1','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect7={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'3-2','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect8={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'3-3','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}

rect9={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'4-1','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect10={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'4-2','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect11={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'4-3','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}

rect12={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'5-1','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect13={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'5-2','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect14={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':0,'speed':None,'num':'5-3','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}

rect15={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'6-1','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect16={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'6-2','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}
rect17={'rect':pygame.Rect(0,displayHeight-fHeight*4, 60,fHeight),'color':(255,0,0),'dir':1,'speed':None,'num':'6-3','broken':None,'FISH':{'fish':None,'rect':pygame.Rect(0,0,40,23),'color':(0,200,200)}}


l1_rects=[rect0,rect1,rect2]
l2_rects=[rect3,rect4,rect5]
l3_rects=[rect6,rect7,rect8]
l4_rects=[rect9,rect10,rect11]
l5_rects=[rect12,rect13,rect14]
l6_rects=[rect15,rect16,rect17]
rects=[l1_rects,l2_rects,l3_rects,l4_rects,l5_rects,l6_rects]
def skin_gold():
    global characterImage
    characterImage=pygame.image.load("character_gold.png")
def skin_muffler():
    global characterImage
    characterImage=pygame.image.load("character_muffler.png")
def skin_basic():
    global characterImage
    characterImage=pygame.image.load("character.png")
#버튼 만드는 함수!
button_down = False
def button( x,y,w,h,picture,pictureOver,action=None,actionArgs=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global buttonDown
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        screen.blit(pictureOver ,  ( x,y))
        if click[0] == 1 and not buttonDown and action!= None:

            if actionArgs is not None:
                action(*actionArgs)
            else:
                action()

            buttonDown = True

        elif click[0] == 0:
            buttonDown = False
    else:
        screen.blit(picture,  ( x,y))
#땅,캐릭터와 점수판을 그리는 함수
def draw_screen():
    global glacierImage,brokenGlacierImage
    CHARIMAGE=characterImage#global characterImage를 사용해서 이미지 자체를 반복적으로 늘렸다 줄였다 하니까 그림이 깨져버림 ->지역변수로 복사해서 사용
    GLACIERIMAGE=glacierImage
    B_GLCIERIMAGE=brokenGlacierImage
    screen.fill((11,99,180))
    #screen.blit(backgroundImage,(0,0)) #->이미지를 배경으로 했을 때 렉이 심해짐..
    for l_rects in rects:
        for r in l_rects:
            #pygame.draw.rect(screen, r['color'], r['rect']) 
            if r['broken']==False:
                GLACIERIMAGE=pygame.transform.smoothscale(GLACIERIMAGE,(r['rect'].width,r['rect'].height))
                screen.blit( GLACIERIMAGE,(r['rect'].x,r['rect'].y))
            elif r['broken']==True:
                B_GLCIERIMAGE=pygame.transform.smoothscale(B_GLCIERIMAGE,(r['rect'].width,r['rect'].height))
                screen.blit( B_GLCIERIMAGE,(r['rect'].x,r['rect'].y))
            if r['FISH']['fish']==True:
                #pygame.draw.rect(screen, r['FISH']['color'], r['FISH']['rect'])
                screen.blit( fishImage,(r['FISH']['rect'].x,r['FISH']['rect'].y))
    #pygame.draw.rect(screen, (0,0,0), character['rect'])
    CHARIMAGE=pygame.transform.smoothscale(CHARIMAGE,(character['rect'].width,character['rect'].height))
    screen.blit( CHARIMAGE,(character['rect'].x,character['rect'].y))
    draw_text()
    return
def draw_text():
    global coin
    scoreText=sf.render("SCORE: " + str(score), True, (0,0,0))
    screen.blit(scoreText,(10,10))
    coinText=sf.render("COIN: " + str(coin), True, (0,0,0))
    screen.blit(coinText,(10,30)) 
    return
def gameover_screen():
    #screen.blit(gameOverText,(160,200))
    
    text = sf.render("GAME OVER", True, BLACK)
    text_rect = text.get_rect( )
    text_rect.centerx = screen.get_rect( ).centerx
    text_rect.y = screen.get_rect( ).centery-100
    screen.blit(text, text_rect)
#스페이스바 눌렀을 때 배경이 아래로 내려가고 캐릭터가 점프하는 애니메이션 실행 함수
def jump():
    global characterImage
    pygame.mixer.Sound.play(jumpSound)
    for i in range (0,20):
        #밟고 있는 땅과 밟을 땅을 제외한 모든 땅 한칸 아래로
        for l_rects in rects:
            for r in l_rects:
                r['rect'].top += fHeight/20
                r['FISH']['rect'].top += fHeight/20
                #if r['dir']==0 and r!=rects[0] and r!=rects[1]:
                r['rect'].right += r['speed']
                r['FISH']['rect'].right += r['speed']                       
        #캐릭터 크기와 위치를 늘렸다 줄여서 점프하는 것처럼 보이게!
        if i<10:
            character['rect'].left-=1
            character['rect'].width+=2
            character['rect'].top-=4
            character['rect'].height+=2
        else:
            character['rect'].left+=1
            character['rect'].width-=2
            character['rect'].top+=4
            character['rect'].height-=2
        draw_screen()
        #characterImage=pygame.transform.scale(characterImage,(character['rect'].width,character['rect'].height))
        time.sleep(0.01)
        pygame.display.update()
    return

#설명창 띄우는 함수
def on_explain_screen():
    while True:
        #button(150,500,100,50,explainButton,explainButtonOver,on_explain_screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(explainScreen,  ( 0,0))
        button(displayWidth-100,displayHeight-100,81,81,startButton,startButtonOver,in_game)
        button(displayWidth-200,displayHeight-100,81,81,backButton,backButtonOver,main)
        pygame.display.update()
        pygame.event.wait()
def shop_screen():
    while True:
        #button(150,500,100,50,explainButton,explainButtonOver,on_explain_screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(shopScreen,  ( 0,0))
        button(displayWidth-100,displayHeight-100,81,81,startButton,startButtonOver,in_game)
        button(displayWidth-200,displayHeight-100,81,81,backButton,backButtonOver,main)
        button(150,110,83,25,choiceButton,choiceButtonOver,skin_basic)
        button(300,110,83,25,choiceButton,choiceButtonOver,skin_gold)
        button(450,110,83,25,choiceButton,choiceButtonOver,skin_muffler)
        pygame.display.update()
        pygame.event.wait()
            


def in_game ():
    pygame.mixer.music.load('in_game_bgm.mp3')
    pygame.mixer.music.play(-1)
    global coin,characterImage,glacierImage,brokenGlacierImage,score
    while True:
        character['rect']=pygame.Rect((displayWidth-chWidth)/2,displayHeight-chHeight, chWidth,chHeight)
        #randDir=random.randint(0,1)
        
        yCoord=displayHeight-fHeight
        on_rect=rects[0][0]
        front_rect=rects[1][0]
        for l_rects in rects:
            randSpeed=random.randint(2,3)/2
            xList=[50,150,250,350,450,550]
            num=5
            for r in l_rects:
                r['rect'].y=yCoord
                xIndex=random.randint(0,num)
                r['rect'].centerx=xList.pop(xIndex)
                num-=1
                r['rect'].width=80#random.randint(80,100)
                #r['dir']=randDir
                if r['dir']==1:
                    r['speed']=randSpeed
                else:
                    r['speed']=-randSpeed
                if random.randint(0,5)==0:#코인 존재확률 :20%
                    r['FISH']['fish']=True
                    r['FISH']['rect'].centerx=random.randint(r['rect'].left+(r['FISH']['rect'].width/2),r['rect'].right-(r['FISH']['rect'].width/2))
                    r['FISH']['rect'].centery=r['rect'].centery
                else :
                    r['FISH']['fish']=False
                if random.randint(0,10)==0:#부서진 빙하일 확률 :10%
                    r['broken']=True
                else:
                    r['broken']=False
            yCoord-=fHeight
        rects[0][0]['FISH']['fish']=False
        rects[0][0]['broken']=False
        rects[0][1]['FISH']['fish']=False
        rects[0][2]['FISH']['fish']=False
        
        rects[0][0]['rect'].centerx=displayWidth/2
        rects[0][1]['rect'].y=displayHeight
        rects[0][2]['rect'].y=displayHeight
        #첫줄만 코인,부서짐 x 땅 하나만 가운데에 있게 초기화
        
        score=0
        flag=1#default 가 땅 위에 있을 때
        
        check_over=False
        check_re=False
        while not check_over:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                #for r in rects[1]:
                    #여기서 for문으로 모든 땅 검사하는게 아니라 제일 근처의 땅만 front_rect=r 이런 식으로 지정하는게 나을 듯

                if event.type == KEYDOWN:
                    keys=pygame.key.get_pressed()
                    if keys[K_LEFT]:
                    #if event.key == K_LEFT:
                        
                        character['rect'].x-=10
                        if character['dir']==1:
                            characterImage = pygame.transform.flip(characterImage,True,False)
                            character['dir']=0
                    elif event.key == K_RIGHT:
                        character['rect'].x+=10
                        
                        if character['dir']==0:
                            characterImage = pygame.transform.flip(characterImage,True,False)
                            character['dir']=1
                    if event.key == K_SPACE and flag==1:#flag==1 안붙이면 바다에 빠질때도 한번 더누르면 점프해서 이미지크기가 -가 되면서 오류남
                        jump()
                        for r in rects[1]:
                            if r['rect'].right>=character['rect'].centerx and r['rect'].left<=character['rect'].centerx and r['rect'].top==displayHeight-fHeight:
                                on_rect=r
                                break
                            else:
                                continue
                            
                        if on_rect['rect'].right>=character['rect'].centerx and on_rect['rect'].left<=character['rect'].centerx and on_rect['rect'].top==displayHeight-fHeight and on_rect['broken']==False:
                            score+=1
                            flag=1
                            #점프했을때 땅을 밟아야하고 땅이 부서져있지 않아야함
                        else :
                            flag=0
                        #게임화면 아래로 나가는 땅을 리스트 맨 앞에서 맨 뒤로 보냄   
                        rects.append(rects.pop(0))
                        #땅이 근처에 없을 때 점프하면 바다에 빠지면서 게임오버
                        if flag==0:
                            pygame.mixer.music.stop()
                            pygame.mixer.Sound.play(gameover1Sound)
                            for i in range (20):
                                character['rect'].width-=chWidth/22

                                character['rect'].left+=chWidth/36
                                character['rect'].height-=chHeight/22
                                character['rect'].top+=chHeight/24
                                time.sleep(0.015)
                                draw_screen()
                                pygame.display.update()    
                            #print("game over")
                            #print(flag)
                            check_over=True
          
                        
                            
                        #flag가 1일 때 -> 캐릭터가 길을 건넜을 때
                        else:
                            randSpeed=( random.randint(2,3) + (score/50)*random.randint(2,3) )/2
                            #땅들의 위치와 랜덤으로 지정, flag 다시 0으로
                            xList=[50,150,250,350,450,550]
                            num=5
                            for r in rects[5]:
                                r['rect'].top=displayHeight-fHeight*6
                                xIndex=random.randint(0,num)
                                r['rect'].centerx=xList.pop(xIndex)
                                num-=1
                                r['rect'].width=random.randint(70,80)-random.randint(1,2)*score/3
                                #r['dir']=randDir
                                if r['dir']==1:
                                    r['speed']=randSpeed
                                else:
                                    r['speed']=-randSpeed
                                if random.randint(0,5)==0:#코인 존재확률 :20%
                                    r['FISH']['fish']=True
                                    r['FISH']['rect'].centerx=random.randint(r['rect'].left+15,r['rect'].right-15)
                                    r['FISH']['rect'].centery=r['rect'].centery

                                else:
                                    r['fish']=False
                                if random.randint(0,10)==0:#부서진 빙하일 확률 :10%
                                    r['broken']=True
                                else:
                                    r['broken']=False
                            #flag=0                     
            for l_rects in rects:
                for r in l_rects:
                    #if (r['num']!=on_rect['num']):
                    if r['rect'].left>=displayWidth:
                        r['rect'].right=0
                        r['FISH']['rect'].right=0
                    elif r['rect'].right<=0:
                        r['rect'].left=displayWidth
                        r['FISH']['rect'].left=displayWidth
                    r['rect'].centerx += r['speed']
                    r['FISH']['rect'].centerx += r['speed']
            character['rect'].centerx +=on_rect['speed']
            #땅들이 계속 좌우로 움직이고, 캐릭터가 밟은 땅의 속도에 맞춰서 캐릭터도 이동됨
            
            if character['rect'].left>=displayWidth or character['rect'].right<=0  :
                check_over=True
            #캐릭터가 화면 밖으로 나가면 게임 오버
            if (character['rect'].centerx>on_rect['rect'].right or character['rect'].centerx<on_rect['rect'].left ) and flag==1 :
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(gameover1Sound)
                for i in range (20):
                    character['rect'].width-=chWidth/22
                    character['rect'].left+=chWidth/36
                    character['rect'].height-=chHeight/22
                    character['rect'].top+=chHeight/24
                    time.sleep(0.015)
                    draw_screen()
                    pygame.display.update()    
                check_over=True
            if on_rect['FISH']['fish']==True and (on_rect['FISH']['rect'].left<=character['rect'].right and on_rect['FISH']['rect'].right>=character['rect'].left and on_rect['FISH']['rect'].bottom>=character['rect'].top):
                on_rect['FISH']['fish']=False
                coin+=1
            draw_screen()
            draw_text()
            pygame.display.update()
            time.sleep(0.01)
            
        while not check_re:
            #pygame.mixer.music.stop()
            #pygame.mixer.Soundplay(gameover1Sound)
            button(displayWidth/2-37.5,displayHeight/2-37.5,75,75,reButton,reButtonOver,in_game)
            button(displayWidth/2-37.5,displayHeight/2+75,75,75,mainButton,mainButtonOver,main)
            #사진 메인화면가는 버튼으로 바꾸기
            gameover_screen()  
            pygame.display.update()
            pygame.event.wait()


def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                return

    

#처음 시작 타이틀 화면 
def main():
    pygame.mixer.music.load('title_bgm.mp3')
    pygame.mixer.music.play(-1)
    while not begin:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit( mainBackgroundImage,(0,0))
        screen.blit( title,(300-91.5,50))
        screen.blit( characterImage,(50,200))
        
        #button함수 argument -> 순서대로 x좌표,y좌표,너비,높이,일반버튼이미지,호버링버튼이미지
        button(259.5,175,81,81,startButton,startButtonOver,in_game)#크기 81x81
        button(258.5,280,83,25,tutorialButton,tutorialButtonOver,on_explain_screen)#크기 83x25
        button(258.5,325,83,25,shopButton,shopButtonOver,shop_screen)
        pygame.display.update( )
        pygame.event.wait()
    pygame.quit
    
if __name__ == '__main__':
    main()
