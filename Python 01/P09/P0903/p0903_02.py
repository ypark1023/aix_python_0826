# 숫자에 _ 넣으면 하나로 인식
# 숫자에 , 넣으면 한 숫자로 인식 못함


# # split 예제

# # split 하면 쪼개서 List로 만들어줌

# # 하나엔 10 곱하기, 하나엔 100 곱하기
# num = input("숫자 입력(1/3) :")
# nums = num.split("/")
# #1
# # result = (int(nums[0])*10) + (int(nums[1])*100)
# # print(result)
# #2
# nums = [int(i) for i in nums]
# result = (nums[0]*10) + (nums[1]*100)
# print(result)



#######################


def cal(choice):
    choice2 = choice.split("/")
    if choice2[0] == "1" :
        print("1.컴퓨터")
        print("구매금액: ", int(choice2[1])*1_000_000)
    elif choice2[0] == "2" :
        print("2. 세탁기")
        print("구매금액: ", int(choice2[1])*2_000_000)
    elif choice[0] == "3" :
        print("3. 오디오")
        print("구매금액: ", int(choice2[1])*500_000)
    else : 
        print("다른 번호 입력")


print("1. 컴퓨터-1_000_000")
print("2. 세탁기-2_000_000")
print("3. 오디오-500_000")
choice = input("번호와 개수 입력(1/3): ")
cal(choice)






