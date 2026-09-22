# 함수 예제

import random

def main_print() :
    print("1. 랜덤 숫자 5개 가져오기")
    print("2. 랜덤 숫자 3개 가져오기")
    print("3. 랜덤 숫자 1개 가져오기")
    choice = int(input("원하는 번호 입력: "))
    return choice

def ran_num(choice) :
    if choice == 1 :
        result = random.sample(range(1,101), 5)
    elif choice == 2 :
        result = random.sample(range(1,101), 3)
    elif choice == 3 :
        result = random.sample(range(1,101), 1)
    else :
        result = print("1,2,3 중 입력")
    return result


while True :
    choice = main_print()
    result = ran_num(choice)
    print("결과: ", result)


