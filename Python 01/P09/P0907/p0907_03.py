# 외부 파일 읽어오기

# # 방법 1
# f_o = open("c:/aaa/abcd.txt", "r", encoding="utf-8")

# while True :
#     str1 = f_o.readline()
#     if str1 == "" : break
#     print(str1, end="")

# # print("프로그램 종료")
# f_o.close()



# # 방법 2
# with open("c:/aaa/abcd.txt", "r", encoding="utf-8") as file1 :

#     while True:
#         str2 = file1.readline()
#         if str2 == "" : break
#         print(str2, end="")

# print("프로그램 종료")
# # f_o.close() 쓰지 않아도 된다



# # 연습
# stuL = []

# with open("c:/aaa/stu1.txt", "r", encoding="utf-8") as file1 :

#     while True:
#         line1 = file1.readline()
#         line1 = line1.strip()
#         if line1 == "" : break
#         arr1 = line1.split(",")
#         # print(arr1, end="")
#         for i, s in enumerate(arr1) :
#             if i == 0 or i == 1 : continue
#             elif 2 <= i <= 5 :
#                 arr1[i] = int(s.strip())
#             elif i == 6 :
#                 arr1[i] = float(s.strip())
#         stuL.append(arr1)
#         # stuL.append({"no":arr1[0], "name":arr1[1], "kor":arr1[2], "eng":arr1[3], "math":arr1[4], "total":arr1[5], "avg":arr1[6]})
#         # print(arr1)


# print(stuL)



# 반복 연습

# sum = 0
# stuL2 = []
# with open("c:/aaa/test3.txt", "r", encoding="utf-8") as file2 :
#     while True:
#         line2 = file2.readline()
#         line2 = line2.strip()
#         if line2 == "" : break
#         if line2.isdigit() :
#             line2 = int(line2)
#             sum += line2
#         stuL2.append(line2)
        
#     print(sum)
#     print(stuL2)





# # csv 파일 테스트
# with open("c:/aaa/testset1.csv", "r") as file1 :

#     while True:
#         str2 = file1.readline()
#         if str2 == "" : break
#         print(str2, end="")

# print("프로그램 종료")
# # f_o.close() 쓰지 않아도 된다
