import string


def hash_func(astring):
    s = 0
    for one in astring:
        if one in string.whitespace:
            continue
        # ord() : 인수가 유니코드 객체일 때, 문자의 유니코드를 나타내는 정수를 리턴하고,
        # 인수가 8비트 문자열인 경우 바이트 값을 반환한다.
        s = s + ord(one)
    return s


def find_anagram_hash_function(word1, word2):
    return hash_func(word1) == hash_func(word2)


def test_find_anagram_hash_function():
    word1 = "buffy"
    word2 = "bffyu"
    word3 = "bffya"
    assert(find_anagram_hash_function(word1, word2) is True)
    assert(find_anagram_hash_function(word1, word3) is False)

    # find_anagram_hash_function 함수에서 양쪽 문자의 바이트값을 비교하기 때문에
    # 애너그램 외에도 단순히 서로 바이트 값이 같은 경우에도 애너그램으로 인식되는 문제가 있음
    word1 = "aad"
    word2 = "bca"
    assert(find_anagram_hash_function(word1, word2) is True)
    print("Test Pass")


if __name__ == "__main__":
    test_find_anagram_hash_function()
