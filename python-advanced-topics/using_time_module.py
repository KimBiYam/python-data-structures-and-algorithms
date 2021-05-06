import time


def sumOfN2(number: int):
    start = time.time()
    theSum = 0
    for i in range(1, number+1):
        theSum = theSum + i
    end = time.time()
    return theSum, end - start


if __name__ == '__main__':
    number = 5
    print('총 합계: %d\t 시간: %10.7f초' % sumOfN2(number))
    number = 200
    print('총 합계: %d\t 시간: %10.7f초' % sumOfN2(number))
