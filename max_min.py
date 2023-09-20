numbers = [3, 1, 3, 5, 6, 123, 5, 61]
min = numbers[0]
max = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max:
      max = numbers[i]
    elif numbers[i] < min:
      min = numbers[i]

print("min:", min)
print("max", max)