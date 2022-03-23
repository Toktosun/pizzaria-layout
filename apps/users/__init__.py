list(range(1, 101))


even_numbers = []

for number in range(1, 101):
    if number % 2 == 0:
        even_numbers.append(number)

# List comprehension
number_list = [number for number in range(1, 101)]
even_number_list = [number for number in range(1, 101) if number % 2 == 0]
