from collections import OrderedDict


def orderedDict_example():
    pairs = [("c", 1), ("b", 2), ("a", 3)]

    # Basic dictionary
    basic_dictionary = {}
    for key, value in pairs:
        if key not in basic_dictionary:
            basic_dictionary[key] = []
        basic_dictionary[key].append(value)
    for key in basic_dictionary:
        print(key, basic_dictionary[key])

    # OrderedDict
    orderedDict = OrderedDict(pairs)
    for key in orderedDict:
        print(key, orderedDict[key])


if __name__ == "__main__":
    orderedDict_example()
