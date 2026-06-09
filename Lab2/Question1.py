def remove_adjacent(numbers):
    result = []

    for num in numbers:
        if len(result) == 0 or num != result[-1]:
            result.append(num)

    return result

print(remove_adjacent([1, 1, 2, 2, 3, 3]))