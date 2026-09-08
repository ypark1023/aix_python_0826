# 예제1 : 반복문을 사용해서 1~100까지 합을 출력
# 예제2 : 200 넘는 시점의 i값과 i번째 합계를 출력
# 예제3 : 200 넘는 이전 시점의 i값 합계를 출력
# 예제4 : 구구단을 출력


# 예제 1 : 1~100 합계

sum = 0
for i in range(1,101) :
    sum = sum+i
print (sum)

# 결과값은 5050



# 예제 2~3 : 200 넘는 시점

sum = 0
for i in range(1,101) :
    sum = sum+i
    if sum > 200 : 
        print ("200 넘을 때 i값: ", i)
        print ("200 넘을 때 합계: ", sum+i)
        print ("200 넘기 전 i값: ", i-1)
        print ("200 넘기 전 합계: ", sum-i)
        break

# 결과값
# 200 넘을 때 i값:  20
# 200 넘을 때 합계:  230
# 200 넘기 전 i값:  19
# 200 넘기 전 합계:  190



# 예제 4: 구구단 출력
for i in range(1,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j))

# 결과값
# 1 X 1 = 1 ~ 9 X 9 = 81



# 예제 : 점수 입력하기

name = []
score = []
for i in range(2) :
    name.append(input("이름 입력: "))
    score.append(input("점수 입력: "))

for i in range(2) :
    print("{} \t {}".format(name[i], score[i]))

# 결과값
    # 이름 입력: 홍길동 
    # 점수 입력: 100
    # 이름 입력: 유관순
    # 점수 입력: 90
    # 홍길동   100
    # 유관순   90



list_a = []
for i in range(2) :
    name = input("이름 입력: ")
    score  = input("점수 입력: ")
    list_a.append([name, score])

for i in range(2) :
    print("{}\t{}".format(*list_a[i]))

# 결과값
    # 이름 입력: 홍길동
    # 점수 입력: 90
    # 이름 입력: 유관순
    # 점수 입력: 100
    # 홍길동  90
    # 유관순  100