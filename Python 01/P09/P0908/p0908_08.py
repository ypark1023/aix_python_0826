from p0908_07 import Stu1
from p0908_07 import StuLog1

stuList = StuLog1()
s1 = Stu1(1, "홍길동", 90, 80, 70)
s2 = Stu1(2, "유관순", 80, 100, 75)
stuList.add(s1, s2)

for s in stuList.slist:
    print(s)

# 결과값은 
# 1       홍길동  90      70      80      240     80.0
# 2       유관순  80      75      100     255     85.0