# 파일에서 한줄씩 읽어오기

# file1 = open("C:/aaa/test1.txt", "r", encoding="utf-8")
# f1 = file1.readline()
# print(f1, end="")
# f2 = file1.readline()
# print(f2, end="")
# f3 = file1.readline()
# print(f3, end="")

# file1.close()

# 결과값은 Hello / Love / Goodbye 으로 동일


# while 반복문으로 만들기
file1 = open("C:/aaa/test1.txt", "r", encoding="utf-8")
while True :
    line = file1.readline()
    if line == "" : break
    print(line, end="")
file1.close()

# 결과값은 Hello / Love / Goodbye 으로 동일


