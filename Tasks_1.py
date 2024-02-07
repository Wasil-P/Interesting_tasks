# A decimal number is called deci - binary if each of its 0 or 1 without any leading zeros.For
# example, 101 and 1100 are deci - binary,while 112 and 3001 are not.
# Given a string n that represents a positive decimal integer, return the minimum number of
# positive deci - binary numbers needed so that they sum up to n.
# Example
# Input: n = "32"
# Explanation: 10 + 11 + 11 = 32

n = "345"
n2 = "12"
n3 = "12121"
def minPartitions(n):
    new_list = [int(num) for num in n]
    num_big = max(new_list)
    total_list = [[] for _ in range(num_big)]
    for num in new_list:
        ind_num = num - 1
        for list_ in total_list:
            if ind_num < 0:
                list_.append(0)
            else:
                list_.append(1)
            ind_num -= 1

    total_list = [[int(''.join(map(str, sublist)))] for sublist in total_list]
    return total_list

print(minPartitions(n))
print(minPartitions(n2))
print(minPartitions(n3))