import pygame
import sys
import random
from pygame.locals import *

pygame.mixer.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED=(234,152,132)
GREEN = (187, 192, 0)
BLUE=(157,204,224)
GRAY=(204,204,204)

WIDTH = 941
HEIGHT = 673
FPS = 60
words = [['こんにちは', '世界', 'ゲーム', 'プログラミング',"進入",
          "親友","時間","旅行","紅葉","夢中",
          "スーパー","ニート","ヤニカス","洗濯機","ウインナー",
          "スタバ","ルフィ","黄猿","エクセル","食堂",
          "頻尿","シーパップ","豚鼻","尿漏れ","バイト",
          "金欠","クソガキ","財布","定時","アイフォン",
          "アンドロイド","坊主","電卓","研究","定時",
          "華金","コップ","なんで","ワロタ","自分",
          "ですね。","はい？","45度","ヒカキン","みそきん",
          "デカキン","ユニクロ","あいみょん","バーキン","マクド",
          "アイクぬわら","おぎやはぎ","ヨネダ2000","フワちゃん","粗品",
          "エビチリ","バナナマン","ヤムチャ","クリリン","ベジータ",
          "ヤフー","ホリエモン","ワークマン","ヤケクソ","キルア",
          "ペプシマン","本の虫","ドルヲタ","鼻くそ","ガンダム",
          "正露丸","ステンドグラス","校歌","覇気","ガンタンク",
          "ララパーク","ハンコック","スペイン村","納豆","チャンジャ",
          "トッポギ","ラーメン","タピオカ","推し活","ネズコ"],
        ["konnnitiha","sekai","ge-mu","puroguramingu","sinnnyuu",
         "sinyuu","jikann","ryokou","kouyou","mutyuu",
         "su-pa-","ni-to","yanikasu","sentakuki","uinnna-",
         "sutaba","rufi","kizaru","ekuseru","syokudou",
         "hinnnyou","si-pappu","butabana","nyoumore","baito",
         "kinketu","kusogaki","saihu","teiji","aifonn",
         "andoroido","bouzu","dentaku","kenkyuu","teiji",
         "hanakinn","koppu","nande","warota","jibunn",
         "desune.","hai?","45do","hikakinn","misokinn",
         "dekakinn","yunikuro","aimyonn","ba-kinn","makudo",
         "aikunuwara","ogiyahagi","yoneda2000","huwatyann","sosina",
         "ebitiri","bananamann","yamutya","kuririnn","beji-ta",
         "yahu-","horiemonn","wa-kumann","yakekuso","kirua",
         "pepusimann","honnnomusi","doruwota","hanakuso","gandamu",
         "seirogann","sutendogurasu","kouka","haki","gantanku",
         "rarapa-ku","hankokku","supeinmura","nattou","tyanja",
         "toppogi","ra-menn","tapioka","osikatu","nezuko"]]

words2=[["先人の知恵","ピーナッツバター","イカ２貫","ペンパイナッポーアッポーペン","しのけん大食い",
         "給食こぼした","ピカソの本名クソ長い","生乾き臭","有給休暇","ママさんバレー",
         "地獄のプール前シャワー","出席番号127番","危なすぎる遊具","シーソーで骨折","恐怖の調理実習",
         "二ノ宮金次郎像","傘盗まれがち","一輪車乗りこなす男子","最古の木造建築法隆寺","この気持ちは何だろう",
         "屋上で記念撮影","教室のガラス割れがち","涙のない卒業式","給食2倍","ぴえんぱおんひいん",
         "朝早すぎるラジオ体操","夏休みの自由研究","蜂に刺された","からあげクンまずい","ファミチキうますぎ",
         "リコーダー臭すぎ","アルトとソプラノの狭間","サッカー音痴","バレエ大好き","高野豆腐",
         "グリーンブリーフマン","習字かばん派手すぎ","クソダサティーシャツ","職員室涼しい","ウサギの世話係",
         "トマトの水やり係","マラソン大会ガチ勢","室温40度","下駄箱臭すぎ","ココイチ臭すぎ",
         "昼休み短い","痛かったファール","往復4時間","ヤンキーのせいで遅刻","宇宙の果てまで飛んでいけ",
         "次の月に死んだ","絶対に成功させようね","せっせっせいや","ひかり太刀魚","愛が足りひん",
         "世間がおかしいと思う","千葉県いいとこ","張り切りチャイティーヨ","微動だにしない","組体操禁止",
         "足速いやつはモテる","ブザービート","堕落の懺悔室","牛タンチケット","仮想通貨で大儲け",
         "通勤時間徒歩5分","ライジングサン踊れる","恋するフォーチュンクッキー","許してやったらどうや","外周5周",
         "忍者サスケ","ピンク色のマスク","万年準優勝","秋の体力づくり","ハマスカ放送部"],
        ["senjinnnotie","pi-nattubata-","ika2kann","penpainappo-appo-penn","sinokenoogui",
         "kyuusyokukobosita","pikasonohonmyoukusonagai","namagawakisyuu","yuukyuukyuuka","mamasanbare-",
         "jigokunopu-rumaesyawa-","syussekibangou127bann","abunasugiruyuugu","si-so-dekossetu","kyouhunotyourijissyuu",
         "ninomiyakinjirouzou","kasanusumaregati","itirinsyanorikonasudansi","saikonomokuzoukentikuhouryuuji","konokimotihanandarou",
         "okujoudekinensatuei","kyousitunogarasuwaregati","namidanonaisotugyousiki","kyuusyoku2bai","pienpaonhiinn",
         "asahayasugirurajiotaisou","natuyasuminojiyuukenkyuu","hatinisasareta","karaagekunmazui","famitikiumasugi",
         "riko-da-kusasugi","arutotosopuranonohazama","sakka-onti","bareedaisuki","kouyadouhu",
         "guri-nburi-humann","syuujikabanhadesugi","kusodasathi-syatu","syokuinsitusuzusii","usaginosewagakari",
         "tomatonomizuyarigakari","marasontaikaigatizei","situon40do","getabakokusasugi","kokoitikusasugi",
         "hiruyasumimijikai","itakattafa-ru","ouhuku4jikann","yanki-noseidetikoku","utyuunohatemadetondeike",
         "tuginotukinisinda","zettainiseikousaseyoune","sessesseiya","hikaritatiuo","aigatarihinn",
         "sekengaokasiitoomou","tibakeniitoko","harikirityaithi-yo","bidoudanisinai","kumitaisoukinsi",
         "asihayaiyatuhamoteru","buza-bi-to","darakunozangesitu","gyuutantiketto","kasoutuukadeoomouke",
         "tuukinjikantoho5hunn","raijingusanodoreru","koisurufo-tyunkukki-","yurusiteyattaradouya","gaisyuu5syuu",
         "ninjasasuke","pinkuironomasuku","bannnenjunyuusyou","akinotairyokudukuri","hamasukahousoubu"]]
