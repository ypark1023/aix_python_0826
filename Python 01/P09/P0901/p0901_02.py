# 리스트 만들기

# num_arr = list(range(1,10))
# print(num_arr)
# # 결과값은 [1, 2, 3, 4, 5, 6, 7, 8, 9]


# all_arr = []
# for i in range(0,9,3) :
#     # print(i)
#     all_arr.append(num_arr[i:i+3])
# print(all_arr)
# # 결과값은 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



stu_list = [
    [1,"홍길동",100,100,100,300,100.0],
    [2,"유관순",100,100,100,300,100.0],
    [3,"이순신",100,100,100,300,100.0],
]

# stu_list = []
# stu_list.append([1, "홍길동", 100, 100, 100, 300, 100.0])
# stu_list.append([2, "유관순", 100, 100, 100, 300, 100.0])
# stu_list.append([3, "이순신", 100, 100, 100, 300, 100.0])


# # for문 이용하기
# stu_list = []

# for i in range(3):
#     no = input("번호 입력: ")
#     name = input("이름 입력: ")
#     kor = int(input("국어 점수 입력: "))
#     eng = int(input("영어 점수 입력: "))
#     math = int(input("수학 점수 입력: "))
#     total = kor+eng+math
#     avg = total/3
#     stu_list.append([no, name, kor, eng, math, total, avg])

# print(stu_list)



# # while문 이용하기
stu_list = []

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

print("번호 \t 이름 \t 국어 \t 영어 \t 수학 \t 합계 \t 평균")
print("-"*60)

for s in stu_list :
    print("{} \t {} \t {} \t {} \t {} \t {} \t {}".format(*s))

# print(stu_list)
print("입력된 학생 성적은 몇 개: {}".format(len(stu_list)))