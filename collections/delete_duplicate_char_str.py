import string


def delete_duplicate_word(str):
    alphabet_table = {key: 0 for key in string.ascii_lowercase}
    for i in str:
        alphabet_table[i] += 1
    for key, value in alphabet_table.items():
        if value > 1:
            str = str.replace(key, "")
    return str


def test_delete_duplicate_word():
    str = 'google'
    assert(delete_duplicate_word(str) == 'le')
    print("Test Pass")


if __name__ == "__main__":
    test_delete_duplicate_word()
