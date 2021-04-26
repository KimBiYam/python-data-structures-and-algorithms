people = {"버피", "에인절", "자일스"}
people.add("윌로")
print(people)

people = {"버피", "에인절", "자일스"}
people.update({"로미오", "줄리엣", "에인절"})
print(people)

people = {"버피", "에인절", "자일스"}
print(people.union({"로미오", "줄리엣"}))
print(people | {"브라이언"})
