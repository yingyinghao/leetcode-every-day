def test(num):
    total = 0
    for i in range(num):
        total += i
    return total


# time complexity is O(n)

# O(1)
def O1(num):
    i = num
    j = num*2
    return i+j

# O(logN) 二分查找法


def OlogN(num):
    i = 1
    while i < num:
        i = i*2
    return i

# O(N)


def ON(num):
    total = 0
    for i in range(num):
        total += i
    return total

# O(M+N)


def OMN(num1, num2):
    total = 0
    for i in range(num1):
        total += i
    for j in range(num2):
        total += j
    return total

# O(NlogN) 排序


def ONLOGN(num1, num2):
    total = 0
    j = 0
    for i in range(num1):
        while(j < num2):
            total += i + j
            j = j * 2
    return total

# O(N^2)


def ON2(num):
    total = 0
    for i in range(num):
        for j in range(num):
            total += i + j


# 空间复杂度
# O(1) only have the int type(变量等于常量)
#  o(1) o(n) o(n^2)

def test(num):
    total = 0
    for i in range(num):
        total += i
    return total


def test(nums):
    array = []
    for num in nums:
        array.append(num)
    return array
