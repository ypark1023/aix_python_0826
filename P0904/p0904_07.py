# r : 파일읽기 / w : 덮어쓰기 / a : 이어쓰기

# 파일에 써넣기

# 위처럼 쓸수도 있다
# with open("c:/aaa/abc.txt", "w") as fw:


# fw = open("c:/aaa/abc.txt", "w")
# while True:
#     line = input("글을 입력하시오: ")
#     if line != "" :
#         fw.writelines(line+"\n")
#     else : break

# print("파일이 저장됐음")


fw = open("c:/aaa/abc.txt", "a")
while True:
    line = input("글을 입력하시오: ")
    if line != "" :
        fw.writelines(line+"\n")
    else : break

print("파일이 저장됐음")

