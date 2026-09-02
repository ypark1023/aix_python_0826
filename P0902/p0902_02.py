# 리스트 깊은 복사 vs 얕은 복사

# alist = [1,2,3]
# alist2 = []
# # alist2 = alist        # 얕은 복사
# # alist2 = [*alist]     # 깊은 복사

# print(alist2)



# # 리스트의 count
# aa = ["바나나", "딸기", "사과", "딸기", "딸기", "사과"]
# print(aa.count("바나나"))       # 결과값 1
# print(aa.count("사과"))         # 결과값 2
# print(aa.count("딸기"))         # 결과값 3



# # 딕셔너리
# adic = {"바나나":1, "딸기":3, "사과":2}
# print(adic["바나나"])   #밸류값이 출력됨

# adic["배"] = 5     # 추가
# print(adic)      # 결과값은 {'바나나': 1, '딸기': 3, '사과': 2, '배': 5}

# # del adic["바나나"]  # 삭제
# adic["사과"] = 10
# print(adic)     # 수정 - 결과값은 {'바나나': 1, '딸기': 3, '사과': 10, '배': 5}


# # 딕셔너리 수정
# aa = ["바나나", "딸기", "사과", "딸기", "딸기", "사과"]
# # adic = {"바나나":1, "딸기":3, "사과":2}

# aa_dic = {}
# for a in aa:
#     if a not in aa_dic :
#         aa_dic[a] = 1
#     else : 
#         aa_dic[a] = aa_dic[a]+1
#         print("있음")

# print(aa_dic)


# # 리스트 -> 딕셔너리
# bb = [1,2,3,1,1,1,1,2,3,1,1,1,2,2,3]
# bb_dic = {}

# for b in bb :
#     if b not in bb_dic :
#         bb_dic[b] = 1
#     else : 
#         bb_dic[b] = bb_dic[b]+1

# print(bb_dic)       # 결과값은 {1: 8, 2: 4, 3: 3}

