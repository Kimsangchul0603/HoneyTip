# 목차
# 리스트

# 리스트
x = [1, 2, 3]
x.extend([4, 5, 6]) # 리스트에 리스트 추가, x = [1, 2, 3, 4, 5, 6]
x.append(4) # 리스트에 항목 추가, x = [1, 2, 3, 4]
1 in [1, 2, 3] # 항목 존재 여부, True

# 딕셔너리
dict.get("없는key", "value") # 딕셔너리 내 없는 키의 값을 value로 대체해줌
dict.keys() # key 호출
dict.values() # value 호출
dict.items() # key, value를 튜플로 묶어 리스트로 호출

# defaultdict : 키가 없으면 자동으로 추가해주는 딕셔너리
from collections import defaultdict
