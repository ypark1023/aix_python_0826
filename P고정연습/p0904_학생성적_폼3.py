# 학생 성적 만들기 함수

title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균"]
k_title = ["no", "name", "kor", "eng", "math", "total", "avg"]
stu = []

# 파일 불러오기
file0 = open("C:/aaa/test2.txt", "r", encoding="utf-8")
while True :
    line1 = file0.readline()
    line1 = line1.strip()
    if not line1 : break
    arr = line1.split(",")
    for i, a in enumerate(arr) :
        if 2 <= i <= 5 :
            arr[i] = int(a)
        elif i == 6 :
            arr[i] = float(a)
    stu.append({"no":arr[0], "name":arr[1], "kor":arr[2], "eng":arr[3], "math":arr[4], "total":arr[5], "avg":arr[6]})
    # print(arr)
file0.close()


# 메인화면 함수 선언
def s_mainPrint():
    print("-"*50)
    print("[학생 성적 프로그램]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("0. 프로그램 종료")
    print("-"*50)
    choice = int(input("번호 입력: "))
    return choice

# 성적입력 함수 선언
def s_input():
    global s_no
    while True:
        print("-"*50)
        print("[학생 성적 입력]")
        no = s_no
        name = input("{}번째 학생 이름 입력(0 입력 시 종료): ".format(no))
        if name == "0" : break
        kor = int(input("국어 점수 입력: "))
        eng = int(input("영어 점수 입력: "))
        math = int(input("수학 점수 입력: "))
        total = kor+eng+math
        avg = total/3
        stu.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg})
        print("{} 학생 성적 입력 완료".format(name))
        s_no += 1
        s_output()
        print()
    return s_no

s_no = 1

# 성적출력 함수 선언
def s_output():
    print("-"*50)
    print("[학생 성적 출력]")
    print("-"*50)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*50)
    if len(stu) == 0 : 
        print("입력된 성적 없음")
    else :
        for s in stu :
            print(f"{s["no"]}\t{s["name"]}\t{s["kor"]}\t{s["eng"]}\t{s["math"]}\t{s["total"]}\t{s["avg"]:.2f}")
    print()

# 성적수정 함수 선언
def s_modi():
    print("[학생 성적 수정]")
    print("-"*50)
    name = input("성적 수정할 학생 이름: ")
    temp = 0
    for i, s in enumerate(stu) :
        if s["name"] == name : 
            print(f"{name} 학생 검색 완료")
            temp = 1
            break
    if temp == 0 :
        print(f"{name} 학생 없음")
    elif temp == 1 :
        print("[수정할 과목 선택]")
        print("1. 국어 / 2. 영어 / 3. 수학")
        choice1 = int(input("번호 입력: "))
        if 1 <= choice1 <= 3 :
            print("현재 {} 점수: {}".format(title[choice1+1], s[k_title[choice1+1]]))
            s[k_title[choice1+1]]= int(input("변경 {} 점수: ".format(title[choice1+1])))
            s["total"] = s["kor"]+s["eng"]+s["math"]
            s["avg"] = s["total"]/3
            print("{} 학생의 {} 점수가 {}점으로 변경됨".format(name, title[choice1+1], s[k_title[choice1+1]]))
        else :
            print("1~3 중 입력하시오")
        print()

# 성적삭제 함수 선언
def s_del():
    print("[학생 성적 삭제]")
    print("-"*50)
    name = input("성적 삭제할 학생 이름: ")
    temp = 0
    for i, s in enumerate(stu) :
        if s["name"] == name : 
            print(f"{name} 학생 검색 완료")
            temp = 1
            break
    if temp == 0 :
        print(f"{name} 학생 없음")
    elif temp == 1 :
        print("삭제하시겠습니까? 1:네 / 0: 아니오")


while True :
    choice = s_mainPrint()
    if choice == 1 :
        s_input()
    elif choice == 2 :
        s_output()
    elif choice == 3 :
        s_modi()
    elif choice == 4 :
        s_del()
    elif choice == 0 :
        print("[프로그램 종료]")
        break
    else :
        print("1~3 중 입력하시오")