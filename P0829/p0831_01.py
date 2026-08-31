# # 반복문

# for i in range(5) : 
#     print(i)

# # 결과값은 0 1 2 3 4

# for i in range(1, 5+1) : 
#     print(i)

# # 결과값은 1 2 3 4 5

# for i in range(1, 10+1, 2) : 
#     print(i)

# # 결과값은 1 3 5 7 9 


# for i in range(1,11) :
#     print(i*10)

# # 결과값 10 20 30 40 50 60 70 80 90 10


# fruits = ["베", "사과", "수박"]
# for f in fruits :
#     print(f)


# for i in "안녕하세요" :
#     print(i)

# # 결과값은 안 녕 하 세 요  



# # 예제 : 이름 입력 세 번 반복
# list_n = []
# for i in range(3) :
#     n = input("이름 입력: ")
#     list_n.append(n)
# print("[학생 명단]: {}".format(list_n))



# nums = [3,9,10,105,220,2,1]
# for n in nums :
#     print(n)



# # 예제 : 입력한 숫자가 홀수인지 짝수인지
# a = int(input("숫자 입력: "))

# # if문
# if a%2 == 0 :
#     print("짝수입니다")
# else :
#     print("홀수입니다")




# # 예제 : 홀짝 출력하기
# nums = [3,9,10,105,220,2,1]

# for n in nums :
#     if n%2 == 0 :
#         print("{}:짝수".format(n))
#     else :
#         print("{}:홀수".format(n))


# # +짝수만 출력해보기
# nums = [3,9,10,105,220,2,1]

# for n in nums :
#     if n%2 == 0 :
#         print("{}:짝수".format(n))
#     else :
#         pass





# # end="" 옆으로 출력됨 / end=" " 한칸 띄어서 횡으로 출력됨 / end="\t" 탭으로 띄어서 횡으로 추력됨
# for i in range(9) :
#     print(i, end="")       

# for i in range(9) :
#     print(i, end=" ")       

# for i in range(9) :
#     print(i, end="\t")       



# # 예제 : 구구단 출력
# for i in range(2,10) :
#     print("{}x1={}".format(i,1,i*1), end=" ")

# # 결과값은 2x1=1 3x1=1 4x1=1 5x1=1 6x1=1 7x1=1 8x1=1 9x1=1 


# for i in range(2,10) :
#     for j in range(1,10) :
#         print("{}x{}={}".format(i,j,i*j), end=" ")


# for i in range(2,10) :
#     print("[{}단]".format(i))
#     for j in range(1,10) :
#         print("{}x{}={}".format(i,j,i*j), end=" ")
#     print()



for i in range(2,10) :
    for j in range(1,10) :
        print("{}x{}={}".format(i,j,i*j), end=" ")
    print()
