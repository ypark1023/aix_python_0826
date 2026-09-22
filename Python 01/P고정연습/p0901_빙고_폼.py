# 빙고 만들기
bb = list(range(1,26))
# print(bb, end =" ")

# i = index
# v = value

import random
random.shuffle(bb)

while True :
    print(" "*15, end="")
    print("[5x5 빙고 게임]")
    print("-"*40)
    for i, v in enumerate(bb) :
        if (i+1)%5 != 0 :
            print(v, end="\t") 
        else :
            print(v)
    print("-"*40)
    num = int(input("1~25 원하는 번호 입력: "))
    if num in bb :
        idx = bb.index(num)
        bb[idx] = "X"


