# 학생 성적 클래스1 - 입력

class Student():
    def __init__(self, no, name, kor, eng, math) :
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        # self.total = kor + eng + math
        # self.average = (kor + eng + math) / 3
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

    def __str__(self):
        str1 = f"번호: {self.no}, 이름: {self.name}, 국어: {self.kor}, 영어: {self.eng}, 수학: {self.math}, 총합: {self.total}, 평균: {self.average:.2f}"
        return str1

