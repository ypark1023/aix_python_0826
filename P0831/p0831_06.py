ranNo = [1,5,9,7,4]
inputNo = [1,2,3,4]
answerNo = []

if inputNo in ranNo :
    print("있음")
else :
    print("없음")


count = 0
if inputNo in ranNo :
    count = count+1
    print("있음")
else :
    print("없음")
print("개수: ", count)



# count = 0
# for i in inputNo:
#     if inputNo in ranNo :
#         count = count+1
#         answerNo.append(i)        
#         print("있음")
#     else :
#         print("없음")
# print("개수: ", count)



# count = 0
# no = []
# while True :
#     inum = int(input("숫자 입력: "))
#     if inum == 0:
#         print("입력 숫자: {} / 종료".format(no))
#         break
#     no.append(inum)
#     count = count+1
# print("개수: ", count)
