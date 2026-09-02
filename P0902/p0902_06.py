# 함수는 프로그램 간결화 위해
# def print_a() :
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")


# print_a()



def main_print():
    print("[학생 성적 프로그램]")
    print("-"*40)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("0. 프로그램 종료")
    print("-"*40)

def stu_input():
    print()
    c_no = 1
    while True :
        print("[학생 성적 입력]")
        no = c_no
        name = input("학생 이름 입력(0 입력 시 종료): ")
        if name == "0" : break
        kor = int(input("국어 점수 입력: "))
        eng = int(input("영어 점수 입력: "))
        math = int(input("수학 점수 입력: "))
        total = kor + eng + math
        avg = total/3
        stu.append(
            {"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg}
        )
        print(name, "학생 이름이 입력됐습니다")
        c_no += 1
        print()



c_no = 1

while True : 
    main_print()
    choice = int(input("원하는 번호 입력: "))
    if choice == 1 :
        stu_input()
    elif choice == 2 :
        print()
        print("[학생 성적 출력]")
        print("-"*40)
        print("번호 \t 이름 \t 국어 \t 영어 \t 수학 \t 합계 \t 평균")
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
            print()
    elif choice == 0 :
        print("[프로그램 종료]")
        break
    else :
        print()

