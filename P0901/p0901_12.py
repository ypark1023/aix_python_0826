# 복습 시간


# # 구구단 만들기
# for i in range(2,10) :
#     for j in range(1,10):
#         print("{}x{}={}".format(i, j, i*j), end=" ")


# # 로또 만들기
# import random
# lotto = random.sample(range(1,46),6)

# i = 0
# mylist = []

# print("[1~45 중 6개 숫자 입력]")
# while i < 6 :
#     mynum = int(input("숫자 입력: "))
#     if mynum not in mylist :
#         mylist.append(mynum)
#         i = i+1
#     else : 
#         print("번호 있음")

# count = 0
# answer = []

# for i in mylist :
#     if i in lotto :
#         count = count+1
#         answer.append(i)


# print("로또 번호: {}".format(lotto))
# print("입력 번호: {}".format(mylist))
# print("맞춘 번호: {}".format(answer))
# print("맞춘 개수: {}".format(count))




# 학생 성적 리스트 만들기

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

    choice = int(input("원하는 번호 입력:"))
    if choice == 1 :
        print("[1. 학생 성적 입력]")
        while True :
            no = len(stu_list)+1
            print("자동 번호: {}".format(no))
            name = input("이름 입력(종료 시 0 입력): ")
            if name == "0" : break
            kor = int(input("국어 성적 입력: "))
            eng = int(input("영어 성적 입력: "))
            math = int(input("수학 성적 입력: "))
            total = kor+eng+math
            avg = total / 3
            stu_list.append([no, name, kor, eng, math, total, avg])
            print("학생 성적 입력 완료")
            print()

    elif choice == 2 :
        print("[2. 학생 성적 출력]")
        print("번호 \t 이름 \t 국어 \t 영어 \t 수학 \t 합계 \t 평균")
        print("-"*60)
        for s in stu_list :
            print("{} \t {} \t {} \t {} \t {} \t {} \t {:.2f}".format(*s))
        print("입력된 학생 성적은 몇 개: {}".format(len(stu_list)))

    elif choice == 3 :
        print("[3. 학색 성적 수정]")

    elif choice == 4 :
        print("[4. 학색 성적 삭제]")

    elif choice == 5 :
        print("[5. 학색 성적 검색]")

    else :
        print("프로그램 종료")
        break
