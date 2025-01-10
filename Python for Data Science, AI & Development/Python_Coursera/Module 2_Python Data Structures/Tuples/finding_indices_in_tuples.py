def find_all_indices(tpl, value):
    indices = []
    start = 0
    while True:
        try:
            index = tpl.index(value, start)
            indices.append(index)
            start = index + 1
        except ValueError:
            break
    return indices

data = (1, 2, 3, 2, 4, 2)
print(find_all_indices(data, 2))  # Output: [1, 3, 5]