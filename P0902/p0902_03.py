# # 리스트 만들기
# a1 = [1,2,3,4,5]
# a2 = [0]*5
# a3 = list(range(1,6))
# a4 = [i for i in range(1,6)] #컴프리헨션, 리스트내포
# a5 = [i for i in range(1,6) if i%2 == 0] #컴프리헨션, 리스트내포


# print(a1)       # 결과값은 [1, 2, 3, 4, 5]
# print(a2)       # 결과값은 [0, 0, 0, 0, 0]
# print(a3)       # 결과값은 [1, 2, 3, 4, 5]   
# print(a4)       # 결과값은 [1, 2, 3, 4, 5]
# print(a5)       # 결과값은 [2, 4]



# 리스트 zip
# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# c = []


# for i in range(len(a)):
#     c.append([a[i], b[i]])
# print(c)        # 결과값은 [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]]

# for i, j in zip(a, b) :
#     c.append([i, j])
# print(c)        # 결과값은 [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]]

# c = list(zip(a,b))
# d = dict(zip(a,b))
# print(c)        # 결과값은 [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
# print(d)        # 결과값은 {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}





# # 예제 : 딕셔너리 이해하기

# aa = "가나다라가가가나나다라라라라라라라"
# aa_dic = {}

# for a in aa :
#     if a not in aa_dic :
#         aa_dic[a] = 1
#     else :
#         aa_dic[a] += 1

# print(aa_dic)       # 결과값은 {'가': 4, '나': 3, '다': 2, '라': 8}




# # split
# ee = "a/b/c/d/e/f/g"

# ee_list = ee.split("/")
# print(ee_list)      # 결과값은 ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# bb = "100,10,5,4,1"
# bb_list = bb.split(",")
# print(bb_list)      # 결과값은 ['100', '10', '5', '4', '1'] 문자열 타입

# bb_list2 = [int(i) for i in bb_list]
# print(bb_list2)     # 결과값은 [100, 10, 5, 4, 1] 정수 타입으로 바꾸기


# sum = 0
# for b in bb_list2 :
#     sum += b

# print(sum)          # 결과값은 120





# # find 와 index

# ss = "파이썬 공부 !! 열심히 합시다 파이썬"
# print(ss.count("공부"))     # 결과값은 1
# print(ss.count("파이썬"))   # 결과값은 2
# print(ss.find("파이썬"))    # 결과값은 0
# print(ss.find("자바"))      # 결과값은 -1  없을 때 -1
# print(ss.index("공부"))     # 결과값은 4
# print(ss.index("자바"))     # ValueError 뜸




# # strip, replace

# ss = "   파이썬"
# ss2 = "<<<파<이<썬<<"

# # print(ss.strip(" "))          #결과값은 "파이선"
# print(ss.strip())               #결과값은 "파이선"
# print(ss2.replace("<",""))      #결과값은 "파이선"




# # join
# aa = "/"
# bb= aa.join("바나나")
# cc= aa.join(["바나나", "딸기"])

# print(bb)       # 결과값은 바/나/나
# print(cc)       # 결과값은 바나나/딸기




# # 예제
# alist = "1,홍길동,100,100,100,300,100.0"

# alist2 = alist.split(",")
# print(alist2)      # 결과값은 ['1', '홍길동', '100', '100', '100', '300', '100.0']
# alist2[2] = 90
# print(alist2)      # 결과값은 ['1', '홍길동', 90, '100', '100', '300', '100.0']
# alist2[3] = int(alist2[3])
# alist2[4] = int(alist2[5])
# alist2[5] = alist2[2]+alist2[3]+alist2[4]
# alist2[6] = alist2[5]/3
# print(alist2)       # 결과값은 ['1', '홍길동', 90, 100, 300, 490, 163.33333333333334]

# alist3 = [str(i) for i in alist2]
# print(alist3)       # 결과값은 ['1', '홍길동', '90', '100', '300', '490', '163.33333333333334']


# # join으로 다시 묶기 - 다시 문자열로 변경
# dd = "/"
# ee= dd.join(alist3)
# print(ee)       # 결과값은 1/홍길동/90/100/300/490/163.33333333333334





# 예제예제88 :

str = input("번호 3개 입력(1/2/3 형태): ")

alist = str.split("/")
alist2 = [int(i) for i in alist]
print(alist2)

sum = 0
for a in alist2:
    sum += a
print(sum)

# 결과값은
# 번호 3개 입력(1/2/3 형태): 7/9/12
# [7, 9, 12]
# 28


