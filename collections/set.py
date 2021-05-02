# add : set에 값을 추가
print(f'{"-"*20} set add() {"-"*20}')
people = {"버피", "에인절", "자일스"}
people.add("윌로")
print(people)

# update / |= : 합집합
print(f'{"-"*20} set update() {"-"*20}')
people = {"버피", "에인절", "자일스"}
people.update({"로미오", "줄리엣", "에인절"})
print(people)
people = {"버피", "에인절", "자일스"}
people |= {"리키", "유진"}
print(people)

# union : update와 결과는 같지만 해당 결과값을 리턴함
print(f'{"-"*20} set union() {"-"*20}')
people = {"버피", "에인절", "자일스"}
print(people.union({"로미오", "줄리엣"}))
print(people | {"브라이언"})

# intersection / & : 교집합
print(f'{"-"*20} set intersection() {"-"*20}')
people = {"버피", "에인절", "자일스", "이안"}
vampires = {"에인절", "자일스", "윌로"}
print(people.intersection(vampires))
print(people & vampires)

# difference / - : 차집합
print(f'{"-"*20} set difference() {"-"*20}')
people = {"버피", "에인절", "자일스", "아영"}
vampires = {"스파이크", "에인절", "상민"}
print(people.difference(vampires))
print(people - vampires)

# clear : 초기화
print(f'{"-"*20} set clear() {"-"*20}')
people = {"버피", "자일스", "에인절"}
people.clear()
print(people)

# discard : set의 특정 값을 삭제하며 리턴은 없음
# remove : set의 특정 값을 삭제하며 해당 값이 리턴되며, 해당 값이 set에 없을 경우 예외 발생
print(f'{"-"*20} set discard(), remove(), pop() {"-"*20}')
countries = {"프랑스", "스페인", "영국"}
countries.discard("한국")
# countries.remove("일본") - KeyError exception

# pop : set의 랜덤한 값을 삭제하며, set이 비어있는 경우 예외 발생
print(countries.pop())
countries.pop()
countries.pop()
# countries.pop() - KeyError exception
