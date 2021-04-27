def set_opertaions_with_dict():
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    d1 = dict(pairs)
    print(f"dictionary1\t: {d1}")

    d2 = {"a": 1, "c": 2, "d": 3, "e": 4}
    print(f"dictionary2\t: {d2}")

    intersection = d1.keys() & d2.keys()
    print(f"d1 & d2 (key)\t : {intersection}")

    intersection_items = d1.items() & d2.items()
    print(f"d1 & d2 (key,value)\t : {intersection_items}")

    subtraction1 = d1.keys() - d2.keys()
    print(f"d1 - d2 (key)\t : {subtraction1}")

    subtraction2 = d2.keys() - d1.keys()
    print(f"d2 - d1 (key)\t : {subtraction2}")

    subtraction_items = d1.items() - d2.items()
    print(f"d1 - d2 (key,value)\t : {subtraction_items}")

    print(d2.keys())
    d3 = {key: d2[key] for key in d2.keys() - {"c", "d"}}


if __name__ == "__main__":
    set_opertaions_with_dict()
