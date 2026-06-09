def is_different(numbers):

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):

            if numbers[i] == numbers[j]:
                return False

    return True

print(is_different([1, 5, 7, 9]))
print(is_different([2, 4, 5, 5, 7, 9]))