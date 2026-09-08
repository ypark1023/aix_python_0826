# 학생 성적 프로그램 모듈

from p0908_stu_class3 import Student
from p0908_stu_class2 import StuLog

stus = StuLog()
stuList = []
# title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
# s_title = ["no", "name", "kor", "eng", "math", "total", "avg", "rank"]
s_no = 1

# 메인화면 함수 선언
def s_mainPrint():
    print("-"*50)
    print("[학생 성적 프로그램]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("9. 학생 성적 저장")
    print("0. 프로그램 종료")
    print("-"*50)
    choice = int(input("번호 입력: "))
    print()
    return choice

# 성적입력 함수 선언
def s_input():
    print()
    global s_no
    while True:
        print(["학생 성적 입력"])
        no = s_no
        name = input("{}번째 학생 이름 입력(0 입력시 이전페이지로): ".format(no))
        if name == "0" : break
        kor = int(input("국어 점수 입력: "))
        eng = int(input("영어 점수 입력: "))
        math = int(input("수학 점수 입력: "))
        total = kor+eng+math
        avg = total / 3
        rank = 0
        stus.add(Student(no, name, kor, eng, math))
        # stuList.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg, "rank":rank})
        print("{}번 {} 학생 성적 입력 완료".format(no, name))
        # s_no += 1
        print()
    return s_no

# 성적출력 함수 선언 - 클래스 변경 완료
def s_output():
    stus.print()
    # print("-"*50)
    # if len(stuList) == 0 : 
    #     print("입력된 성적 없음")
    # else :
    #     for s in stuList :
    #         print(f"{s["no"]}\t{s["name"]}\t{s["kor"]}\t{s["eng"]}\t{s["math"]}\t{s["total"]}\t{s["avg"]:.2f}\t{s["rank"]}")
    print()

# 성적 수정 함수 선언
def s_modi():
    print()
    print(["학생 성적 수정"])
    print("-"*50)
    name = input("성적 수정할 학생 이름: ")
    temp = 0
    for s in stus.slist :
        if s.name == name :
            print(f"{name} 학생 검색 완료")
            temp = 1
            break
    if temp == 0 :
            print(f"{name} 학생 기록 없음")
    elif temp == 1 :
        print("[수정할 과목 선택]")
        print("1.국어 / 2.영어 / 3.수학 / 0. 이전화면")
        choice = int(input("숫자 입력: "))
        if choice == 1:
            print(f"현재 국어 점수: {s.kor}")
            s.kor = int(input("변경 국어 점수: "))
            sub_name = "국어"
        elif choice == 2:
            print(f"현재 영어 점수: {s.eng}")
            s.eng = int(input("변경 영어 점수: "))
            sub_name = "영어"
        elif choice == 3:
            print(f"현재 수학 점수: {s.math}")
            s.math = int(input("변경 수학 점수: "))
            sub_name = "수학"
        elif choice == 0 :
            print("이전화면으로 돌아감")
            return
        else:
            print("1~3 중 입력해야 합니다.")
        
        # 총점과 평균 재계산
        s.calc_sum()
        s.calc_avg()
        print(f"{name} 학생의 {sub_name} 점수가 변경됨")
    print()


# 학생 성적 파일 불러오기 함수 선언
def readStu():
    global s_no
    with open("c:/aaa/stu1.txt", "r", encoding="utf-8") as f1 :
        while True :
            line1 = f1.readline()
            line1 = line1.strip()
            if not line1 : break
            stu = line1.split(",")

            # no = int(stu[0].strip())
            # name = stu[1].strip()
            # kor = int(stu[2].strip())
            # eng = int(stu[3].strip())
            # math = int(stu[4].strip())
            
            # s_obj = Student(no, name, kor, eng, math)
            # s_obj.total = int(stu[5].strip())
            # s_obj.average = float(stu[6].strip())
            # s_obj.rank = int(stu[7].strip())
            
            # stus.add(s_obj)
            # # stuList.append(dict(zip(s_title, stu)))

            for i,s in enumerate(stu):
                if 0<=i<=1 : continue
                elif 2<=i<=5 : stu[i] = int(s.strip())
                elif i==6 : stu[i] = float(s.strip())
                elif i==7 : stu[i] = int(s.strip())
            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]))
            s_no = len(stus.slist)+1


# 학생 성적 파일 저장 함수 선언
def wrtStu():
    with open("c:/aaa/stu1.txt", "w", encoding="utf-8") as f1 :
        while True :
            for s in stus.slist :
                str = s.s_str()
                f1.write(str+"\n")
            break
        print("성적 파일 저장 완료")