time_remain=5*FPS
time_remain2=7*FPS
q_num=0
input_text=""
ans_check_txt=""
words_idx=random.randint(0,84)
words_idx2=random.randint(0,74)
current_word = words[0][words_idx]
current_word2=words2[0][words_idx2]
ipt_key_bf=[""]*50
ipt_key_af=[""]*50
ipt_len=0
ipt_len_af=0

img_bg=pygame.image.load("images/blackboard.png")
img_kyositu=pygame.image.load("images/kyositu.jpg")
img_keiji=pygame.image.load("images/keijiban.jpg")
img_bbryodo=pygame.image.load("images/bbryodo.jpg")
img_title=pygame.image.load("images/title.png")
img_miyake=pygame.image.load("images/miyake.png")
img_kametani=pygame.image.load("images/kametani.png")
img_sakatoku=pygame.image.load("images/sakatoku.png")
img_yada=pygame.image.load("images/yada.png")
characters=[img_miyake,img_kametani,img_sakatoku,img_yada]
comments=["遅くてもいいから手元は見ないように！","手首は固定できてる？","君はまだまだ速くなれる","どのキーをどの指で打つか決めるんだ",
          "トレーニングモードでじっくり練習するのも良き","タイピング速いと「仕事できそうなやつ」に見える"]

chaimu=pygame.mixer.Sound("sounds/chaimu.mp3")
taiko=pygame.mixer.Sound("sounds/taiko_se.mp3")
correct=pygame.mixer.Sound("sounds/correct.mp3")
incorrect=pygame.mixer.Sound("sounds/incorrect.mp3")
success=pygame.mixer.Sound("sounds/success.mp3")
sippai=pygame.mixer.Sound("sounds/sippai.mp3")
pygame.mixer.music.load("sounds/taiko_bgm.ogg")

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def init_question(index):
    global time_remain,time_remain2,q_num,input_text,ans_check_txt,words_idx,words_idx2,current_word,current_word2,ipt_key_bf,ipt_key_af,ipt_len,ipt_len_af
    time_remain=5*FPS
    time_remain2=7*FPS
    q_num=q_num+1
    input_text = ""  
    ans_check_txt=""
    if index==13:         
        words_idx=random.randint(0,84)
        current_word = words[0][words_idx]
    elif index==14 or index==15 or index==19:
        words_idx2=random.randint(0,74)
        current_word2 = words2[0][words_idx2]
    ipt_key_bf=[""]*50
    ipt_key_af=[""]*50
    ipt_len=0
    ipt_len_af=0

