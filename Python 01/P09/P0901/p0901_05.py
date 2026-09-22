# a_arr = [0,0,0,0,0,0,0,0,0,0,0,0]
# for a in a_arr :
#     print(a, end=" ")

# # for문을 써서 리스트에 추가해도 계속 출력해낼 수 있음


# # 슬라이싱
# a_arr = [10,20,30,40,50,60,70,80,90,100]
# print(a_arr[2:5])   # 결과값 [30, 40, 50] 슬라이싱
# print(a_arr[::-1])  # 결과값은 [100, 90, 80, 70, 60, 50, 40, 30, 20, 10] 역순으로


# # 리스트 안 값들 합계
# sum = 0
# for a in a_arr :
#     print(a)
#     sum += a
# print(sum)


# # 리스트 추가 : append, insert, extend
# # 리스트 수정 : list[위치] = 값 변경
# # 리스트 삭제 : pop, del

# alist = [1,2,3]
# alist.append(4)
# print(alist)    # 결과값은 [1, 2, 3, 4]

# alist.pop()
# print(alist)    # 결과값은 [1, 2, 3] 제일 뒤의 값이 지워짐

# alist.pop(0)
# print(alist)    # 결과값은 [2, 3] 0번째 값 지워짐


# 예제 : 리스트에서 100 이상 숫자 출력하기
n_arr = [100,91,230,1,2,5,70,500]
a_arr = []
# for n in n_arr :
#     if n >= 100 :
#         a_arr.append(n)
# print(a_arr)        # 결과값은 [100, 230, 500]



for n in n_arr :
    no = len(str(n))
    a1 = "{}:{}자리수".format(n, no)
    a_arr.append(a1)
    print(a1)
print(a_arr)
# 결과값은 ['100:3자리수', '91:2자리수', '230:3자리수', '1:1자리수', '2:1자리수', '5:1자리수', '70:2자리수', '500:3자리수']
