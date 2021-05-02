def usual_dict(dict_data):
    newdata = {}
    for k, v in dict_data:
        if k in newdata:
            newdata[k].append(v)
        else:
            newdata[k] = [v]
    return newdata


def setdefault_dict(dict_data):
    newdata = {}
    # setdefault(key,default) : 해당 dictionary에 key 값이 존재하면 해당 값을 리턴, 존재하지 않으면 해당 key의 value로 default 값을 저장
    for k, v in dict_data:
        newdata.setdefault(k, []).append(v)
    return newdata


def test_setdef():
    dict_data = (
        ("key1", "value1"),
        ("key1", "value2"),
        ("key2", "value3"),
        ("key2", "value4"),
        ("key2", "value5"),
    )

    print(usual_dict(dict_data))
    print(setdefault_dict(dict_data))


if __name__ == "__main__":
    test_setdef()
