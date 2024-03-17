import time

s = "asdcbsdcagfsdbgdfanfghbsfdab"
dic = {}
letters = [letter for letter in s]
max_length = 0


def find_distinct():
    dic.clear()
    for letter in letters:
        if letter not in dic.items():
            dic.update({letter: letters.count(letter)})


def remove_consecutive():
    global letters
    while True:
        consecutive = []
        for i in range(len(letters) - 2):
            if letters[i] == letters[i + 1]:
                consecutive.append(letters[i])

        if len(consecutive) == 0:
            return

        letters = [letter for letter in letters if letter not in consecutive]


def remove_singles():
    global letters
    i = 0
    while i < len(letters):
        if letters.count(letters[i]) == 1:
            letters = [letter for letter in letters if letter != letters[i]]
            i = 0  # reset the counter
        else:
            i += 1  # increment the counter


def main():
    global letters
    global max_length
    global dic
    local_letters = letters
    local_dic = dic

    while True:
        local_letters = letters
        remove_consecutive()
        remove_singles()
        find_distinct()
        local_dic = dict(
            sorted(local_dic.items(), key=lambda item: item[1], reverse=True)
        )

        if letters == local_letters:
            dic = local_dic
            print(dic)
            break

    for i in range(len(local_dic) - 1):
        for j in range(i + 1, len(local_dic)):
            temp = letters
            letters = [
                letter
                for letter in letters
                if letter == list(local_dic.keys())[i]
                or letter == list(local_dic.keys())[j]
            ]
            print("start", letters)
            remove_consecutive()
            remove_singles()
            print(list(local_dic.keys())[i], list(local_dic.keys())[j], letters)

            if len(letters) == 0:
                print("NO")
            else:
                if len(letters) > max_length:
                    max_length = len(letters)

            letters = temp


find_distinct()
main()
print(max_length)
