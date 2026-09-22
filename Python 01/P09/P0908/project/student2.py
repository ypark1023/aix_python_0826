# 학생 성적 클래스2 - 입력



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

    def print(self):
        print("번호", "이름", "국어", "영어", "수학", "총합", "평균", sep="\t")
        print("-"*50)
        for s in self.slist:
            print(s)
