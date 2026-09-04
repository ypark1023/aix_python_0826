# 학생 성적표 파일 불러오기

# stu = []

# file0 = open("C:/aaa/test2.txt", "r", encoding="utf-8")

# while True :
#     line1 = file0.readline()
#     line1 = line1.strip()
#     if not line1 : break
#     arr = line1.split(",")
#     for i, a in enumerate(arr) :
#         if 2 <= i <= 5 :
#             arr[i] = int(a)
#         elif i == 6 :
#             arr[i] = float(a)
#     stu.append({"no":arr[0], "name":arr[1], "kor":arr[2], "eng":arr[3], "math":arr[4], "total":arr[5], "avg":arr[6]})
#     print(arr)

# file0.close()

# print(stu)





# with open으로도 가능

# stu = []
# with open("C:/aaa/test2.txt","r",encoding="utf-8") as file0:
#     while True:
#         line00 = file0.readline()
#         line00 = line00.strip()
#         if not line00 : break
#         arr0 = line00.split(",")
#         for i, a in enumerate(arr0):
#             if 2<= i <=5 :
#                 arr0[i] = int(a)
#             elif i == 6 :
#                 arr0[i] = float(a)
#         stu.append({"no":arr0[0], "name":arr0[1], "kor":arr0[2], "eng":arr0[3], "math":arr0[4], "total":arr0[5], "avg": arr0[6]})


# print(stu)

