a = "a14b6fh"
are_all_unique = len(set(a)) == len(a)
print("4. Усі символи унікальні:", are_all_unique)

my_list = [1, 2, 2, 3, 4, 4, 4, 5]
occurrences = {item: my_list.count(item) for item in set(my_list)}
print("5. Кількість повторень елементів у списку:", occurrences)

my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
result = {value for key, value in my_dict.items() if key % 2 == 0}
print("6. Значення з парними ключами:", result)

my_dict = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
filtered_dict = {key: value for key, value in my_dict.items() if not value.startswith('a')}
print("7. Словник після видалення ключів зі значеннями, які починаються з 'а':", filtered_dict)
