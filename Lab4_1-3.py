A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}

result = A - B
print("1. Елементи A, яких немає в B:", result)

common_elements = A.intersection(B)
print("2. Спільні елементи A та B:", common_elements)

union_set = A.union(B)
print("3. Об'єднання множин A та B:", union_set)