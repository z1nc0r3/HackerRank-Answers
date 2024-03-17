b = "RBY_YBR"


def one_unhappy(b):
    for i in b:
        if i != "_" and b.count(i) == 1:
            return True

    return False


def no_space(b):
    empty_list = []
    
    if b.count("_") == 0:
        return True

    return False


def total_unhappy(b):
    count = 0
    list = []

    try:
        for i in range(0, len(b)):
            if b[i] != "_" and (b[i] != b[i - 1] or b[i] != b[i + 1]):
                count += 1
                list.append(i)
    except:
        pass

    return count, list


print(total_unhappy(b))
print(one_unhappy(b))
print(no_space(b))
