# 클래스 캡슐화

class Student:
    def __init__(self, no, name, kor, eng, math):
        self.__no = no
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__math = math
        self.__total = kor + eng + math
        self.__average = (kor + eng + math) / 3

    def calc_sum(self):
        self.__total = self.__kor + self.__eng + self.__math
        return self.__total
        
    def calc_avg(self):
        self.__average = (self.__kor + self.__eng + self.__math) / 3
        return self.__average

    def __str__(self):
        return f"번호: {self.__no}, 이름: {self.__name}, 국어: {self.__kor}, 영어: {self.__eng}, 수학: {self.__math}, 총점: {self.__total}"

# 캡술화는 클래스 내부의 변수를 보호하기 위함
# 캡슐화 했을 때는 수정할 수 있도록, get과 set 함수를 넣어줘야 함
    def get_kor(self):
        return self.__kor

    def set_kor(self, kor):
        if kor < 0 :
            print("잘못된 값 입력됨")
            return
        self.__kor = kor
    


# 객체 선언
s1 = Student(1, "홍길동", 100, 90, 60)

s1.kor = 80
print(s1)   # 결과값 - 번호: 1, 이름: 홍길동, 국어: 100, 영어: 90, 수학: 60, 총점: 250 (변경이 적용 안됨)

s1.set_kor(80)
s1.calc_sum()
s1.calc_avg()
print(s1)   # 결과값 - 번호: 1, 이름: 홍길동, 국어: 80, 영어: 90, 수학: 60, 총점: 230


