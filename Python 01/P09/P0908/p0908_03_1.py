# 클래스 반복 연습 - 변수값을 바꾸었을 때

class Student():
    def __init__(self, no, name, kor, eng, math) :
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = 0
        self.average = 0
        self.calc_sum()
        self.calc_avg()

    def calc_sum(self):
        self.total = self.kor + self.eng + self.math
        return self.total
        
    def calc_avg(self):
        self.average = (self.kor + self.eng + self.math) / 3
        return self.average

    def print(self):
        print(self.no, self.name, self.kor, self.eng, self.math, self.total, self.average, sep=" ")


stuList = []

s1 = Student(1, "홍길동", 100, 90, 80)
s1.calc_sum()
s1.calc_avg()
s1.print()
# 결과값은 1 홍길동 100 90 80 270 90.0

# 값을 바꾸었을 때
s1.kor = 80
s1.calc_sum()
s1.calc_avg()
s1.print()
# 결과값은 1 홍길동 80 90 80 250 83.33333333333333