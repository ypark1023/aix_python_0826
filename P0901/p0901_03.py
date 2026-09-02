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
    print("{} \t {} \t {} \t {} \t {} \t {} \t {:.2f}".format(*s))

# print(stu_list)
print("입력된 학생 성적은 몇 개: {}".format(len(stu_list)))




# 전개 연산자

arr = [1,2,3,4,5]
# print(arr)  # 결과값은 [1, 2, 3, 4, 5]
# print(*arr) # 결과값은 1 2 3 4 5 - 리스트에서 꺼내서 결과값은 내줌

# arr2 = []
# arr2 = arr
# print(arr2) # 결과값은 [1, 2, 3, 4, 5]

# arr[2] = 1000
# print(arr)  # 결과값은 [1, 2, 1000, 4, 5]
# print(arr2)  # 결과값은 [1, 2, 1000, 4, 5]

# arr3 = [*arr]   # 이런 형태를 '깊은 복사'라고 함
# arr[2] = 1000
# print(arr)  # 결과값은 [1, 2, 1000, 4, 5]
# print(arr3)  # 결과값은 [1, 2, 3, 4, 5]
