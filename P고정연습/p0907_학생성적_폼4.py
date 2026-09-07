# 학생 성적 프로그램 만들기
from p_StuM import *

readStu()

while True :
    choice = s_mainPrint()
    if choice == 1 :
        s_input()
    elif choice == 2 :
        s_output()
    elif choice == 3 :
        s_modi()
    elif 4 <= choice <= 8 :
        pass
    elif choice == 9 :
        wrtStu()
    elif choice == 0 :
        print("[프로그램 종료]")
        break
    else :
        print("0~9 중 입력하시오")

