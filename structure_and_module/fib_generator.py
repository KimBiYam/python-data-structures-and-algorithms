def fib_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


if __name__ == "__main__":
    fib = fib_generator()

    for i in range(0, 10):
        print(next(fib))
    # for 과 함께 else 를 사용하면 반복문 종료 시 else 절 코드가 실행됨(단 break로 종료시에는 실행 안됨)
    else:
        print("반복문 종료")
