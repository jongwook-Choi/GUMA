init:

    ### 배경 ###
    image bg room0 = "images/배경/신당0.png"
    image bg room1 = "images/배경/신당1.png"

    ### 시나리오1 ###
    image guest1_1 = "images/시나리오1/여자1.png"
    image guest1_2 = "images/시나리오1/여자2.png"
    image guest1_3 = "images/시나리오1/여자3.png"

    image ghost1_1 = "images/시나리오1/태자귀1.png"
    image ghost1_2 = "images/시나리오1/태자귀2.png"

    define bunker_1 = 0 

    ### 시나리오2 ###
    image guest2_1_1  = "images/시나리오2/부모(모)1.png"
    image guest2_1_2  = "images/시나리오2/부모(모)2.png"
    image guest2_1_3  = "images/시나리오2/부모(모)3.png"

    image guest2_2_1  = "images/시나리오2/여자아이1.png"
    image guest2_2_2  = "images/시나리오2/여자아이2.png"
    image guest2_2_3  = "images/시나리오2/여자아이3.png"

    define bunker_2 = 0

    ### 시나리오3 ###
    image guest3_1 = "images/시나리오3/남자1.png"
    image guest3_2 = "images/시나리오3/남자2.png"
    image guest3_3 = "images/시나리오3/남자3.png"

    define bunker_3 = 0


    ### 캐릭터 정의 ###
    define player = Character('무당', color="33d4ff")
    define guest1 = Character('이혜진', color="#c8ffc8")
    define guest2_1 = Character('김희연')
    define guest2_2 = Character('박진아')
    define guest3 = Character("김원길")



# 여기에서부터 게임이 시작합니다.
label start:

    pass

label chapter1:

    play music "audio/ofeliasdream.mp3"
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
    scene bg room0

    show guest1_1 with fade

    guest1 "안녕하세요"
    guest1 "고민이 있어 찾아왔습니다."

    # 이름 색 변경 가능
    guest1 "신당이 굉장히 외진곳에 있군요.."


    player "어서오게.."
    player "근심이 많아 보이는구만.."

    hide guest1_1

    show guest1_2
    show ghost1_1 with fade

    menu:
        "혹시 아이의 생명을 다루는 직업을 가지고 있나?":
            $ bunker_1 = 0
            pass
        "혹시 아이를 죽인적이 있나?":
            $ bunker_1 = 1
            pass

    # hide guest1_2 with fade

label result1:
    if bunker_1 == 0:
        show ghost1_2 with fade
        "네.. 사실 제가 산부인과 의사에요.."  
    elif bunker_1 == 1:
        hide guest1_2
        hide ghost1_1
        show guest1_1 with fade
        "무슨 헛소리를 하시는거죠!"

    hide guest1_1
    hide guest1_2
    hide ghost1_1
    hide ghost1_2
    
label chpater2:

    show guest2_1_1 
    show guest2_2_1

    guest2_1 "안녕하세요." 
    guest2_2 "..."


    menu:
        "김희연에게 말을 건낸다.":
            $ bunker_2 = 0
        "박진아에게 말을 건넨다.":
            $ bunker_2 = 1


label result2:
    if bunker_2 == 0:
        hide guest2_1_1
        show guest2_1_2 with fade
        guest2_1 "우리아이가 요즘 문제가 많아서요.."
        pass
    elif bunker_2 == 1:
        hide guest2_2_1
        show guest2_2_2 with fade
        guest2_2 "네? 저한테 말씀하시는 건가요?"
        pass

    hide guest2_1_1 
    hide guest2_2_1

    hide guest2_1_2
    hide guest2_2_2
    pass

label chapter3:
    show guest3_1 with fade
    guest3 "안녕하십니까.."

    menu:
        "자네같은 손님은 받지 않네 돌아가게!":
            $ bunker_3 = 0
        "자네 살인을 저질렀나?":
            $ bunker_3 = 1

label result3:
    if bunker_3 == 0:
        hide guest3
        show guest3_2 with fade
        guest3 "아니 왜그러십니까.. 제 말좀 들어주세요..."
    elif bunker_3 == 1:
        hide guest3
        show guest3_3 with fade
        guest3 "...?"

    stop music
    