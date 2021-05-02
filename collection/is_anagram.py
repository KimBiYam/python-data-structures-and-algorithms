from collections import Counter


def is_anagram(s1, s2):
    counter = Counter()
    # counter 를 이용해서 각 문자의 갯수를 셈
    for c in s1:
        counter[c] += 1
    for c in s2:
        counter[c] -= 1
    # 하나의 문자라도 일치하지 않는다면(0이 아니면) 두 문자열은 애너그램이 아니게 됨
    for i in counter.values():
        if i:
            return False
    return True


def test_is_anagram():
    s1 = "marina"
    s2 = "aniram"
    assert(is_anagram(s1, s2) is True)
    s1 = "google"
    s2 = "gouglo"
    assert(is_anagram(s1, s2) is False)
    print("Test Pass")


if __name__ == "__main__":
    test_is_anagram()
