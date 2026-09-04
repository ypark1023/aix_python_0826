# lambda = 함수 요약

# def sum(n1, n2):
#     result = n1+n2
#     return result

# print(sum(10,20))     # 결과값은 30
#####################################################

# # 람다식
# sum = lambda n1, n2 : n1+n2
# print(sum(10,20))       # 결과값은 30

# mul = lambda n1, n2 : n1*n2
# print(mul(10,20))       # 결과값은 200

# sum1 = lambda n1 : n1+10
# print(sum1(15))         # 결과값은25


#####################################################

# map 함수

# mlist = [1,2,3,4,5]
# mlist2 = []

# for m in mlist:
#     mlist2.append(m+10)

# print(mlist2)       # 결과값은 [11, 12, 13, 14, 15]

######################
# 함수 활용 형식

# def add(num):
#     return num + 10

# mlist = [1,2,3,4,5]
# a_arr = []

# for m in mlist:
#     a_arr.append(add(m))

# print(a_arr)        # 결과값은 [11, 12, 13, 14, 15]     

######################
# 리스트 내포 형식

# mlist = [1,2,3,4,5]
# a_arr = [m+10 for m in mlist]
# print(a_arr)       # 결과값은 [11, 12, 13, 14, 15]


######################
# 람다와 맵 활용 형식

# sum0 = lambda n1 : n1+10
# mlist = [1,2,3,4,5]
# mlist2 = list(map(sum0,mlist))
# print(mlist2)       # 결과값은 [11, 12, 13, 14, 15]


######################
# data = ["100", "200", "300"]
# result = map(int, data)
# print(list(result))     # 결과값은 [100, 200, 300]


######################
a = [1,2,3]
b = [10,20,30]
result = map(lambda x, y : x+y, a,b)
print(list(result))        # 결과값은 [11, 22, 33]


######################
# 1~4 곱하기 구하기
result = 1
for i in range(1,5) :
    result *= i
print(result)           # 결과값은 24 / 속도는 이 형태가 빠르다!


def fact1(num):
    if num <=1 : return num
    else : return num * fact1(num-1)

print(fact1(4))           # 결과값은 24 / 재귀함수