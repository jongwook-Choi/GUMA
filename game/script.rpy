init:

    ### 배경 ###
    image bg room0 = "images/배경/신당0.png"
    image bg room1 = "images/배경/신당1.png"

    ### 시나리오1 ###
    image guest1_1 = "images/시나리오1/여자_평범.png" # 평범
    image guest1_2 = "images/시나리오1/여자_우울.png" # 우울
    image guest1_3 = "images/시나리오1/여자_공포.png" # 공포
    image guest1_4 = "images/시나리오1/여자_놀람.png" # 놀람
    image guest1_5 = "images/시나리오1/여자_울컥.png" # 울컥
    image guest1_6 = "images/시나리오1/여자_불쾌.png" # 불쾌
    image guest1_6 = "images/시나리오1/여자_울먹.png" # 울먹

    image ghost1_1 = "images/시나리오1/태자귀1.png" # 오른쪽 태자귀
    image ghost1_2 = "images/시나리오1/태자귀2.png" # 왼쪽 아래 태자귀

    ### 시나리오2 ###
    image guest2_1_1  = "images/시나리오2/부모평범.png"
    image guest2_1_2  = "images/시나리오2/부모놀람.png"
    image guest2_1_3  = "images/시나리오2/부모분노_수정.png"
    image guest2_1_4  = "images/시나리오2/부모어색.png"
    image guest2_1_5  = "images/시나리오2/부모울음.png"
    image guest2_1_6  = "images/시나리오2/부모귀신.png"

    image guest2_2_1  = "images/시나리오2/여자평범.png"
    image guest2_2_2  = "images/시나리오2/여자우울_수정.png"
    image guest2_2_3  = "images/시나리오2/여자놀람.png"
    image guest2_2_4  = "images/시나리오2/여자귀신.png"
    image guest2_2_5  = "images/시나리오2/여자귀신우울_수정.png"

    image ghost2_2_1_1 = "images/시나리오2/아이여자귀신.png"
    image ghost2_2_1_2 = "images/시나리오2/아이언니귀신.png"
    image ghost2_2_1_3 = "images/시나리오2/아이언니귀신2.png"
    image ghost2_2_1_4 = "images/시나리오2/아이기타귀신.png"


    ### 시나리오3 ###
    image guest3_1 = "images/시나리오3/남자평범.png"
    image guest3_2 = "images/시나리오3/남자울적.png"
    image guest3_3 = "images/시나리오3/남자기쁨.png"
    image guest3_4 = "images/시나리오3/남자변신.png"
    image guest3_5 = "images/시나리오3/남자곤란_수정.png"
    image guest3_6 = "images/시나리오3/남자얼굴변형.png"
    image guest3_7 = "images/시나리오3/남자변신살해.png"

    image ghost3_1 = 'images/시나리오3/여자귀신1.png'
    image ghost3_1 = 'images/시나리오3/여자귀신2.png'
    image ghost3_1 = 'images/시나리오3/여자귀신3.png'

    ### 캐릭터 정의 ###
    define player = Character('무당', color="33d4ff")
    define guest1 = Character('이혜진', color="#c8ffc8")
    define guest1_2 = Character('빙의당한_이혜진', color="#c8ffc8")

    define guest2_1 = Character('김희연')
    define guest2_2 = Character('박진아')
    define guest3 = Character("김원길")



   ###분기 정리 ###

    define bunker_1 = 0 
    define bunker_2 = 0
    define bunker_3 = 0
    define bunker_4 = 0
    define bunker_5 = 0
    define bunker_6 = 0

    define end_1 = 0
    define end_2 = 0
    define end_3 = 0


    define fade = Fade(1.5, 1.0, 1.5)


# 여기에서부터 게임이 시작합니다.
label start:

    pass

