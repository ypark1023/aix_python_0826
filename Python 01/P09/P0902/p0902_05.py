# # 함수

# # 함수 기본구조
# def print00():
#     print("함수를 호출한다")

# print00()
# print00()       # 반복하는 수만큼 출력됨


# # 함수 작동
# def cal():  # 함수 정의
#     num1 = int(input("숫자 입력1: "))
#     num2 = int(input("숫자 입력2: "))

#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)

# cal()       # 함수 호출



# 예제 

def stu_print():
    for s in stu :
        print("{},{},{},{},{}".format(*s))

stu = [
    [1,"홍길동",100,100,100],
    [2,"유관순",80,100,90],
    [3,"이순신",90,80,100]
]

while True:
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 검색")
    choice = int(input("번호 입력: "))
    if choice == 1 :
        name = input("이름 입력: ")
        stu_print()
    elif choice == 2 :
        print("번호 \t 이름 \t 국어 \t 영어 \t 수학 \t 합계 \t 평균")
        stu_print()
    else: 
        name = input("이름 입력: ")
        stu_print()