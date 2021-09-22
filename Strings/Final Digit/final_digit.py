
'''
    Given a non-negative integer, num repeatedly add all its digits until it has a single digit remaining and return it.

    Ex: Given the following num...

    num = 123, return 6 (1 + 2 + 3 = 6)

    Ex: Given the following num...

    num = 8353, return 1 (8 + 3 + 5 + 3 = 19 = 1 + 9 = 10 = 1 + 0 = 1).
'''

# def add_int(value):
#     # non-negative
#     if value / 10 > 1:
#         value = add_int(sum([int(i) for i in str(value)]))
#     else:
#         return value
#     if value / 10 < 1:
#         return value

# print(add_int(123))