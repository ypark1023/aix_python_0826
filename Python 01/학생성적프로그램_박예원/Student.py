
class Student():
    def __init__(self, *args):
        if len(args) == 5 :
            self.no = args[0]
            self.name = args[1]
            self.kor = args[2]
            self.eng = args[3]
            self.math = args[4]
            self.total = 0
            self.average = 0
            self.rank = 0

        elif len(args) == 8 :
            self.no = args[0]
            self.name = args[1]
            self.kor = args[2]
            self.eng = args[3]
            self.math = args[4]
            self.total = args[5]
            self.average = args[6]
            self.rank = args[7]

        self.cal_sum()
        self.cal_avg()

    def cal_sum(self):
        self.total = self.kor + self.eng + self.math
        return self.total
    
    def cal_avg(self):
        self.average = (self.kor + self.eng + self.math)/3
        return self.average

    def __str__(self):
        str1 = f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.average:.2f}\t{self.rank}"
        return str1


    def s_str(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.average:.2f},{self.rank}"