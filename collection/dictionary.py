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
