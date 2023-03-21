max_opening_weekend = 0
max_movie_data = []

with open('Winter2023/CSE110/harry-potter.txt') as movie_file:
    movie_file.readline()
    for line in movie_file:
        line=line.strip()
        movie_data = line.split(',')
        opening_weekend = int(movie_data[3])
        if opening_weekend > max_opening_weekend:
            max_opening_weekend = opening_weekend
            max_movie_data = movie_data

print(f'Movie: {max_movie_data[0]}')
print(f'Highest opening weekend was ${max_opening_weekend:,}.')
print(f'Released on {max_movie_data[5]}')
print(f'Lifetime gross of ${int(max_movie_data[1]):,}.')