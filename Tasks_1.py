"""1) A decimal number is called deci - binary if each of its 0 or 1 without any leading zeros.For
example, 101 and 1100 are deci - binary,while 112 and 3001 are not.
Given a string n that represents a positive decimal integer, return the minimum number of
positive deci - binary numbers needed so that they sum up to n.
Example
Input: n = "32"
Explanation: 10 + 11 + 11 = 32"""

n = "345"
n2 = "12"
n3 = "12121"
def minPartitions(n: str) -> list[list]:
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


""" 2) There is a hidden integer array arr that consists of n non-negative integers.
It was encoded into another integer array encoded of length n - 1, such that
encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1],
then encoded = [1,2,3].

You are given the encoded array. You are also given an integer first, that is
the first element of arr, i.e. arr[0].
Return the original array arr. It can be proved that the answer exists and is
unique.

Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]"""


encoded1 = [1, 2, 3]
first1 = 1

encoded2 = [6, 2, 7, 3]
first2 = 4


def decode(encoded: list[int], first: int) -> list[int]:
    decode = []
    decode.append(first)
    for ind, num in enumerate(encoded):
        decode.append(decode[ind] ^ num)
    return decode

print(decode(encoded1, first1))
print(decode(encoded2, first2))


"""You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

Input: n = 7
Output: 6
Explanation: Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6."""

n = 7
n2 = 6
def numberOfMatches(n: int) -> int:

    list_ = []
    while n > 1:
       if n % 2 == 0:
            list_.append(n // 2)
            n = n // 2
       else:
            n = n - 1
            list_.append((n // 2))
            n = ((n // 2) + 1)
    return sum(list_)

print(numberOfMatches(n))
print(numberOfMatches(n2))
