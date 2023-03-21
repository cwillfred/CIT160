print('Here is the list of Harry Potter movies released in July.')
print('===================================')

with open ('Winter2023/CSE110/harry-potter.txt') as movie_file:
    movie_file.readline()
    for line in movie_file:
        line = line.strip()
        movie_data = line.split(',')
        release_date_parts = movie_data[5].split(' ')
        if release_date_parts[0] == 'Jul':
            print(f'{movie_data[0]} was released on {movie_data[5]}')