label chapter1:

    # play music "audio/ofeliasdream.mp3"
    # 배경 띄우기
    scene bg room1 with fade
    "때는 0000년 0월 0일 6살인 나는 물가에서 놀다 물에 빠지는 사고를 당했다"
    "바로 구조되기는 했지만 내가 너무 어렸기 때문이었을까, 나는 잠시 죽어있었다고 한다."
    "그 후 부터 였다. 귓가에 물소리가 들리고 주변 사람들에게 이유없는 불행이 닥치기 시작했다."
    "나 또한 알 수 없는 고열에 시달리며 보이면 안되는 것들이 보이기 시작했다."
    "그런 나를 걱정한 부모님들은 나를 데리고 병원을 전전했지만..."
    "병원은 나의 병명을 알아내지 못했다."
    "결국 이런 나를 더 이상 두고 볼 수 없었던 부모님은 나를 무당에게로 데려갔고.."
    "당연한 것처럼, 나는 신을 받아들이는 무당이 되었다."

    # scene bg room1
    # scene bg room0

    play sound "sound/open_door.mp3"
    pause .5
    scene bg room0
    show guest1_2 with fade
    

    guest1 "안녕하세요"
    guest1 "고민이 있어 찾아왔습니다."

    # 이름 색 변경 가능
    # guest1 "신당이 굉장히 외진곳에 있군요.."

    player "어서오게.."
    player "근심이 많아 보이는구만.."

    show ghost1_1 with fade

    menu:
        "너, 산부인과에서 일하지?":
            $ bunker_1 = 0
            pass
        "너, 유치원에서 일하지?":
            $ bunker_1 = 1
            pass

    # hide guest1_1 with fade

label chpater1:
    if bunker_1 == 0:
        hide guest1_2
        hide ghost1_1

        show guest1_1
        show ghost1_1 
        show ghost1_2 

        guest1 "네.. 사실 제가 산부인과 의사에요.."  

        player "그래, 딱 봐도 무슨 일로 왔는지 알겠네. 태자귀를 둘이나 달고 말이야. 어디 한 번 니 입으로 말해봐"

        guest1 "사실 아이를 가지고 싶은데, 아이가 생기지 않아요. 남편이랑 오랫동안 노력도 해보고 좋다는 음식, 약 ... 다 해봤는데"  
        guest1 "아이가 들어서기는커녕 몸이 점점 나빠져만 가는 것 같은 기분이 들어요. 이런 일이 오래되다 보니 부부사이도 소원해져버렸어요."
        guest1 "제발, 어떻게 하면 아이를 가질 수 있을까요?"

        menu:
            "너, 네 아이를 죽인 적 있지":
                $ end_1 = 1
                pass
            "너, 남의 아이를 죽인 적 있지":
                $ bunker_2 = 1
                pass
            
        if bunker_2 == 1:
            guest1 '...'

            player '계속 입다물고 있을거야?'
            
            guest1 '사실... 전 낙태수술을 집도한 적이 있어요.'
            
            player '한 두 번이 아니었겠지.'

            guest1 '산부인과 의사로 일하다보면 얼마나 많은 사람들이 찾아오는 줄 아세요?'
            guest1 '저는 저만의  선이 있었다고요. '
            guest1 '물론, 제가 한 일이 마냥 잘 했다는 건 아니에요. 하지만, 하지만…!'

            player '…그래서, 너한테 붙은 그 귀신들, 뗄거야 말거야.'
            player '네 손으로 뗀 목숨들이 너한테 붙어있어. 그것 때문에 니가 아이를 가지지 못하고 있는거야.'

            guest1 '저는...'

            menu:
                '이 일을 그만둘 순 없어요. 누군가에겐 꼭 필요한 일이에요.':
                    $ bunker_3 = 1
                '이 일을 그만둬야 아이를 가질 수 있는 거라면…':
                    $ bunker_4 = 1

        if bunker_3 == 1:
            guest1_2 '…엄.. 마, 엄마… 어디있어… '

            player '이녀석들! 왜 여기서 네 엄마를 찾아! 썩 나오지 못 해!'

            guest1_2 '엄마… 쓰다듬어 줘… '

            player '이녀석들이 그래도…!'

            guest1_2 '엄마, 엄마… 이름, 불러줘… 엄마… '

            player '...'

            guest1_2 '… …싸우지 마… 무서워…'

            player '… 너희 둘 다 좋은 곳으로 보내줄 테니 얼른 나오거라!'

            guest1_2 '… 왜 나만? 왜 우리들은 태어나지 못 했어? '
            guest1_2 '…나는 이해 못 해. 나한텐 이유같은거 필요 없어.'

            #슬픈 표정의 태자귀들이 천천히 사라지는 장면 추가

            player '...'

            # 빙의가 풀린 이혜진이 정신 차림, 평범한 표정 추가

            guest1 '…? 응…? 뭐죠. 잠깐 정신을 잃었던 것 같은데…'

            player '가 봐.'

            # 당황환 표정

            guest1 '네?'

            player '…조만간 아이를 가질 수 있을 거야. '

            # 놀란 표정

            guest1 '정말인가요?!'
            
            player '그래. 쌍둥이를 가질거야.'

            hide ghost1_1 with dissolve
            hide ghost1_2 with dissolve
            
            hide guest1_1 with fade

            jump chpater2

        elif bunker_4 == 1:
            player '…그래 네 뜻이 그렇다면 네게 붙은 태자귀들의 천도를 도와주도록하지.'

            guest1 '(울컥한표정) … 감사합니다'

            player '됐어. 어떤 선택을 하든 너의 선택이란 것만 기억해.'

            #(울기 시작하는 태자귀들. 시끄러운 울음소리가 신당을 채우기 시작한다.)

            guest1 '(당황한표정) 꺄악…! 이, 이게 무슨 소리죠?!'

            player '뭐긴 뭐야. 네가 선택한 결과지.'

            guest1 '(당황한표정) …네? 제가 선택한 거라구요…?'

            player '그래. 잘 듣고 기억해 둬.'

            # (딸랑이는 방울소리들이 들리면서 태자귀들의 울음소리가 점점 옅어진다.)

            hide guest1_1
            hide ghost1_1 
            hide ghost1_2 

            jump chpater2           

