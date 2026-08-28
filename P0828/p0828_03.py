# paper = """\
# 네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
# 2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
# 이번 홍수의 원인으로 지목된 것처럼 
# 산 위의 빙하가 붕괴되면서 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다.\
# """

# print(paper)            
# print(len(paper))       # 문자열 몇 개인지 세기

# # 문자열 함수
# # split 함수
# str1 = "1,홍길동,100,90,80,100,90,80"
# s = str1.split(",")
# print(s)  
# # 결과값은 ['1', '홍길동', '100', '90', '80', '100', '90', '80'] / 리스트 형태로 출력이 됨
# print(s[2])
# # 결과값은 100  / 2번자리값을 출력해줌


# str2 = "2026-08-27"
# s2 = str2.split("-")
# print(s2[2])
# # 결과값은 27 / 2번자리값을 출력해줌

# str3 = "안녕 반가워 우리는 친구야"
# s3 = str3.split(" ")
# print(s3[3])
# # 결과값은 친구야 / 3번자리값을 출력해줌


# CSV 파일이란 Comma로 Segment를 Seperate분리하겠다는 것

# str4 = "EDMS,307-2E-PS-W-611-W008,VF5770"
# s = str4.split(",")
# print(s)
# print(s[2])



# # strip 함수
# aa1 = "    안녕하세요    "
# print(aa1.strip())
# # 결과값은 "안녕하세요"  / 공백 제거 기능

# aa2 = "   안녕   하세요   "
# print(aa2.strip())
# # 결과값은 "안녕   하세요"  / 글자 사이의 공백은 제거되지 않음



# # replace 함수
# aa3 = "aabbccddaaeeff"
# aa4= aa3.replace("a", "k")
# print(aa4)
# # 결과값은 kkbbccddkkeeff / a를 k로 대체함

# aa5 = aa2.replace(" ", "")
# print(aa5)
# # 결과값은 안녕하세요 / 공백을 공백없이 치환해서 공백 없애줌



# # find 함수
# bb = "abcdefghi"
# print(bb.find("f"))
# print(bb.rfind("c"))       
# # 결과값은 5  / 해당값이 몇번자리에 위치해 있는지 알려줌
# # 만약 찾는 값이 없으면 -1을 결과값으로 내줌
# # rfind는 오른쪽에서부터 찾아줌



# isalpha / isdigit

# name = input("이름 입력: ")
# if name.isalpha() :
#     print("입력 완료")
# else :
#     print("입력 오류")
# print(name)

# # 띄어쓰기도 포함되면 오류


# num = input("숫자 입력: ")
# num1 = int(num)
# print("입력 숫자: ", num1)


# num0 = input("숫자 입력: ")

# if num0.isdigit() :
#     num0 = int(num0)
#     print(num0)
# else : 
#     print ("숫자 외 입력됐음")


# # 반복문

# while(True) :
#     id = input("아이디 입력: ")
#     pw = input("패스워드 입력: ")
#     if id=="aaa" and pw=="1111" :
#         print("로그인 성공")
#         break
#     else :
#         print("로그인 실패. 재입력해주세요")

# # 실패하게 되면 계속 반복해서 물어보게 됨





paper = """\
네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
이번 홍수의 원인으로 지목된 것처럼 
산 위의 빙하가 붕괴되면서 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다.\
"""

print(paper.find("홍수"))
# 결과값은 4 제일 앞에서 부터
print(paper.rfind("홍수"))
# 결과값은 109 제일 끝에서부터

print(paper.count("홍수"))
# paper 속에 "홍수"가 몇 번 나오는지 세줌 / 결과값은 4

