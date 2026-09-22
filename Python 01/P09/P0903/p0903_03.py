
def cal1():
    for i in range(2,10):
        for j in range(1,10):
            print("{}x{}={}".format(i, j, i*j), end = " ")


def cal2():
    no1 = int(input("숫자 입력1: "))
    no2 = int(input("숫자 입력2: "))
    str1 = input("기호 입력 +/-/*//: ")
    if str1 == "+" :
        print("결과값: ", no1 + no2)
    elif str1 == "-" :
        print("결과값: ",no1 - no2)
    elif str1 == "*" :
        print("결과값: ",no1 * no2)
    elif str1 == "/" :
        print("결과값: ",no1/no2)
    else : 
        print("기호 입력")

import random
def cal3():
    mynum = int(input("1~45 번호 입력:"))
    lotto = random.randint(1,46)
    if mynum == lotto :
        print("입력: {}, 당첨번호: {}, 당첨!".format(mynum, lotto))
    else :
        print("입력: {}, 당첨번호: {}, 꽝!".format(mynum, lotto))


while True :
    print("1. 구구단 출력")
    print("2. 두 수를 입력받아 사칙연산 값 출력")
    print("3. 1~45까지 로또 당첨")
    choice = int(input("원하는 번호 입력: "))
    if choice == 1 :
        cal1()
    elif choice == 2 :
        cal2()
    elif choice == 3 :
        cal3()
    print()

