from collections import Counter, defaultdict


def find_dice_probabilities(target, dice_faces=6):
    if target > 2 * dice_faces or target < 2:
        return None

    counter = Counter()
    default_dict = defaultdict(list)

    for dice1 in range(1, dice_faces+1):
        for dice2 in range(1, dice_faces+1):
            t = [dice1, dice2]
            counter[dice1+dice2] += 1
            default_dict[dice1+dice2].append(t)

    return [counter[target], default_dict[target]]


def test_find_dice_probabilities():
    dice_faces = 6
    target = 5
    results = find_dice_probabilities(target, dice_faces)
    print(results)
    assert(results[0] == len(results[1]))
    print("Test Pass")


if __name__ == "__main__":
    test_find_dice_probabilities()
