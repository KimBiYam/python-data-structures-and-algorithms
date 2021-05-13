from stack import Stack


def reverse_string_with_stack(string):
    stack = Stack()
    revStr = ""

    for c in string:
        stack.push(c)

    while not stack.isEmpty():
        revStr += stack.pop()

    return revStr


if __name__ == "__main__":
    tmp_string = "버피는 천사다."
    print(tmp_string)
    print(reverse_string_with_stack(tmp_string))
