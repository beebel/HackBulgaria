def hash_them(keys, values):
    result = {}
    i = 0
    for i in range(len(keys)):
        if i >= len(values):
            result[keys[i]] = None
        else:
            result[keys[i]] = values[i]

    return result


keys = ["Ivan", "Maria"]
values = [1, 2]
print(hash_them(keys, values))
