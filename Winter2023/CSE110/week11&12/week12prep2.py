max_opening_weekend = 0
max_movie_data = []

with open('Winter2023/CSE110/harry-potter.txt') as movie_file:
    movie_file.readline()
    for line in movie_file:
        line=line.strip()
        movie_data = line.split(',')
        opening_theaters = int(movie_data[4])
        opening_weekend = int(movie_data[3])
        if opening_theaters < 4000:
            if opening_weekend > max_opening_weekend:
               max_opening_weekend = opening_weekend
               max_movie_data = movie_data

print(f'The movie with the highest opening weekend with less than 4000 theaters was {max_movie_data[0]} with ${max_opening_weekend:,} in {max_movie_data[4]} theaters.')