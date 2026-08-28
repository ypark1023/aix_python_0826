# 반복문
# for 문 / while 문

# for i(변수) in 범위 : - 범위만큼 반복을 해준다

# for i in range(10) :
#     print(2)              # 2가 10번 반복해서 출력됨


# for i in range(5) :
#     print(i)              # 결과값은 0 1 2 3 4


# for i in range(5) :
#     print(i*10)           # 결과값은 0 10 20 30 40


# for i in range(1,6) :
#     print(i)              # 결과값은 1 2 3 4 5 / 1부터 시작해서 6전까지


# for i in range(1,11,2) :
#     print(i)              # 결과값은 1 3 5 7 9 / 1부터 시작해서 11전까지, 간격 2로


# for i in "안녕하세요" :
#     print(i)                # 결과값은 안 녕 하 세 요



# for i in range(2) :
#     print("안녕")

# for _ in range(3) :
#     print("안녕")               # i 대신 _(언더바)를 써도 동일




# for i in range(3) :
#     no = i+1
#     name = input("이름 입력: ")
#     kor = input("국어 점수 입력: ")
#     print("{},{},{}".format(no, name, kor))


# for i in range(1, 10):
#     print(f"2 X {i} = {2*i}")

# 결과값은
# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
# 2 X 6 = 12
# 2 X 7 = 14
# 2 X 8 = 16
# 2 X 9 = 18


# sum = 0
# for i in range(1,11) :
#     sum = sum+i
# print("합계: ", sum)

# sum = 0
# for i in range(1,101) :
#     sum = sum+i
# print("합계: ", sum)

# sum = 0
# for i in range(1,1001) :
#     sum = sum+i
# print("합계: ", sum)

# sum = 0
# for i in range(1,10001) :
#     sum = sum+i
# print("합계: ", sum)

# sum = 0
# for i in range(1,100001) :
#     sum = sum+i
# print("합계: ", sum)

# 결과값은
# 합계:  55
# 합계:  5050
# 합계:  500500
# 합계:  50005000
# 합계:  5000050000



# 퀴즈 : sum이 100이 넘는 때는 언제일까요?

# sum = 0
# for i in range(1,101) :
#     sum = sum+i
#     if sum > 100 :
#         print("100보다 클 때: ", i)
#         print("100초과될 때 시점: ", sum)
#         break
# print("합계: ", sum)



# sum = 0
# for i in range(1,11) :
#     sum = sum+i
#     if sum > 11 :
#         print("100보다 클 때: ", i)
#         print("100보다 바로 앞의 작은 수: ", sum-i)
#         print("100초과될 때 시점: ", sum)




# for i in range(0,10) :
#     for j in range(0,10) :
#         print("{}{}".format(i,j))

# # 결과값은 00~99까지


# # 번호표
# for i in range(0,10) :
#     for j in range(0,10) :
#         for k in range (0,10) :
#             print("[번호표]: {}{}{}".format(i,j,k))

# # 결과값은 000~999까지