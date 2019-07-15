from copy import deepcopy


def is_alpha(char1):
    return 'A' <= char1 <= 'Z' or 'a' <= char1 <= 'z'


def split_as_subdict(arr):
    ret = {}
    for idx in range(len(arr) - 1):
        if is_alpha(arr[idx]) and is_alpha(arr[idx + 1]):
            key = arr[idx:idx + 2].lower()
            if key not in ret:
                ret[key] = 0
            ret[key] += 1

    return ret


def get_union(a, b):
    union = deepcopy(a)

    for key, val in b.items():
        if key in union:
            union[key] = max(union[key], val)
        else:
            union[key] = val

    return union


def get_intersection(a, b):
    intersection = {}

    for key, val in a.items():
        if key in b:
            intersection[key] = min(val, b[key])

    return intersection


def get_dict_sum(dict1):
    ret = 0
    for val in dict1.values():
        ret += val
    return ret


def safe_divition(val1, val2):
    if val2 == 0:
        return 1

    return val1 / val2


def get_zakard_similarity(a, b):
    subdict_a = split_as_subdict(a)
    subdict_b = split_as_subdict(b)
    union = get_union(subdict_a, subdict_b)
    intersection = get_intersection(subdict_a, subdict_b)
    return int(safe_divition(get_dict_sum(intersection), get_dict_sum(union)) * 65536)


if __name__ == '__main__':
    # print(is_alpha("a"))
    # print(is_alpha("a"))
    # print(split_as_subarray("abc"))
    # print(split_as_subarray("abcd"))
    # print(split_as_subarray("ab+d"))
    # print(split_as_subarray("ab d"))
    # print(split_as_subdict("Abd"))
    # print(split_as_subdict("AbD"))
    a = split_as_subdict("FRANCE")
    b = split_as_subdict("FRENCH")
    # print(a)
    # print(b)
    # print(get_union(a, b))
    # print(get_intersection(a, b))
    print(get_zakard_similarity("FRANCE", "french"))
    print(get_zakard_similarity("handshake", "shake hands"))
    print(get_zakard_similarity("aa1+aa2", "AAAA12"))
    print(get_zakard_similarity("E=M*C^2", "e=m*c^2"))
