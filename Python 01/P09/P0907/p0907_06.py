# 파일 복사하기

import os

# # 연습1
# rf = open("c:/aaa/1re.jpg", "rb")
# wf = open("c:/aaa2/2re.jpg", "wb")

# while True:
#     fdata = rf.read(1)
#     if not fdata : break
#     wf.write(fdata)

# rf.close()
# wf.close()
# print("이미지 파일이 복사됨")



# 연습2
rf = open("c:/aaa/1sw.jpg", "rb")
wf = open("c:/aaa2/2sw.jpg", "wb")

while True:
    fimage = rf.read(1)
    if not fimage : break
    wf.write(fimage)

rf.close()
wf.close()
print("이미지 복사 완료")