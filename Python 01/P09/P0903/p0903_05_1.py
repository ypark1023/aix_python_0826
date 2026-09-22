# 쇼핑몰 예제

my_info = {"id":"aaa", "pw":"1111", "money":10_000_000, "bonusP":0}
cart = []

prod = [
    {"name":"컴퓨터", "price":1_000_000, "bonusP":1_000_000*0.1},
    {"name":"냉장고", "price":2_000_000, "bonusP":2_000_000*0.1},
    {"name":"오디오", "price":500_000, "bonusP":500_000*0.1}
]

def cal1(choice):
    print("구매 완료")
    my_info["money"] = my_info["money"]-prod[choice-1]["price"]
    my_info["bonusP"] = my_info["bonusP"]+prod[choice-1]["bonusP"]
    print("남은 금액: {}원".format(my_info["money"]))
    print("보너스 포인트: {}p".format(my_info["bonusP"]))


while True :
    print("[A 쇼핑몰에 오신 걸 환영합니다]")
    id = input("ID: ")
    pw = input("PW: ")
    if (my_info["id"] == id) & (my_info["pw"] == pw) :
        print("로그인이 됐습니다")
        break
    else :
        print("ID 또는 PW가 일치하지 않습니다")
print()
print("나의 보유액 : {:,}원".format(my_info["money"]))
print("나의 포인트 : {:,}p".format(my_info["bonusP"]))
print("-"*40)
while True :
    print()
    print("[쇼핑 리스트]")
    # print("1. 컴퓨터: 1,000,000원")
    # print("2. 냉장고: 2,000,000원")
    # print("3. 오디오: 500,000원")
    for i,p in enumerate(prod) :
        print(f"{i+1}. {p["name"]}: {p["price"]:,}원")
    print("9. 구매상품 리스트")
    print("-"*40)
    choice = int(input("1~3 중 원하는 번호 입력: "))
    print()
    if choice == 1 :
        no1= int(input("1. 컴퓨터를 구매하시겠습니까? 구매: 1 / 취소: 0 :"))
        if no1 == 1 :
            cal1(choice)
        elif no1 == 0 :
            print("구매 취소")
        else : 
            print("이전 화면으로 이동")
        print()
    elif choice == 2 :
        no1= int(input("2. 냉장고를 구매하시겠습니까? 구매: 1 / 취소: 0 :"))
        if no1 == 1 :
            cal1(choice)
        elif no1 == 0 :
            print("구매 취소")
        else : 
            print("이전 화면으로 이동")
        print()
    elif choice == 3 :
        no1= int(input("3. 오디오를 구매하시겠습니까? 구매: 1 / 취소: 0 :"))
        if no1 == 1 :
            cal1(choice)
        elif no1 == 0 :
            print("구매 취소")
        else : 
            print("이전 화면으로 이동")
        print()
    elif choice == 9 :
        pass