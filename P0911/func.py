# 학생 성적 프로그램

from Student import Student
from StuLog import StuLog

stus = StuLog()
s_no = 1

def s_mainPrint():
    print("-"*60)
    print("[학생 성적 프로그램]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("9. 학생 성적 저장")
    print("0. 프로그램 종료")
    print("-"*60)
    choice = int(input("번호 입력(0 입력 시 종료):"))
    print()
    return choice


def s_input():
    while True:
        print("[학생 성적 입력]")
        global s_no
        no = s_no
        name = input("{}번째 학생 이름 입력(0 입력 시 종료): ".format(no))
        if name == "0" : break
        kor = int(input("국어 점수 입력: "))
        eng = int(input("영어 점수 입력: "))
        math = int(input("수학 점수 입력: "))
        stus.add(Student(no, name, kor, eng, math))
        print("{}번째 {} 학생 성적 입력 완료".format(no, name))
    return s_no


def s_output():
    print("-"*60)
    print("[학생 성적 출력]")
    if len(stus.slist) == 0:
        print("입력된 성적 없음")
    else:
        stus.print()


def s_modi():
    print("[학생 성적 수정]")
    print("-"*60)
    name = input("수정할 학생 이름 입력: ")
    temp = 0
    for s in stus.slist:
        if s.name == name:
            print("{} 학생 성적 검색 완료".format(name))
            temp = 1
            break
    if temp == 0:
        print("{} 학생 기록 없음".format(name))
    elif temp == 1:
        print("[수정할 과목]")
        choice = int(input("1.국어 / 2.영어 / 3.수학 / 0.이전화면 : "))
        if choice == 1 :
            print(f"현재 국어 점수: {s.kor}")
            s.kor = int(input("변경할 국어 성적 입력: "))
            sub_nm = "국어"
        elif choice == 2 :
            print(f"현재 영어 점수: {s.eng}")
            s.eng = int(input("변경할 영어 성적 입력: "))
            sub_nm = "영어"
        elif choice == 3 :
            print(f"현재 수학 점수: {s.math}")
            s.math = int(input("변경할 수학 성적 입력: "))
            sub_nm = "수학"
        elif choice == 0 :
            print("이전화면으로 돌아감")
            return
        else :
            print("1~3 중 입력하시오")
        s.cal_sum()
        s.cal_avg()
        print(f"{name} 학생의 {sub_nm} 점수가 변경됨")
    print()


def readStu():
    global s_no
    with open("c:/aaa/stu3.txt", "r", encoding="utf-8") as f1:
        while True:
            line1 = f1.readline()
            line1 = line1.strip()
            if not line1 : break
            stu = line1.split(",")

            for i, s in enumerate(stu):
                if 0<=i<=1 : continue
                elif 2<=i<=5 : stu[i] = int(s.strip())
                elif i==6 : stu[i] = float(s.strip())
                elif i==7 : stu[i] = int(s.strip())
            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]))
            s_no = len(stus.slist)+1


def wrtStu():
    with open("c:/aaa/stu3.txt", "w", encoding="utf-8") as f1:
        while True:
            for s in stus.slist:
                str = s.s_str()
                f1.write(str + "\n")
            break
        print("성적 저장 완료")