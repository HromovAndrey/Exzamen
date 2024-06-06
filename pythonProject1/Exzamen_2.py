# . Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.
sum_even = sum(num for num in range(1, 101) if num % 2 == 0)

print(sum_even)
