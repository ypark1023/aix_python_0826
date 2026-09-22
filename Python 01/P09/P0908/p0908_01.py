# 클래스 이해하기
# 변수와 함수가 모두 포함됨

# class Car :
#     color = ""
#     speed = 0
#     tire = 0
#     door = 0

#     def Upspeed(self):
#         self.speed += 10
#     def Downspeed(self):
#         self.speed -= 10


# # 클래스 1개 생성
# # c = Car()
# # c2 = Car()
# # # c2.Upspeed()

# # c.color = "white"               # 객체 생성
# # print("색상: ", c.color)        # 결과값은 / 색상:  white
# # print("속도: ", c.speed)        # 결과값은 / 속도:  0

# # c.Upspeed() 
# # print("속도2: ", c.speed)       # 결과값은 / 속도: 10


# # c.speed = 10
# # c.Upspeed() 
# # print("속도3: ", c.speed)       # 결과값은 / 속도: 20

# c1 = Car()
# c1.color = "white"
# c1.Upspeed()
# print("c1 색상: ", c1.color)
# print("c1 속도: ", c1.speed)

# c2 = Car()
# c2.color = "blue"
# c2.speed = 10
# c2.Upspeed()
# print("c2 색상: ", c2.color)
# print("c2 속도: ", c2.speed)

# c3 = Car()
# c3.color = "red"
# c3.speed = 100
# c3.Downspeed()
# print("c3 색상: ", c3.color)
# print("c3 속도: ", c3.speed)

# # 결과값은
# # c1 색상:  white
# # c1 속도:  10
# # c2 색상:  blue
# # c2 속도:  20
# # c3 색상:  red
# # c3 속도:  90


##################################################
# 생성함수의 활용, 생성자

class Car :
    color = ""
    speed = 0
    tire = 0
    door = 0

    # 생성자 - 클래스 선언될 때 자동으로 실행되는 함수
    def __init__(self, color, speed, tire, door):
        self.color = color
        self.speed = speed
        self.tire = tire
        self.door = door

    def Upspeed(self):
        self.speed += 10
    def Downspeed(self):
        self.speed -= 10


c1 = Car("white", 100, 4, 5)
c2 = Car("blue", 150, 6, 7)
c3 = Car("red", 120, 3, 5)

print(c1.color, c1.speed)
print(c2.color, c2.speed)
print(c3.color, c2.speed)

# 결과값은
# white 100
# blue 150
# red 150