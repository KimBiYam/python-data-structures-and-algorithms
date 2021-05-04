class Symbol(object):
    def __init__(self, value):
        self.value = value

    # __eq__ 메서드만 재정의하면 unhashable 에러가 나오게된다.
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplemented


if __name__ == "__main__":
    x = Symbol("Py")
    y = Symbol("Py")

    symbols = set()
    symbols.add(x)
    symbols.add(y)

    print(f'x is y : {x is y}')
    print(f'x == y : {x == y}')
    print(f'len(symbols) : {len(symbols)}')
