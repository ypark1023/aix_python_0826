# 리스트

# a_arr = [1,5,10,20,90,100,7,2]

# a_arr.sort()
# print(a_arr)
# # 결과값은 [1, 2, 5, 7, 10, 20, 90, 100]
# # 정렬되면 기존 리스트로 되돌릴 수 없음


# b_arr = [1,5,10,20,90,100,7,2]
# b_arr2 = [*b_arr]
# print(b_arr2)   # 결과값은 [1,5,10,20,90,100,7,2]
# b_arr2.sort()
# print(b_arr2)   # 결과값은 [1, 2, 5, 7, 10, 20, 90, 100] / b_arr 리스트는 변하지 않았음



# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# for number in numbers :
#     if number >=100 :
#         print("- 100 이상의 수: ", number)
# # 결과값은
# # - 100 이상의 수:  273
# # - 100 이상의 수:  103
# # - 100 이상의 수:  800



# # 2차원 리스트
# aa = list(range(1,13))
# print(aa)   # 1차원 리스트

# # 결과값은 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# a_arr = []
# for i in range(0,12,4) :
#     a_arr.append(aa[i:i+4])
# print(a_arr)

# # 결과값은 [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


# bb = list(range(1,26))
# for i in bb :
#     # print(i, end="\t")
#     if i%5 != 0 :
#         print(i, end="\t")
#     else : 
#         print(i)

# 결과값은
# 1       2       3       4       5
# 6       7       8       9       10
# 11      12      13      14      15
# 16      17      18      19      20
# 21      22      23      24      25



# 빙고 만들기
bb = list(range(1,26))
# print(bb, end =" ")

# i = index
# v = value

import random
random.shuffle(bb)

while True :
    print(" "*15, end="")
    print("[5x5 빙고 게임]")
    print("-"*40)
    for i, v in enumerate(bb) :
        if (i+1)%5 != 0 :
            print(v, end="\t") 
        else :
            print(v)
    print("-"*40)
    num = int(input("1~25 원하는 번호 입력: "))
    if num in bb :
        idx = bb.index(num)
        bb[idx] = "X"


