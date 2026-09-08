# 여러 개의 클래스 연습 

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

    # def print(self):
    #     print(self.no, self.name, self.kor, self.eng, self.math, self.total, self.average, sep=" ")

    # def __str__(self):
    #         return f"번호: {self.no}, 이름: {self.name}, 국어: {self.kor}, 영어: {self.eng}, 수학: {self.math}, 총합: {self.total}, 평균: {self.average:.2f}"

    def __str__(self):
        str1 = f"번호: {self.no}, 이름: {self.name}, 국어: {self.kor}, 영어: {self.eng}, 수학: {self.math}, 총합: {self.total}, 평균: {self.average:.2f}"
        return str1

class StuLog():
    def __init__(self, s = None):
        self.slist = []  # 인스턴스 변수로 생성
        if s is not None:
            self.slist.append(s)

    # def add(self, s):
    #     self.slist.append(s)

    def add(self, *stu):      # 가변매개변수 활용
        for s0 in stu :
            self.slist.append(s0)


#############################################

# stuList = []
s1 = Student(1, "홍길동", 100, 90, 80)
s2 = Student(2, "유관순", 90, 85, 75)

stuList = StuLog()
# stuList.add(s1)
# stuList.add(s2)
stuList.add(s1, s2)

for ss in stuList.slist:            # .slist 요게 기억할 부분!
    print(ss)

