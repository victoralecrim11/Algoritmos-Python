x = [6, 3, 2, 1, 9]

min_value = None

for array in x:
    if (min_value is None or array < min_value):
        min_value = array

print("min_value:", min_value)
