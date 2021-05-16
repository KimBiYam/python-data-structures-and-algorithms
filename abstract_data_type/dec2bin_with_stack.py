from stack import Stack


def dec2bin_with_stack(decnum):
    stack = Stack()
    str_aux = ""

    while decnum > 0:
        dig = decnum % 2
        decnum = decnum // 2
        stack.push(dig)

    while not stack.isEmpty():
        str_aux += str(stack.pop())

    return str_aux


if __name__ == "__main__":
    decnum = 9
    print(dec2bin_with_stack(decnum))
