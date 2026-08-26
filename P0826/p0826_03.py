
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

# print는 출력, input은 입력

num = input("숫자를 입력하세요")
print("입력숫자: {}".format(num))


# input으로 받은 건 모두 문자열 타입, int를 앞에 넣어서 정수 타입으로 바꿔줌
a2=int(input("첫번째 숫자를 입력하세요"))
b2=int(input("두번째 숫자를 입력하세요"))
print(a2+b2)
print(a2-b2)
print(a2*b2)
print(a2/b2)
print(a2**b2)


# 예제: 아이디, 패스워드 입력받아 출력하시오

aa=input("아이디를 입력하세요")
bb=input("패스워드를 입력하세요")
print("아이디: {}, 패스워드: {}".format(aa, bb))