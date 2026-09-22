# try, except 함순

# arr = [1,2,3,4,5]

# while True :
#     choice = input("0~4까지 숫자 입력: ")
#     if choice.isdigit():
#         choice = int(choice)
#         if choice > 4 :
#             print("0~4까지만 입력")
#         else :
#             print("선택 값: ", arr[choice])
#     else :
#         print("숫자만 입력")
#         continue


# while True :
#     try :
#         choice = int(input("0~4까지 숫자 입력: "))
#         print("선택 값: ", arr[choice])
#     except Exception as e:
#         print("에러 발생")
#         print(e)

# # 5 이상 입력 시 except 처리하고 프로그램 계속 돌아감
# 웬만하면 try/except는 쓰지 않도록 하라 (외부 잘못이 아닌 이상)




# print(1)
# try :
#     print(2)
#     print(3)
#     print(4)
# except :
#     print(5)
#     print(6)
# print(7)        # 결과값은 1 2 3 4 7
