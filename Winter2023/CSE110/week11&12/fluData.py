min_life = 9999.99
max_life = 0
max_data = []
min_data = []

with open ('Winter2023/CSE110/life-expectancy.csv') as flu_file:
    for line in flu_file:
        line=line.strip()
        flu_data=line.split(',')
        life = flu_data[3]
        max_life = life
        max_data = flu_data
        min_life = life 
        min_data = flu_data

print (f'The max life expectancy is {max_life}')
print (f'The min life expectancy is {min_life}')
