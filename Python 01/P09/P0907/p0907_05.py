# 파일 저장하기

import os

# if not os.path.exists("aaa4") :
#     os.makedirs("aaa4")

# with open ("aaa4/stu.txt", "w", encoding="utf-8") as file0 :

#     while True :
#         line0 = input("내용 입력: ")
#         if line0 == "" : break
#         file0.write(line0+",")


#     print("파일 저장됨")



# stu0 = []
# with open("aaa4/stu.txt", "r", encoding="utf-8") as file0 :
#     while True:
#         line0 = file0.readline()
#         line0 = line0.strip()
#         if line0 == "" : break
#         arr0 = line0.split(",")
#         stu0.append(arr0)

# print(stu0)

# # 방법1 rstrip
# with open("aaa4/stu.txt","a",encoding="utf-8") as f:
#     allStr = ""
#     while True:
#         outStr = input("내용 입력 : ")
#         if outStr == "" :
#             f.write(allStr.rstrip(",")+"\n")
#             break
#         allStr += (outStr+",")
#     # print(allStr)

# 방법2
with open("aaa4/stu.txt","a",encoding="utf-8") as f:
    allStr = ""
    no = 0
    while True:
        outStr = input("내용 입력 : ")
        if no == 0 : 
            allStr = outStr
            no =+ 1
            continue

        if outStr == "" :
            f.write(allStr+"\n")
            break
        allStr += ("," + outStr)
        no =+ 1
    # print(allStr)





# # 연습22
# # 외부 자료 변경하기

# strL =[]

# m_str = '"서울특별시  (1100000000)","9,330,658","4,482,949","          2.08","4,504,432","4,826,226","          0.93"'
# test = m_str.split('","')

# for t in test :
#     t = t.replace('"', '')
#     t = t.replace(",", "")
#     t = t.strip()
#     if t.isdigit():
#         t = float(t)
#     strL.append(t)
#     # print(t)

# result1 = strL[4]/strL[1]*100
# result2 = strL[5]/strL[1]*100
# print(strL)
# print("서울 총인구 대비 남성 비율:{:.2f}".format(result1))
# print("서울 총인구 대비 남성 비율:{:.2f}".format(result2))

# # 결과값은
# # 서울 총인구 대비 남성 비율:48.28
# # 서울 총인구 대비 남성 비율:51.72

