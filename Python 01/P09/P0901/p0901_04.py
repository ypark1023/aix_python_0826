# 성적 프로그램 만들기
# print("[학생 성적 프로그램]")
# print("1. 학생 성적 입력")
# print("2. 학생 성적 출력")
# print("3. 학생 성적 수정")
# print("4. 학생 성적 삭제")
# print("5. 학생 성적 검색")
# print("0. 프로그램 종료")
# print("-"*40)

# choice = int(input("원하는 번호를 입력하시오: "))

stu_list = []

while True :
    print("[학생 성적 프로그램]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("5. 학생 성적 검색")
    print("0. 프로그램 종료")
    print("-"*40)

    choice = int(input("원하는 번호를 입력하시오: "))
    if choice == 1 :
        print("[학생 성적입력]")
        while True:
            no = len(stu_list)+1
            print("자동 번호: {}".format(no))
            name = input("이름 입력(종료하려면 0): ")
            if name == "0" : break
            kor = int(input("국어 점수 입력: "))
            eng = int(input("영어 점수 입력: "))
            math = int(input("수학 점수 입력: "))
            total = kor+eng+math
            avg = total/3
            stu_list.append([no, name, kor, eng, math, total, avg])
            print(name, " 학생 성적이 등록되었습니다")
            print()

    elif choice == 2 :
        print("[학생 성적 출력]")
        print("번호 \t 이름 \t 국어 \t 영어 \t 수학 \t 합계 \t 평균")
        print("-"*60)
        for s in stu_list :
            print("{} \t {} \t {} \t {} \t {} \t {} \t {:.2f}".format(*s))
        print("입력된 학생 성적은 몇 개: {}".format(len(stu_list)))

    elif choice == 3 :
        print("[학생 성적 수정]")
    elif choice == 4 :
        print("[학생 성적 삭제]")
    elif choice == 5 :
        print("[학생 성적 검색]")



    else : 
        print("[프로그램 종료]")
        break

