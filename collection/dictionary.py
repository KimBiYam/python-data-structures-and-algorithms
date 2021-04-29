tarantino = {}
tarantino['name'] = '쿠엔틴 타란티노'
tarantino['job'] = '감독'
print(tarantino)

sunnydale = {"name": "버피", "age": 16, "hobby": "게임"}
print(sunnydale)

sunnydale = dict({"name": "버피", "age": 23, "hobby": "게임"})
print(sunnydale)

sunnydale = dict(name="자일스", age=45, hobby="영화감상")
print(sunnydale)

# 튜플, 리스트안에 값이 두개인 튜플, 리스트가 들어있으면 해당 값들을 key, value로 dictonary를 생성함
sunnydale = dict([("name", "윌로"), ("age", 15), ("hobby", "개발")])
print(sunnydale)

# A.update(B) : A 딕셔너리에 B 딕셔너리의 키가 존재한다면, 기존 A의 (key,value)를 B 딕셔너리의 (key,value)로 갱신.
# B 딕셔너리의 키가 A에 존재하지 않는다면 B의 (key,value)를 A 딕셔너리에 추가
d = {'a': 1, 'b': 2}
d.update({'b': 10})
print(d)

d.update({'c': 100})
print(d)

d.update({'b': 55, 'c': 119, 'd': 22})
print(d)

# A.get(key) : 딕셔너리 A의 key에 해당하는 값을 리턴. key가 존재하지 않으면 리턴이 없다.
sunnydale = dict(name='제인', age=18, hobby='게임')
print(sunnydale.get('hobby'))
print(sunnydale['hobby'])
print(sunnydale.get('hello'))  # None
# print(sunnydale['hello']) - Dictionray[key] 로 접근시에 해당 key가 없는 경우에는 KeyError Exception 발생

# A.items() : 해당 딕셔너리의 아이템을 조회하는 읽기 전용의 반복 가능한 객체를 리턴함
# A.values() : 해당 딕셔너리의 값들을 조회하는 읽기 전용의 반복 가능한 객체를 리턴함
# A.keys() : 해당 딕셔너리의 키들을 조회하는 읽기 전용의 반복 가능한 객체를 리턴함
sunnydale = dict(name="잰더", age=17, hobby="게임")
print(sunnydale.items())
print(sunnydale.values())
print(sunnydale.keys())
sunnydale_copy = sunnydale.items()
# sunnydale_copy['address'] = '서울' - throw Exception
sunnydale['address'] = '서울'
print(sunnydale)

# A.pop(key) : 딕셔너리 A의 key 항목을 제거 후, 그 값을 리턴
# A.popitem() : 딕셔너리 A에서 항목을 제거 후, 그 키와 항목을 리턴
sunnydale = dict(name="잰더", age=17, hobby="게임", address="서울")
print(sunnydale.pop("age"))
print(sunnydale.popitem())
print(sunnydale)

# A.clear() : 딕셔너리의 모든 값을 제거
sunnydale.clear()
print(sunnydale)
