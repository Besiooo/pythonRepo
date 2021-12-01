class Diff1:
    data_table = []
    counter = 0
    with open("dec1_txt.txt") as data:
        for line in data.readlines():
            data_table.append(int(line))

    for index, num in enumerate(data_table):
        try:
            if data_table[index + 1] > data_table[index]:
                counter += 1
        except IndexError:
            print(f"decreases in depth: {counter}")


def sum_little(table, i):
    return table[i] + table[i + 1] + table[i + 2]


class Diff2:
    data_table = []
    counter = 0
    with open("dec1_txt.txt") as data:
        for line in data.readlines():
            data_table.append(int(line))

    for index, num in enumerate(data_table):
        try:
            if sum_little(data_table, index + 1) > sum_little(data_table, index):
                counter += 1
        except IndexError:
            print(f"decreases in sumaric depth: {counter}")
            break


Diff1()
Diff2()