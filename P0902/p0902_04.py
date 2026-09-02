# # map
# aa= ['1','2','3']
# aa2 = list(map(int,aa))
# print(aa2)      # 결과값은 [1, 2, 3]



# # 예제예제88 :

# str = input("번호 3개 입력(1/2/3 형태): ")

# alist = str.split("/")
# # alist2 = [int(i) for i in alist]
# alist2 = list(map(int,alist))
# print(alist2)

# sum = 0
# for a in alist2:
#     sum += a
# print(sum)

# # 결과값은 
# # 번호 3개 입력(1/2/3 형태): 8/12/19
# # 39


# # 예제 
# stu = [1,"홍길동",100,100,100]
# stu2 = list(map(str,stu))
# print(stu2)     #결과값은 ['1', '홍길동', '100', '100', '100']


# # map은 한꺼번에 타입 바꿀 때 (문자열 -> 숫자, 숫자 -> 문자...)


# # 예제22
# str = input("날짜 입력(2000/1/1): ")

# str2 = str.split("/")
# print(str2)             # 결과값은  ['2026', '9', '2']

# print("{}년 {}월 {}일".format(*str2))   # 결과값은 2026년 9월 2일



# isdigit

while True :
    a = input("숫자 입력: ")
    if a.isdigit():
        a = int(a)
        break
    else : 
        print("숫자가 아님 다시 입력")
print(a)