def text_judge(index):
    global ipt_key_af,ipt_len_af
    if ipt_len>=3:
        if ipt_key_af[ipt_len_af-3]=="c" and ipt_key_af[ipt_len_af-2]=="h" and ipt_key_af[ipt_len_af-1]=="i":
            ipt_key_af[ipt_len_af-3]="t"
            ipt_key_af[ipt_len_af-2]="i"
            ipt_len_af=ipt_len_af-1
        if ipt_key_af[ipt_len_af-2]=="f" and ipt_key_af[ipt_len_af-1]=="u":
            ipt_key_af[ipt_len_af-2]="h"
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="a":
            ipt_key_af[ipt_len_af-2]="l"
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="i":
            ipt_key_af[ipt_len_af-2]="l" 
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="u":
            ipt_key_af[ipt_len_af-2]="l" 
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="e":
            ipt_key_af[ipt_len_af-2]="l" 
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="o":
            ipt_key_af[ipt_len_af-2]="l" 
        if ipt_key_af[ipt_len_af-2]=="z" and ipt_key_af[ipt_len_af-1]=="i":
            ipt_key_af[ipt_len_af-2]="j"
        if ipt_key_af[ipt_len_af-3]=="s" and ipt_key_af[ipt_len_af-2]=="h" and ipt_key_af[ipt_len_af-1]=="a":
            ipt_key_af[ipt_len_af-3]="s"
            ipt_key_af[ipt_len_af-2]="y"
        if ipt_key_af[ipt_len_af-3]=="s" and ipt_key_af[ipt_len_af-2]=="h" and ipt_key_af[ipt_len_af-1]=="u":
            ipt_key_af[ipt_len_af-3]="s"
            ipt_key_af[ipt_len_af-2]="y"
        if ipt_key_af[ipt_len_af-3]=="s" and ipt_key_af[ipt_len_af-2]=="h" and ipt_key_af[ipt_len_af-1]=="o":
            ipt_key_af[ipt_len_af-3]="s"
            ipt_key_af[ipt_len_af-2]="y"
        if ipt_key_af[ipt_len_af-3]=="c" and ipt_key_af[ipt_len_af-2]=="h" and ipt_key_af[ipt_len_af-1]=="a":
            ipt_key_af[ipt_len_af-3]="t"
            ipt_key_af[ipt_len_af-2]="y"
        if ipt_key_af[ipt_len_af-3]=="c" and ipt_key_af[ipt_len_af-2]=="h" and ipt_key_af[ipt_len_af-1]=="u":
            ipt_key_af[ipt_len_af-3]="t"
            ipt_key_af[ipt_len_af-2]="y"
        if ipt_key_af[ipt_len_af-3]=="c" and ipt_key_af[ipt_len_af-2]=="h" and ipt_key_af[ipt_len_af-1]=="o":
            ipt_key_af[ipt_len_af-3]="t"
            ipt_key_af[ipt_len_af-2]="y"
        if ipt_key_af[ipt_len_af-3]=="z" and ipt_key_af[ipt_len_af-2]=="y" and ipt_key_af[ipt_len_af-1]=="a":
            ipt_key_af[ipt_len_af-3]="j"
            ipt_key_af[ipt_len_af-2]="a"
            ipt_len_af=ipt_len_af-1
        if ipt_key_af[ipt_len_af-3]=="z" and ipt_key_af[ipt_len_af-2]=="y" and ipt_key_af[ipt_len_af-1]=="u":
            ipt_key_af[ipt_len_af-3]="j"
            ipt_key_af[ipt_len_af-2]="u"
            ipt_len_af=ipt_len_af-1
        if ipt_key_af[ipt_len_af-3]=="z" and ipt_key_af[ipt_len_af-2]=="y" and ipt_key_af[ipt_len_af-1]=="o":
            ipt_key_af[ipt_len_af-3]="j"
            ipt_key_af[ipt_len_af-2]="o"
            ipt_len_af=ipt_len_af-1
        if ipt_key_af[ipt_len_af-3]=="u" and ipt_key_af[ipt_len_af-2]=="l" and ipt_key_af[ipt_len_af-1]=="o":
            ipt_key_af[ipt_len_af-3]="w"
            ipt_key_af[ipt_len_af-2]="h"
        if ipt_key_af[ipt_len_af-3]=="u" and ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="o":
            ipt_key_af[ipt_len_af-3]="w"
            ipt_key_af[ipt_len_af-2]="h"
        if ipt_key_af[ipt_len_af-3]=="s" and ipt_key_af[ipt_len_af-2]=="h" and ipt_key_af[ipt_len_af-1]=="e":
            ipt_key_af[ipt_len_af-3]="s"
            ipt_key_af[ipt_len_af-2]="y" 
        if ipt_key_af[ipt_len_af-3]=="c" and ipt_key_af[ipt_len_af-2]=="h" and ipt_key_af[ipt_len_af-1]=="e":
            ipt_key_af[ipt_len_af-3]="t"
            ipt_key_af[ipt_len_af-2]="y" 
        if index==13:
            if len(words[1][words_idx])>=ipt_len_af:
                if words[1][words_idx][ipt_len_af-3]!="n" and words[1][words_idx][ipt_len_af-2]=="n"and words[1][words_idx][ipt_len_af-1]!="n":
                        if ipt_key_af[ipt_len_af-2]=="n"and ipt_key_af[ipt_len_af-1]=="n":
                            ipt_key_af[ipt_len_af-1]=""
                            ipt_len_af=ipt_len_af-1
        else:
            if len(words2[1][words_idx2])>=ipt_len_af:
                if words2[1][words_idx2][ipt_len_af-3]!="n" and words2[1][words_idx2][ipt_len_af-2]=="n"and words2[1][words_idx2][ipt_len_af-1]!="n":
                        if ipt_key_af[ipt_len_af-2]=="n"and ipt_key_af[ipt_len_af-1]=="n":
                            ipt_key_af[ipt_len_af-1]=""
                            ipt_len_af=ipt_len_af-1
    elif ipt_len==2:
        if ipt_key_af[ipt_len_af-2]=="f" and ipt_key_af[ipt_len_af-1]=="u":
            ipt_key_af[ipt_len_af-2]="h"
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="a":
            ipt_key_af[ipt_len_af-2]="l"
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="i":
            ipt_key_af[ipt_len_af-2]="l" 
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="u":
            ipt_key_af[ipt_len_af-2]="l" 
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="e":
            ipt_key_af[ipt_len_af-2]="l" 
        if ipt_key_af[ipt_len_af-2]=="x" and ipt_key_af[ipt_len_af-1]=="o":
            ipt_key_af[ipt_len_af-2]="l" 
        if ipt_key_af[ipt_len_af-2]=="z" and ipt_key_af[ipt_len_af-1]=="i":
            ipt_key_af[ipt_len_af-2]="j"
    

