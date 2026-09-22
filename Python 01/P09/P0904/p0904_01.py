# 학생 성적 만들기 함수

title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균"]
k_title = ["no", "name", "kor", "eng", "math", "total", "avg"]
stu = []

# 메인화면 함수 선언
def s_mainPrint():
    print("[학생 성적 프로그램]")
    print("-"*40)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("0. 프로그램 종료")
    print("-"*40)
    choice = int(input("번호 입력: "))
    print()
    return choice

# 1.학생성적 입력 함수 선언
def s_input():
    global s_no
    while True:
        no = s_no
        print("[학생 성적 입력]")
        name = input("{}번째 이름 입력(0:이전화면 이동): ".format(no))
        if name == "0" : break
        kor = int(input("국어 점수 입력: "))
        eng = int(input("영어 점수 입력: "))
        math = int(input("수학 점수 입력: "))
        total = kor+eng+math
        avg = total/3
        # score = [0]*3
        # for i in range(3):
        #     score[i] = (input("{} 점수 입력: ".format(title[i+2])))
        stu.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg})
        print("{} 학생 성적 입력 완료".format(name))
        s_no += 1
        s_output()
        print()
    return s_no

s_no = 1

# 2.학생성적 출력 함수 선언
def s_output():
    print()
    print("[학생 성적 출력]")
    print("-"*40)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*40)
    if len(stu) == 0:
        print("입력된 성적 없음")
    else: 
        for s in stu :
            print(f"{s["no"]}\t{s["name"]}\t{s["kor"]}\t{s["eng"]}\t{s["math"]}\t{s["total"]}\t{s["avg"]:.2f}")
    print()


#3. 학생성정 수정 함수 순언
def s_modi():
    print()
    print("[학생 성적 수정]")
    name = input("찾는 학생 이름 입력: ")
    temp = 0
    for i, s in enumerate(stu) : 
        if s["name"] == name :
            print(f"{name} 학생 검색 완료")
            temp = 1
            break
    if temp == 0 :
        print(f"{name} 학생 없음")
    elif temp == 1 :
        print("[과목 수정 선택]")
        print("1.국어 / 2.영어 / 3.수학")
        choice = int(input("번호 입력: "))
        print(f"현재 {title[choice+1]} 점수: {s[k_title[choice+1]]}")
        s[k_title[choice+1]] = int(input(f"변경 {title[choice+1]} 점수: "))
        s['total'] = s['kor']+s['eng']+s['math']
        s['avg'] = s['total']/3
        print(f"{s[k_title[choice+1]]}점으로 {title[choice+1]} 점수 변경됨")
        print()


while True :
    choice = s_mainPrint()
    if choice == 1 :
        s_input()
    elif choice == 2 :
        s_output()
    elif choice == 3 :
        s_modi()
    elif choice == 0:
        print("[프로그램 종료]")
        break
    else :
        print("다른 번호 입력하시오")
