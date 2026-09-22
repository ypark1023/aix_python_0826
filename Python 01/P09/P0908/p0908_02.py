# 클래스 - 함수와 비교

color = ""
speed = 0

def Upspeed():
    global speed
    speed += 10

def Downspeed():
    global speed
    speed -= 10

color = "white"
print("색상: ", color)
print("속도: ", speed)

Upspeed()
print("속도2: ", speed)



# 두번째 변수의 적용
color2 = ""
speed2 = 10

def Upspeed():
    global speed2
    speed2 += 10

def Downspeed():
    global speed2
    speed2 -= 10

color2 = "blue"
print("색상: ", color2)
print("속도: ", speed2)

Downspeed()
print("속도2: ", speed2)

Downspeed()
print("속도2: ", speed2)