def main():
    global ipt_key_bf,ipt_key_af,ipt_len,ipt_len_af,input_text,q_num,current_point
    global ans_check_txt,time_remain,time_remain2
    pygame.init()
    pygame.display.set_caption('タイピングゲーム')
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font("Noto_Sans_JP/static/NotoSansJP-Medium.ttf", 20)
    font2 = pygame.font.Font("Noto_Sans_JP/static/NotoSansJP-Medium.ttf", 30)
    font3=pygame.font.Font("Noto_Sans_JP/static/NotoSansJP-Medium.ttf", 16)

    current_point=100
    fl_idx=open("savedata/idx.txt","r")
    idx=int(fl_idx.read())
    fl_idx.close
    tmr=0
    talk_idx=0
    trn_tlk_idx=0
    fl_plv=open("savedata/plv.txt","r")#どうしてもReadから始まってしまう。実際に遊んでもらうときは、ゲームと一緒に「0」が入ったファイルもインストールしてもらう必要あり
    pl_lv=int(fl_plv.read())
    fl_plv.close()
    game_lv=0
    fl_clrnum=open("savedata/clrnum.txt","r")
    clr_num=int(fl_clrnum.read())
    fl_clrnum.close()
    fl_clrnum2=open("savedata/clrnum2.txt","r")
    clr_num2=int(fl_clrnum2.read())
    fl_clrnum2.close()
    fl_clrnum3=open("savedata/clrnum3.txt","r")
    clr_num3=int(fl_clrnum3.read())
    fl_clrnum3.close()
    fl_talkskip=open("savedata/talkskip.txt","r")
    talkskip_flg=int(fl_talkskip.read())
    fl_talkskip.close()
    fl_tlkskp_train=open("savedata/tlkskp_train.txt","r")
    tlkskp_train_flg=int(fl_tlkskp_train.read())
    fl_tlkskp_train.close()
    txt_basket=font3.render("最も楽しむ者が最も強い！",True,WHITE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fl_idx=open("savedata/idx.txt","w")
                fl_idx.write("9")
                fl_idx.close
                pygame.quit()
                sys.exit()
            if idx==13 or idx==14 or idx==15 or idx==19:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:
                        if ipt_len>0:
                            ipt_key_bf[ipt_len-1] = ""
                            input_text=input_text[:-1]             
                            ipt_len=ipt_len-1

                            ipt_key_af[ipt_len_af-1]=""  
                            ipt_len_af=ipt_len_af-1
                    else:
                        ipt_key_bf[ipt_len]=event.unicode               
                        ipt_len=ipt_len+1
                        input_text=input_text+ipt_key_bf[ipt_len-1]
                        
                        ipt_key_af[ipt_len_af]=event.unicode
                        ipt_len_af=ipt_len_af+1
       

        if tmr%300==0:
            rd_chr=characters[random.randint(0,3)]
            rd_cmt=comments[random.randint(0,5)]
            chr_height=600-rd_chr.get_height()
            chr_width=200-rd_chr.get_width()/2

        tmr=tmr+1
        key=pygame.key.get_pressed()
        mouse_x,mouse_y=pygame.mouse.get_pos()
        mbtn1,mbtn2,mbtn3=pygame.mouse.get_pressed()

        if idx ==9:
            chaimu.play()
            window.fill(BLACK)
            window.blit(img_bg,[0,0])
            window.blit(img_bbryodo,[50,30])
            window.blit(img_title,[15,70])
            window.blit(img_miyake,[60,430])
            window.blit(img_kametani,[260,500])
            window.blit(img_sakatoku,[460,450])
            window.blit(img_yada,[660,430])
            draw_text(window,"スペースキーでスタート",font,WHITE,320,420)
            if key[K_SPACE]==True:
                chaimu.stop()
                if talkskip_flg==0:
                    idx=10
                    tmr=0
                    pygame.mixer.music.play(-1)
                elif talkskip_flg==1:
                    idx=11
                    tmr=0
                    pygame.mixer.music.play(-1)
            
        if idx == 10:
            if talk_idx==0:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_miyake,[400,100])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt1=font.render("ミヤケ先生「よく来たな！新入生諸君。入学おめでとう」",True,WHITE)
                window.blit(txt1,[50,480])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=1
                    tmr=0
            if talk_idx==1:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_miyake,[400,100])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt2=font.render("ミヤケ先生「ここタイピング学園は、手元を見ずにタイピングをする「ブラインドタッチ」",True,WHITE)
                window.blit(txt2,[50,480])
                txt3=font.render("を身につけ、タイピングの速度をアップさせるために作られた専門学校だ」",True,WHITE)
                window.blit(txt3,[50,520])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=2
                    tmr=0
            if talk_idx==2:
                window.fill(WHITE)
                window.blit(img_kyositu,[0,0])
                window.blit(img_kametani,[400,160])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt4=font.render("カメタニ先生「手元を見ずにスラスラタイピングすることができるようになれば、",True,WHITE)
                window.blit(txt4,[50,480])
                txt5=font.render("レポートの作成や仕事の作業効率がかなりアップするわ」",True,WHITE)
                window.blit(txt5,[50,520])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=3
                    tmr=0
            if talk_idx==3:
                window.fill(WHITE)
                window.blit(img_kyositu,[0,0])
                window.blit(img_kametani,[400,160])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt6=font.render("カメタニ先生「上達するにつれて、目に見えて日々の作業で効果を感じられるスキルなのよ。",True,WHITE)
                window.blit(txt6,[50,480])
                txt7=font.render("ここで身につけていってちょうだい」",True,WHITE)
                window.blit(txt7,[50,520])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=4
                    tmr=0
            if talk_idx==4:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_sakatoku,[380,130])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt8=font.render("サカトク先生「最後に、トレーニングに入る前に上達のコツを伝えさせてくれ」",True,WHITE)
                window.blit(txt8,[50,480])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=5
                    tmr=0
            if talk_idx==5:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_sakatoku,[380,130])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt9=font.render("サカトク先生「一つは、どのキーをどの指で押すのかを決めることだ。",True,WHITE)
                window.blit(txt9,[50,480])
                txt10=font.render("[A]は左手小指、[I]は右手指といった感じで。手首は動かさずに打つのがコツだ。」",True,WHITE)
                window.blit(txt10,[50,520])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=6
                    tmr=0
            if talk_idx==6:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_sakatoku,[380,130])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt11=font.render("サカトク先生「人差し指だけで打っていたりしていると、スピードがでないぞ」",True,WHITE)
                window.blit(txt11,[50,480])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=7
                    tmr=0
            if talk_idx==7:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_sakatoku,[380,130])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt12=font.render("サカトク先生「そしてもう一つのコツは、最初は遅くていいから手元をなるべく見ずに打つことだ。",True,WHITE)
                window.blit(txt12,[50,480])
                txt13=font.render("手元を見て打つと遅いしミスタイプにも気づかない」",True,WHITE)
                window.blit(txt13,[50,520])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=8
                    tmr=0
            if talk_idx==8:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_sakatoku,[380,130])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt14=font.render("サカトク先生「最初はもどかしいと思うが、長い目で見れば手元を見ずに打つ方が速い。",True,WHITE)
                window.blit(txt14,[50,480])
                txt15=font.render("スピードは後からついてくる。」",True,WHITE)
                window.blit(txt15,[50,520])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=9
                    tmr=0
            if talk_idx==9:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_sakatoku,[380,130])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                txt16=font.render("サカトク先生「それじゃあ早速、授業開始。」",True,WHITE)
                window.blit(txt16,[50,480])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    talk_idx=10
                    tmr=0
            if talk_idx==10:
                window.fill(BLACK)
                txt17=font.render("※この作品はすべてフィクションです。",True,WHITE)
                window.blit(txt17,[50,330])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    idx=11
                    tmr=0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play(-1)

        elif idx==11:
            input_text=""
            ipt_key_bf=[""]*50
            ipt_key_af=[""]*50
            ipt_len=0
            ipt_len_af=0
            fl_idx=open("savedata/idx.txt","w")
            fl_idx.write(str(idx))
            fl_idx.close()
            talkskip_flg=1
            fl_talkskip=open("savedata/talkskip.txt","w")
            fl_talkskip.write(str(talkskip_flg))
            fl_talkskip.close()
            q_num=0
            current_point=100
            window.fill(BLACK)
            if pl_lv==0:
                window.blit(img_bg,[0,0])
                window.blit(rd_chr,[chr_width,chr_height])
                draw_text(window,rd_cmt,font,WHITE,300,450)
                window.blit(img_bbryodo,[670,30])
                draw_text(window,"モード選択",font2,WHITE,70,80)
                pygame.draw.rect(window,BLUE,[100,150,110,100])
                draw_text(window,"Easy",font2,BLACK,120,180)
                pygame.draw.rect(window,GRAY,[630,150,110,100])           
                draw_text(window,"training",font,BLACK,640,190)
            elif pl_lv==1:
                window.blit(img_bg,[0,0])
                window.blit(rd_chr,[chr_width,chr_height])
                draw_text(window,rd_cmt,font,WHITE,300,450)
                window.blit(img_bbryodo,[670,30])
                draw_text(window,"モード選択",font2,WHITE,70,80)
                pygame.draw.rect(window,BLUE,[100,150,110,100])
                draw_text(window,"Easy",font2,BLACK,120,180)
                pygame.draw.rect(window,GREEN,[260,150,110,100])
                draw_text(window,"Normal",font2,BLACK,265,180)
                pygame.draw.rect(window,GRAY,[630,150,110,100])           
                draw_text(window,"training",font,BLACK,640,190)
            elif pl_lv>=2:
                window.blit(img_bg,[0,0])
                window.blit(rd_chr,[chr_width,chr_height])
                draw_text(window,rd_cmt,font,WHITE,300,450)
                window.blit(img_bbryodo,[670,30])
                draw_text(window,"モード選択",font2,WHITE,70,80)
                pygame.draw.rect(window,BLUE,[100,150,110,100])
                draw_text(window,"Easy",font2,BLACK,120,180)
                pygame.draw.rect(window,GREEN,[260,150,110,100])
                draw_text(window,"Normal",font2,BLACK,265,180)
                pygame.draw.rect(window,RED,[420,150,110,100])           
                draw_text(window,"Hard",font2,BLACK,440,180)
                pygame.draw.rect(window,GRAY,[630,150,110,100])           
                draw_text(window,"training",font,BLACK,640,190)
            if 100<mouse_x and mouse_x<210 and 150<mouse_y and mouse_y<250 and mbtn1==True and mbtn2==False and mbtn3==False:
                idx=12
                game_lv=1
                tmr=0
                pygame.mixer.music.stop()
                taiko.play()
            elif 260<mouse_x and mouse_x<370 and 150<mouse_y and mouse_y<250 and mbtn1==True and mbtn2==False and mbtn3==False:
                if pl_lv>=1:
                    idx=12
                    game_lv=2
                    tmr=0
                    pygame.mixer.music.stop()
                    taiko.play()
            elif 420<mouse_x and mouse_x<530 and 150<mouse_y and mouse_y<250 and mbtn1==True and mbtn2==False and mbtn3==False:
                if pl_lv>=2:
                    idx=12
                    game_lv=3
                    tmr=0
                    pygame.mixer.music.stop()
                    taiko.play()
            elif 640<mouse_x and mouse_x<750 and 150<mouse_y and mouse_y<250 and mbtn1==True and mbtn2==False and mbtn3==False:
                if tlkskp_train_flg==0:
                    idx=18
                    tmr=0
                    pygame.mixer.music.stop()
                    taiko.play()
                else:
                    idx=19
                    tmr=0
                    pygame.mixer.music.stop()
                    taiko.play()

        elif idx==12:
            window.fill(BLACK)
            window.blit(img_bg,[0,0])
            window.blit(img_keiji,[100,50])
            if game_lv==1:
                draw_text(window, "ルール", font2, BLACK, 200, 200)
                draw_text(window, "問題数:20問", font, BLACK, 200, 240)
                draw_text(window, "一問当たりの制限時間:5秒", font, BLACK, 200, 270)
                draw_text(window, "100点満点、1問タイムオーバーで-10点、60点以上でクリア", font, BLACK, 200, 300)
                draw_text(window, "複数の入力パターンに対応: 例、「じ」→ zi,jiどちらでもOK", font, BLACK, 200, 360)
                draw_text(window,"スペースでスタート",font,BLACK,500,500)
                if key[K_SPACE]==True and tmr>30:
                    idx=13
                    tmr=0
            elif game_lv==2:
                draw_text(window, "ルール", font2, BLACK, 200, 200)
                draw_text(window, "問題数:20問", font, BLACK, 200, 240)
                draw_text(window, "一問当たりの制限時間:", font, BLACK, 200, 270)
                draw_text(window, "7秒", font, RED, 420, 270)
                draw_text(window, "100点満点、1問タイムオーバーで-10点、60点以上でクリア", font, BLACK, 200, 300)
                draw_text(window, "複数の入力パターンに対応: 例、「じ」→ zi,jiどちらでもOK", font, BLACK, 200, 360)
                draw_text(window,"スペースでスタート",font,BLACK,500,500)
                if key[K_SPACE]==True and tmr>30:
                    idx=14
                    tmr=0
            elif game_lv==3:
                draw_text(window, "ルール", font2, BLACK, 200, 200)
                draw_text(window, "問題数:20問", font, BLACK, 200, 240)
                draw_text(window, "一問当たりの制限時間:", font, BLACK, 200, 270)
                draw_text(window, "5秒", font, RED, 420, 270)
                draw_text(window, "100点満点、1問タイムオーバーで-10点、60点以上でクリア", font, BLACK, 200, 300)
                draw_text(window, "複数の入力パターンに対応: 例、「じ」→ zi,jiどちらでもOK", font, BLACK, 200, 360)
                draw_text(window,"スペースでスタート",font,BLACK,500,500)
                if key[K_SPACE]==True and tmr>30:
                    idx=15
                    tmr=0

        elif idx==13:
            window.fill(BLACK)
            window.blit(img_kyositu,[0,0])
            window.blit(img_miyake,[400,100])
            pygame.draw.rect(window,BLACK,[0,300,941,300])
            time_remain=time_remain-1
            if q_num >= 5:#ここ戻す
                if clr_num==0:
                    if current_point>=60:           
                        pl_lv=pl_lv+1
                        clr_num=clr_num+1
                    idx = 16
                    tmr=0
                    fl_plv=open("savedata/plv.txt","w")
                    fl_plv.write(str(pl_lv))
                    fl_plv.close()
                    fl_clrnum=open("savedata/clrnum.txt","w")
                    fl_clrnum.write(str(clr_num))
                    fl_clrnum.close()
                else:
                    idx=17
                    tmr=0
            else:
                draw_text(window, "次の単語を入力:", font, WHITE, 20, 320)
                draw_text(window, current_word, font2, WHITE, 20, 360)
                draw_text(window, "残り問題数: " + str(20-q_num), font2, WHITE, WIDTH - 370, 20)
                draw_text(window, "持ち点: " + str(current_point)+"点", font2, WHITE, WIDTH - 370, 60)
                draw_text(window, "残り時間: " + str(time_remain//FPS+1)+"秒", font2, WHITE, WIDTH - 220, 320)
                draw_text(window,"Escで終了して戻る",font,WHITE,600,600)

                if time_remain==0:
                    incorrect.play()
                    current_point=current_point-10
                    init_question(idx)

                text_judge(idx)
                if len(words[1][words_idx])==ipt_len_af:
                    for i in range(ipt_len_af):
                        ans_check_txt=ans_check_txt+ipt_key_af[i]
                if words[1][words_idx] == ans_check_txt:
                    correct.play()
                    init_question(idx)
                else:
                    ans_check_txt=""
            draw_text(window, input_text, font, WHITE, 20, 400)
            tmr=0

            if key[K_ESCAPE]==True:
                idx=11
                tmr=0
                pygame.mixer.music.play(-1)
        
        elif idx==14:
            if pl_lv>=1:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_kametani,[400,160])
                pygame.draw.rect(window,BLACK,[0,300,941,300])        
                time_remain2=time_remain2-1
                if q_num >= 5:#ここ戻す
                    if clr_num2==0:  
                        if current_point>=60:                   
                            pl_lv=pl_lv+1
                            clr_num2=clr_num2+1
                        idx=16
                        tmr=0
                        fl_plv=open("savedata/plv.txt","w")
                        fl_plv.write(str(pl_lv))
                        fl_plv.close()
                        fl_clrnum2=open("savedata/clrnum2.txt","w")
                        fl_clrnum2.write(str(clr_num2))
                        fl_clrnum2.close()
                    else:
                        idx=17
                        tmr=0
                else:
                    draw_text(window, "次の単語を入力:", font, WHITE, 20, 320)
                    draw_text(window, current_word2, font2, WHITE, 20, 360)
                    draw_text(window, "残り問題数: " + str(20-q_num), font2, WHITE, WIDTH - 370, 20)
                    draw_text(window, "持ち点: " + str(current_point)+"点", font2, WHITE, WIDTH - 370, 60)
                    draw_text(window, "残り時間: " + str(time_remain2//FPS+1)+"秒", font2, WHITE, WIDTH - 220, 320)
                    draw_text(window,"Escで終了して戻る",font,WHITE,600,600)

                    if time_remain2==0:
                        incorrect.play()
                        current_point=current_point-10
                        init_question(idx)
                    
                    text_judge(idx)

                    if len(words2[1][words_idx2])==ipt_len_af:
                        for i in range(ipt_len_af):
                            ans_check_txt=ans_check_txt+ipt_key_af[i]

                    if words2[1][words_idx2] == ans_check_txt:
                        correct.play()
                        init_question(idx)
                    else:
                        ans_check_txt=""

                draw_text(window, input_text, font, WHITE, 20, 400)
                tmr=0
                if key[K_ESCAPE]==True:
                    idx=11
                    tmr=0
                    pygame.mixer.music.play(-1)
            else:
                idx=11
        
        elif idx==15:
            if pl_lv>=2:
                window.fill(BLACK)    
                window.blit(img_kyositu,[0,0])
                window.blit(img_sakatoku,[380,130])
                pygame.draw.rect(window,BLACK,[0,300,941,300])        
                time_remain=time_remain-1
                if q_num >= 5:#ここ戻す
                    if clr_num3==0:  
                        if current_point>=60:                   
                            pl_lv=pl_lv+1
                            clr_num3=clr_num3+1
                        idx=16
                        tmr=0
                        fl_plv=open("savedata/plv.txt","w")
                        fl_plv.write(str(pl_lv))
                        fl_plv.close()
                        fl_clrnum3=open("savedata/clrnum3.txt","w")
                        fl_clrnum3.write(str(clr_num3))
                        fl_clrnum3.close()
                    else:
                        idx=17
                        tmr=0
                else:
                    draw_text(window, "次の単語を入力:", font, WHITE, 20, 320)
                    draw_text(window, current_word2, font2, WHITE, 20, 360)
                    draw_text(window, "残り問題数: " + str(20-q_num), font2, WHITE, WIDTH - 370, 20)
                    draw_text(window, "持ち点: " + str(current_point)+"点", font2, WHITE, WIDTH - 370, 60)
                    draw_text(window, "残り時間: " + str(time_remain//FPS+1)+"秒", font2, WHITE, WIDTH - 220, 320)
                    draw_text(window,"Escで終了して戻る",font,WHITE,600,600)

                    if time_remain==0:
                        incorrect.play()
                        current_point=current_point-10
                        init_question(idx)
                   
                    text_judge(idx)

                    if len(words2[1][words_idx2])==ipt_len_af:
                        for i in range(ipt_len_af):
                            ans_check_txt=ans_check_txt+ipt_key_af[i]

                    if words2[1][words_idx2] == ans_check_txt:
                        correct.play()
                        init_question(idx)
                    else:
                        ans_check_txt=""

                draw_text(window, input_text, font, WHITE, 20, 400)
                tmr=0
                if key[K_ESCAPE]==True:
                    idx=11
                    tmr=0
                    pygame.mixer.music.play(-1)
            else:
                idx=11

        elif idx==16:  #表示の機能と変数の操作の機能は分けるべし。ここは表示だから基本的に変数への代入はしない 
            window.fill(BLACK)
            window.blit(img_bg,[0,0])
            window.blit(img_keiji,[100,50])
            draw_text(window, "終了！", font2, BLACK, 250, 200)
            draw_text(window, "得点: " + str(current_point), font, RED, 250, 240)
            draw_text(window,"スペースで戻る",font,BLACK,500,500)
            if current_point>=60:
                if tmr==1:
                    success.play()
                if game_lv==1:
                    draw_text(window,"Easyクリア!レベルアップ!",font,BLACK,250,290)
                    window.blit(img_miyake,[250-img_miyake.get_width()/2,600-img_miyake.get_height()])
                    draw_text(window,"やるじゃないか!どんどんレベルアップしていこう",font,BLACK,320,400)
                elif game_lv==2:
                    draw_text(window,"Normalクリア!レベルアップ!",font,BLACK,250,290)
                    window.blit(img_kametani,[250-img_kametani.get_width()/2,600-img_kametani.get_height()])
                    draw_text(window,"その調子よ!次はもっと難しくなるわ",font,BLACK,320,400)
                elif game_lv==3:
                    draw_text(window,"Hardクリア!全クリ!",font,BLACK,250,290)
                    window.blit(img_sakatoku,[250-img_sakatoku.get_width()/2,600-img_sakatoku.get_height()])
                    draw_text(window,"すごいぞ!これで将来タイピングで困ることはない",font,BLACK,320,400)
            else:
                if tmr==1:
                    sippai.play()
                draw_text(window,"不合格！",font,BLACK,250,260)
                if game_lv==1:
                    window.blit(img_miyake,[250-img_miyake.get_width()/2,600-img_miyake.get_height()])
                    draw_text(window,"大丈夫。焦らず慎重に練習すれば結果はついてくる",font,BLACK,320,400)
                elif game_lv==2:
                    window.blit(img_kametani,[250-img_kametani.get_width()/2,600-img_kametani.get_height()])
                    draw_text(window,"一気に上達はしない。コツコツ頑張るのよ",font,BLACK,320,400)
                elif game_lv==3:
                    window.blit(img_sakatoku,[250-img_sakatoku.get_width()/2,600-img_sakatoku.get_height()])
                    draw_text(window,"全クリは目前。もうひと踏ん張りだ",font,BLACK,320,400)
            if key[K_SPACE]==True:
                idx=11
                tmr=0
                pygame.mixer.music.play(-1)

        elif idx==17:
            window.fill(BLACK)
            window.blit(img_bg,[0,0])
            window.blit(img_keiji,[100,50])
            draw_text(window, "終了！", font, BLACK, 250, 200)
            draw_text(window, "得点: " + str(current_point), font, RED, 250, 240)
            draw_text(window,"スペースで戻る",font,BLACK,500,500)
            if current_point>=60:
                if tmr==1:
                    success.play()
                if game_lv==1:
                    draw_text(window,"Easyクリア!",font,BLACK,250,290)
                elif game_lv==2:
                    draw_text(window,"Normalクリア!",font,BLACK,250,290)
                elif game_lv==3:
                    draw_text(window,"Hardクリア!",font,BLACK,250,290)
            else:
                if tmr==1:
                    sippai.play()
                draw_text(window,"不合格！",font,BLACK,250,290)
                if game_lv==1:
                    window.blit(img_miyake,[250-img_miyake.get_width()/2,600-img_miyake.get_height()])
                    draw_text(window,"大丈夫。焦らず慎重に練習すれば結果はついてくる",font,BLACK,320,400)
                elif game_lv==2:
                    window.blit(img_kametani,[250-img_kametani.get_width()/2,600-img_kametani.get_height()])
                    draw_text(window,"一気に上達はしない。コツコツ頑張るのよ",font,BLACK,320,400)
                elif game_lv==3:
                    window.blit(img_sakatoku,[250-img_sakatoku.get_width()/2,600-img_sakatoku.get_height()])
                    draw_text(window,"全クリは目前。もうひと踏ん張りだ",font,BLACK,320,400)
            if key[K_SPACE]==True:
                idx=11
                tmr=0
                pygame.mixer.music.play(-1)

        elif idx==18:
            if trn_tlk_idx==0:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_yada,[380,90])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                traintxt1=font.render(" ヤダ先生「トレーニングモードへようこそ。",True,WHITE)
                window.blit(traintxt1,[50,480])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    trn_tlk_idx=1
                    tmr=0
            elif trn_tlk_idx==1:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_yada,[380,90])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                traintxt2=font.render("ヤダ先生「ここは、じっくり丁寧にタイピングの練習を繰り返して、",True,WHITE)
                window.blit(traintxt2,[50,480])
                traintxt3=font.render("正確なタイピングを体に染み込ませるためのモード。いわば基礎練習だ。」",True,WHITE)
                window.blit(traintxt3,[50,520])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    trn_tlk_idx=2
                    tmr=0
            elif trn_tlk_idx==2:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_yada,[380,90])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                traintxt4=font.render("ヤダ先生「ここでは制限時間も問題数の制限もない。",True,WHITE)
                window.blit(traintxt4,[50,480])
                traintxt5=font.render("手元を見ないことと、手首を固定し、決まった指でキーを押すことを意識しながら",True,WHITE)
                window.blit(traintxt5,[50,520])
                traintxt6=font.render("じっくり練習をしてみてくれ」",True,WHITE)
                window.blit(traintxt6,[50,560])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    trn_tlk_idx=3
                    tmr=0
            elif trn_tlk_idx==3:
                window.fill(BLACK)
                window.blit(img_kyositu,[0,0])
                window.blit(img_yada,[380,90])
                pygame.draw.rect(window,BLACK,[0,430,941,243])
                window.blit(txt_basket,[150,20])
                traintxt7=font.render("ヤダ先生「それじゃあ早速、はじめ。」",True,WHITE)
                window.blit(traintxt7,[50,480])
                if tmr>60:
                    draw_text(window,"スペースキーでスキップ",font,WHITE,500,600)
                if key[K_SPACE]==True and tmr>30:
                    tlkskp_train_flg=1
                    fl_tlkskp_train=open("savedata/tlkskp_train.txt","w")
                    fl_tlkskp_train.write(str(tlkskp_train_flg))
                    fl_tlkskp_train.close()
                    idx=19
                    tmr=0
                
        elif idx==19:             
            window.fill(BLACK)    
            window.blit(img_kyositu,[0,0])
            window.blit(img_yada,[380,90])
            pygame.draw.rect(window,BLACK,[0,300,941,300])
            draw_text(window,"Escで終了して戻る",font,WHITE,600,600)
            draw_text(window, "次の単語を入力:", font, WHITE, 20, 320)
            draw_text(window, current_word2, font2, WHITE, 20, 360)
            
            text_judge(idx)
            if len(words2[1][words_idx2])==ipt_len_af:
                for i in range(ipt_len_af):
                    ans_check_txt=ans_check_txt+ipt_key_af[i]
            if words2[1][words_idx2] == ans_check_txt:
                correct.play()
                init_question(idx)
            else:
                ans_check_txt=""
            draw_text(window, input_text, font, WHITE, 20, 400)
            if key[K_ESCAPE]==True:
                idx=11
                tmr=0
                pygame.mixer.music.play(-1)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
