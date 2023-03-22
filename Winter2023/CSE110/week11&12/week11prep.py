with open ('Winter2023/CSE110/fruits.txt') as fruit_file:
    for line in fruit_file:
        line = line.strip()
        fruit_data = line.split('.')
        fruit_name = fruit_data[0]
        fruit_origin = fruit_data[1]
        print(f'{fruit_name} comes from {fruit_origin}')