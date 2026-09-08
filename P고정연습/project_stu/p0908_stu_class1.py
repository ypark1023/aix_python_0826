# 학생 성적 프로그램 - 클래스1

class Student():
    def __init__(self, no, name, kor, eng, math) :
    # def __init__(self, no, name, kor, eng, math) :
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        # self.total = kor + eng + math
        # self.average = (kor + eng + math) / 3
        self.total = 0
        self.average = 0
        self.rank = 0
        self.calc_sum()
        self.calc_avg()

    def calc_sum(self):
        self.total = self.kor + self.eng + self.math
        return self.total
        
    def calc_avg(self):
        self.average = (self.kor + self.eng + self.math) / 3
        return self.average

    def __str__(self):
        str1 = f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.average:.2f}\t{self.rank}"
        return str1