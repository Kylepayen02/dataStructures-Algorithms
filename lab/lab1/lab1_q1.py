def add_binary(bin_1, bin_2):
    '''
    :param bin_1: STR
    :param bin_2: STR
    :return: value STR
    '''

    # solution 1: convert to integers, add them, then convert back to binary
    # solution 2 (initial method I used) : make both strings the same length, then follow my implementation

    sum = int(bin_1, 2) + int(bin_2, 2)

    if sum == 0:
        return "0"

    result = []

    while sum > 0.5:
        res = int(sum) % 2
        result.insert(0, str(res))
        sum = sum // 2

    return ''.join(result)

print(add_binary("11","1"))