label chpater2:
    pause 1
    play sound "sound/open_door.mp3"
    pause .5

    show guest2_1_1 
    show guest2_2_1 
    show ghost2_2_1_2

    menu:
        '(아이에게 말을 건다) 얘, 너 요즘 학교 생활에 문제있지?':    
            $ bunker_5 = 0
        '(어머니에게 말을 건다) 애가 아픈지 좀 됐지?':    
            $ bunker_5 = 1

    if bunker_5 == 0:
        hide guest2_2_1
        show guest2_2_2

        player '그래, 그럼 너 말고 누가있어?'

        guest2_2 '아, 저는… 그게…'

        guest2_1 '얘, 너는 애가 왜이렇게 답답하니? 무슨 문제가 있으면 있다고 말을 해야 할 거 아냐.'

        hide guest2_1_1
        show guest2_1_4

        guest2_1 '아, 얘가 긴장해서 그래요. 저희 딸은 학교에서 아무 문제도 없고 성실하게 잘 지내고 있는데 뭐가 문제겠어요.'
        guest2_1 '저희 딸만큼 조용한 애도 찾기 힘들거에요. 그런데 요즘 성적이 조금 떨어져서…'

        player '내가 너한테 물어봤어? 얘, 넌 너희 엄마 떼놓고 다시 와.'

    elif bunker_5 == 1:
        guest2_1 '어머, 어떻게 아셨어요?'
        guest2_1 '애가 어릴 때부터 몸이 약하긴 했는데 요즘따라 열도 계속 나고 헛것이 보인다고 하질않나…' 
        guest2_1 '병원에 가도 딱히 방도가 없더라구요. 그래서 혹시나하고 찾아와봤죠.'

        hide guest2_1_1
        show guest2_1_4

        guest2_1 '…그리고 그것 때문인지 요즘 성적이 좀 많이 떨어졌어요.'

        guest2_2 '… 헛것이 아니에요. 계속 어린 여자애가 내 옆에 붙어있다구요. '

        hide guest2_2_1
        show guest2_2_2

        guest2_2 '그리고 성적이 떨어진건…'

        hide guest2_1_4
        show guest2_1_3

        guest2_1 '어디서 말대꾸야.'

        hide guest2_1_3
        show guest2_1_4

        guest2_1 '저, 그래서… 저희 딸이 공부하는데 집중 할 수 있는 부적 같은 거라도 써주실 수 있는지 싶어서요.'
        
        player '지금 그게 문제가 아니야.'
        
        guest2_1 '네?'

        player '너희 딸 주변에 귀신들이 한가득이야. 이대로 두면 악귀들이 네 딸 몸 차지하려고 들러붙을거야. 특히 저기 붙어있는 어린여자애가 아주 독해.'

        hide guest2_2_2
        show guest2_2_3
        

        guest2_2 '네, 맞아요. 여자애 귀신이…'

        hide guest2_1_4
        show guest2_1_1

        guest2_1 '쓸데없는 말 하지 말래도.'

        player '굿 받을거야, 안받을거야?'

        menu:
            '굿을 받는다.':
            $ bunker_6 = 0:
















    




            







    