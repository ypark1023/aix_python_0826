# # 영어 퀴즈 만들기

# engs = {
#     "car":["자동차","차"],
#     "color":["색깔","색상","색"],
#     "pig":"돼지",
#     "love":"사랑",
#     "phone":"전화기"
# }

# for k, v in engs.items() :
#     # print(k, ":", v)
#     print(k, "은(는) 한국어로 무엇?")
#     answer = input("답: ")
#     if answer == v :
#         print("정답")
#     else :
#         print("오답")
    



# # 리스트 내포
# alist = [i for i in range(1, 11)]
# print(alist)      # 결과값은 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# blist = list(range(1, 11))
# print(blist)      #결과값은 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# clist = [0]*10
# print(clist)        # 결과값은 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



# 리스트 안에 조건식
alist = list(range(1,21))
nlist = []
for a in alist :
    if a%3 == 0 :
        nlist.append(a)
    else :
        pass
print(nlist)    # 결과값은 [3, 6, 9, 12, 15, 18]

# 위와 동일한 결과값을 낼 수 있음
blist = [b for b in range(1,21) if b%3==0]
print(blist)        # 결과값은 [3, 6, 9, 12, 15, 18]