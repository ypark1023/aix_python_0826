# 외부 파일에 쓰기

import os

# # 덮어쓰기
# with open("c:/aaa/test4.txt", "w") as file11:
#     while True : 
#         outStr = input("내용 입력: ")
#         if outStr == "" : break
#         file11.write(outStr+",")

#     print("파일 내용이 저장됨")



# 이어쓰기
# with open("c:/aaa/test4.txt", "a") as file11:
#     while True : 
#         outStr = input("내용 입력: ")
#         if outStr == "" : break
#         file11.write(outStr+",")

#     print("파일 내용이 저장됨")



# # 파일 혹은 폴더 있는지 미리 확인, 없으면 만들어주기
# if not os.path.exists("aaa3"):
#     os.makedirs("aaa3")

# with open("aaa3/test5", "w") as file11:
#     while True : 
#         outStr = input("내용 입력: ")
#         if outStr == "" : break
#         file11.write(outStr+"\n")

#     print("파일 내용이 저장됨")


# 파일 이름도 지정할 수 있음
fname = input("저장할 파일 이름 입력(파일명): ")
if not os.path.exists("aaa3"):
    os.makedirs("aaa3")

with open("aaa3/"+fname, "w") as file11:
    while True : 
        outStr = input("내용 입력: ")
        if outStr == "" : break
        file11.write(outStr+"\n")

    print("파일 내용이 저장됨")
