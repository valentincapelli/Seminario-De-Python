import csv
def without_repeated(route, index):
    "This function returns a list without repeteated elements"
    with open(route, encoding= 'utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        type_list = []

        for line in reader:
            type_list.append(line[index])

    new_list = set(type_list)
    return new_list