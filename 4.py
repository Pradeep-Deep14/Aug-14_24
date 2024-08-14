input_list = ['apple,orange', 'banana,grape', 'watermelon']

# Splitting and printing each item
for item in input_list:
    for fruit in item.split(','):
        print(fruit)