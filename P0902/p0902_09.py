def main_print():
    print("1. 1~45까지 숫자 맞추기 프로그램")
    print("2. 구구단 출력 프로그램")
    print("3. 두 수 ~ +/-/*// 결과 출력 프로그램")
    print("0. 프로그램 종료")
    print()


import random
def number_func() :
    mynum = int(input("1~45 숫자 입력: "))
    rannum = random.randint(1,46)
    if mynum == rannum :
        print("입력 숫자: {}, 랜덤 숫자: {} / 당첨!".format(mynum, rannum))
    else :
        print("입력 숫자: {}, 랜덤 숫자: {} / 꽝!".format(mynum, rannum))

def gugu_func() :
    for i in range(2,10) :
        for j in range(1,10):
            print("{}x{}={}".format(i, j, i*j), end = " ")

def cal_func() :
    num1 = int(input("숫자 입력1: "))
    num2 = int(input("숫자 입력2: "))
    str1 = input("+/-/*// 중 입력: ")
    if str1 == "+" :
        result = num1 + num2
    elif str1 == "-" :
        result = num1 - num2 
    elif str1 == "*" :
        result = num1 * num2 
    elif str1 == "/" :
        result = num1 / num2 
    print("값: ", result)



while True :
    main_print()
    choice = int(input("번호 입력: "))
    if choice == 1 :
        result = number_func()
    elif choice == 2 :
        result = gugu_func()
    elif choice == 3 :
        result = cal_func()
    elif choice == 0 :
        print("[프로그램 종료]")
        break
    else :
        print("1~3 중 번호 입력")
    print()