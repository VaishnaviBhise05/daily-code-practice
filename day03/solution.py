def find_largest(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest


if __name__ == "__main__":
    print(find_largest([3, 7, 2, 9, 4]))   # 9
    print(find_largest([-5, -1, -10]))     # -1
