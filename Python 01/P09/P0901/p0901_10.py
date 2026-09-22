# 리스트, 튜플, 딕셔너리
# aa = [1,2,3,4,5] # 리스트
# bb = (1,2,3,4,5) # 튜플 *수정이 안됨*
# cc = {key1:value1, key2:value2, ....} # 딕셔너리


# 딕셔너리
# 리스트 : stu_arr = [1, "홍길동", 100, 100, 100]
# 딕셔너리는 {키:밸류}로 구성, 어떤 값인지 유추 가능
# stu = {"no":1, "name":"홍길동", "KOR":100, "ENG":100, "MATH":100, "SCI":100}
# print(stu)
# # 결과값은 {'no': 1, 'name': '홍길동', 'KOR': 100, 'ENG': 100, 'MATH': 100, 'SCI': 100}

# # 딕셔너리 추가 방법
# stu["total"] = stu["KOR"]+stu["ENG"]+stu["MATH"]+stu["SCI"]
# stu["avg"] = stu["total"]/4
# print(stu)
# # 결과값은 {'no': 1, 'name': '홍길동', 'KOR': 100, 'ENG': 100, 'MATH': 100, 'SCI': 100, 'total': 400, 'avg': 100.0}

# # 딕셔너리 수정 방법
# stu["KOR"] = 80
# stu["total"] = stu["KOR"]+stu["ENG"]+stu["MATH"]+stu["SCI"]
# stu["avg"] = stu["total"]/4
# print(stu)
# # 결과값은 {'no': 1, 'name': '홍길동', 'KOR': 80, 'ENG': 100, 'MATH': 100, 'SCI': 100, 'total': 380, 'avg': 95.0}


# # 밸류값 출력하기
# print(stu["KOR"])
# # 결과값은 100



# # 학생 성적 리스트
# stu_list = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":300,"avg":100},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":300,"avg":100}
# ]

# print(stu_list[0]["kor"])       # 결과값은 100
# print(stu_list[0]["name"])      # 결과값은 홍길동

# # # 추가, 맨 뒤에 붙음
# # stu_list[0]["rank"] = 1
# # print(stu_list)

# # 삭제, 리스트에서 뭘 지울지 입력
# # del(stu_list[0]["no"])
# # print(stu_list)




# stu = {"no":1,"name":"홍길동","total":300,"avg":100}
# print(stu.keys())
# # 결과값은 dict_keys(['no', 'name', 'total', 'avg'])
# print(stu.values())
# # 결과값은 dict_values([1, '홍길동', 300, 100]) *이건 리스트가 아니므로 아래처럼 리스트로 바꿔서 사용해야

# s_list = list(stu.values())
# print(s_list)
# # 결과값은 [1, '홍길동', 300, 100]

# print(stu.items())
# # 결과값은 dict_items([('no', 1), ('name', '홍길동'), ('total', 300), ('avg', 100)])



# # 딕셔너리 예제
# for i, v in stu.items() :
#     print(i,":", v)

# # 결과값은
# # no : 1
# # name : 홍길동
# # total : 300
# # avg : 100



name_dic = {
    "aaa" : "토마토", "ddd" : "포도", "bbb" : "바나나", "ccc" : "딸기"
}

name_sort1 = []
# import operator
# name_sort1 = sorted(name_dic.items(), key=operator.itemgetter(0))
name_sort1 = sorted(name_dic.items(), key=lambda x:x[0])
print(name_sort1)
# 결과값은 [('aaa', '토마토'), ('bbb', '바나나'), ('ccc', '딸기'), ('ddd', '포도')]

name_sort1 = sorted(name_dic.items(), key=lambda x:x[0], reverse=True)
print(name_sort1)
# 결과값은 [('ddd', '포도'), ('ccc', '딸기'), ('bbb', '바나나'), ('aaa', '토마토')]


