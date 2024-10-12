numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

item_nan = 4
total = sum(numbers[:item_nan]) + sum(numbers[item_nan + 1:])
count = len(numbers)
average = total / count
numbers[item_nan] = average

print('Измененный список:', numbers)
