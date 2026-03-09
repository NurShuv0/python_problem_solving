def all_sum(num1, num2, *numbers):
    print(num1, num2)
    print(numbers)
    sum = 0
    for i in numbers:
        print(i)
        sum += i
    return sum + num1 + num2
sum = all_sum(1,2, 3, 4, 5)
print(sum)