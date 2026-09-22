# 예제 다시

my_info = {"id":"aaa","pw":"1111","money":10_000_000,"bonusP":0}


s_arr = [
    {"name":"컴퓨터", "price":1_000_000}, 
    {"name":"냉장고", "price":2_000_000}, 
    {"name":"오디오", "price":500_000}, 
    {"name":"세탁기", "price":1_500_000}
]


def p_print(choice):
    if my_info["money"] < s_arr[choice-1]["price"]:
        print("머니 충전!")
        return 
    print("제품: {}".format(s_arr[choice-1]["name"]))
    print("가격: {:,}원".format(s_arr[choice-1]["price"]))
    my_info["money"] = my_info["money"] - s_arr[choice-1]["price"]
    print("남은 금액: {:,}원".format(my_info["money"]))


while True:
    print("-"*50)
    print("상품을 선택하시오")
    for i, v in enumerate(s_arr):
        print("{}.{}".format(i+1, v["name"]))

    choice = int(input("번호 입력: "))
    print("-"*50)
    if choice == 1 :
        p_print(choice)
    elif choice == 2 :
        p_print(choice)
    elif choice == 3 :
        p_print(choice)
    elif choice == 4 :
        p_print(choice)
    else :
        print("1~4 중 입력하라")

