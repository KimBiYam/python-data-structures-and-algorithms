from collections import defaultdict


def defaultdict_example():
    pairs = {("a", 1), ("b", 2), ("c", 3)}

    # Basic dictionary
    basic_dictionary = {}
    for key, value in pairs:
        if key not in basic_dictionary:
            basic_dictionary[key] = []
        basic_dictionary[key].append(value)
    print(basic_dictionary)

    # defaultdict
    default_dict = defaultdict(list)
    for key, value in pairs:
        default_dict[key].append(value)
    print(default_dict)


if __name__ == "__main__":
    defaultdict_example()
