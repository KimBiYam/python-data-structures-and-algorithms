def reverser(string, p1=0, p2=None):
    if len(string) < 2:
        return string
    p2 = p2 or len(string)-1
    while p1 < p2:
        string[p1], string[p2] = string[p2], string[p1]
        p1 += 1
        p2 -= 1


def reversing_words_setence_logic(string):
    reverser(string)
    print(string)
    p = 0
    start = 0
    while p < len(string):
        if string[p] == u"\u0020":
            reverser(string, start, p-1)
            start = p+1
        p += 1
    reverser(string, start, p-1)
    return "".join(string)


if __name__ == "__main__":
    str1 = "파이썬 알고리즘 정말 재미있다"
    str2 = reversing_words_setence_logic(list(str1))
    # print(str2)
