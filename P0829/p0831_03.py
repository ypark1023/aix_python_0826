# # 예제 : enumerate
# a_list = ["딸기", "바나나", "사과"]
# for i in range(len(a_list)) :
#     print(i,":", a_list[i])

# # 결과값
# # 0 : 딸기
# # 1 : 바나나
# # 2 : 사과


# for i, value in enumerate(a_list):
#     print("{} : {}".format(i, value))

# # 결과값 동일
# # 0 : 딸기
# # 1 : 바나나
# # 2 : 사과




# alist = []
# print(len(alist)) # 결과값은 0

# blist = [0,0,0]
# print(len(blist)) # 결과값은 3

# clist = [0]
# print(len(clist)*10) # 결과값은 10

# dlist = list(range(10))
# print(len(dlist)) # 결과값은 10

# elist = [i for i in range(10)]
# print(elist) # 결과값은 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - 이런 것을 '리스트 내포'라고 함


# elist2 = [i*2 for i in range(10)]
# print(elist)

# # # 결과값은 두 번 반복되는 결과
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
