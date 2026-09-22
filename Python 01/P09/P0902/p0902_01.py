# # 복습하기

# # arr = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]

# arr1 = [1,2,3,4,5,6,7,8,9]
# arr2 = []

# for i in range(0,len(arr1),3):
#     arr2.append(arr1[i:i+3])

# print(arr2) # 결과값은 [[1, 2, 3], [4, 5, 6], [7, 8, 9]] - 2차원 리스트



# # 문자열을 6자리씩 끊어서 리스트로 저장

# aa = "abcdefabcdefabcdefabcdefabcdef"
# aa2 = []

# for a in range(0,len(aa),6):
#     aa2.append(aa[a:a+6])

# print(aa2) # 결과값은 ['abcdef', 'abcdef', 'abcdef', 'abcdef', 'abcdef']




# # 랜덤 리스트 만들기

# import random
# alist = list(range(1,26))
# random.shuffle(alist)
# alist2 = []

# for i in range(0,len(alist),5) :
#     alist2.append(alist[i:i+5])

# print(alist2)
# # 결과값은 [[19, 23, 7, 25, 6], [22, 10, 2, 9, 14], 
# # [11, 24, 17, 13, 18], [12, 20, 8, 3, 15], [21, 4, 16, 5, 1]]
# # 숫자 랜덤하게 돌아감



# # 빙고 만들기

# import random
# alist = list(range(1,26))
# random.shuffle(alist)
# alist2 = []

# for i in range(0,len(alist)):
#     alist2.append(i)
#     if (i+1)%5 != 0 :
#         print(alist[i], end="\t")
#     else : 
#         print(alist[i])




# 학생 성적 만들기
stu = [
    # {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100},
    # {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100},
    # {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100},
]

c_no = 1

while True : 
    print("[학생 성적 프로그램]")
    print("-"*40)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("0. 프로그램 종료")
    print("-"*40)

    choice = int(input("원하는 번호 입력: "))
    if choice == 1 :
        print()
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

