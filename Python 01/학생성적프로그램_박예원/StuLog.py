
class StuLog():
    title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
    print("-"*60)
    print("[학생 성적 출력]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))

    def __init__(self):
        self.slist = []

    def add(self, *stu):
        for s0 in stu:
            self.slist.append(s0)

    def print(self):
        print("번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수", sep="\t")
        print("-"*60)
        for s in self.slist:
            print(s)