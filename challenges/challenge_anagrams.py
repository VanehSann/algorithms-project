def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return ("", "", False)

    list_first = list(first_string.lower())
    list_second = list(second_string.lower())

    join_One(list_first)
    join_One(list_second)

    sorted_first = "".join(list_first)
    sorted_second = "".join(list_second)

    return (sorted_first, sorted_second, sorted_first == sorted_second)


def join_One(list, start=0, end=None):
    if end is None:
        end = len(list)
    if (end - start) > 1:
        mid = (start + end) // 2
        join_One(list, start, mid)
        join_One(list, mid, end)
        orderOne(list, start, mid, end)


def orderOne(string, start, mid, end):

    a = string[start:mid]
    b = string[mid:end]

    a_index, b_index = 0, 0

    for ab_index in range(start, end):
        if a_index >= len(a):
            string[ab_index] = b[b_index]
            b_index += 1
        elif b_index >= len(b):
            string[ab_index] = a[a_index]
            a_index += 1
        elif a[a_index] < b[b_index]:
            string[ab_index] = a[a_index]
            a_index += 1
        else:
            string[ab_index] = b[b_index]
            b_index += 1
