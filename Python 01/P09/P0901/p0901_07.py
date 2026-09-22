# name_arr = ["홍길동","유관순","이순신","강감찬","김구"]


# # index
# name = input("이름 검색: ")
# print(name_arr.index(name))


# while True :
#     name = input("검색할 이름 입력: ")
#     if name in name_arr :
#         no = name_arr.index(name)
#         print(no, ":", name, " 학생이 검색됐습니다")
#         change = input("변경할 이름 입력: ")
#         name_arr[no] = change
#         print(name_arr)
#     else : 
#         print(name, " 이름이 없습니다")


# stu_list = ["홍길동","유관순","이순신","강감찬","김구"]

stu_list = [
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0],
]

while True :
    flag = 0            # 초기화
    name = input ("이름 검색: ")
    for i, stu in enumerate(stu_list) :
        if name in stu : 
            stu_index = stu.index(name)
            print("해당 이름 있음")
            flag = 1 
            break
    if flag == 0 :
        print("해당 이름 없음")