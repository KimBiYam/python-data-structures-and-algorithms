from stack import Stack


def balance_par_str_with_stack(string):
    stack = Stack()
    balanced = True
    index = 0

    while index < len(string) and balanced:
        symbol = string[index]

        if symbol == "(":
            stack.push(symbol)

        else:
            if stack.isEmpty():
                balanced = False
            else:
                stack.pop()

        index += 1

    if balanced and stack.isEmpty():
        return True

    else:
        return False


if __name__ == "__main__":
    print(balance_par_str_with_stack('((()))'))
    print(balance_par_str_with_stack('(()'))
