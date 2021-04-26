print(f'{"-"*20} set add() {"-"*20}')
people = {"버피", "에인절", "자일스"}
people.add("윌로")
print(people)

print(f'{"-"*20} set update() {"-"*20}')
people = {"버피", "에인절", "자일스"}
people.update({"로미오", "줄리엣", "에인절"})
print(people)

print(f'{"-"*20} set union() {"-"*20}')
people = {"버피", "에인절", "자일스"}
print(people.union({"로미오", "줄리엣"}))
print(people | {"브라이언"})

print(f'{"-"*20} set intersection() {"-"*20}')
people = {"버피", "에인절", "자일스", "이안"}
vampires = {"에인절", "자일스", "윌로"}
print(people.intersection(vampires))
print(people & vampires)

print(f'{"-"*20} set difference() {"-"*20}')
people = {"버피", "에인절", "자일스", "아영"}
vampires = {"스파이크", "에인절", "상민"}
print(people.difference(vampires))
print(people - vampires)

print(f'{"-"*20} set clear() {"-"*20}')
people = {"버피", "자일스", "에인절"}
people.clear()
print(people)

print(f'{"-"*20} set discard(), remove(), pop() {"-"*20}')
countries = {"프랑스", "스페인", "영국"}
countries.discard("한국")

# remove 는 해당 값이 없는경우 에러 발생
# countries.remove("일본")

# 무작위 값 삭제
print(countries.pop())
countries.pop()
countries.pop()

# 셋이 비어있으면 에러 발생
countries.pop()
