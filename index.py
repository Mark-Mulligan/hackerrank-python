def create_list(x, y, z, n):
    num_1 = 0
    num_2 = 0
    num_3 = 0
    result = []

    while num_1 <= x:
        while num_2 <= y:
            while num_3 <= z:
                if (num_1 + num_2 + num_3) != n:
                    result.append([num_1, num_2, num_3])
                num_3 += 1
            num_3 = 0
            num_2 += 1
        num_2 = 0
        num_1 += 1

    return result


print(create_list(2, 2, 2, 2))
