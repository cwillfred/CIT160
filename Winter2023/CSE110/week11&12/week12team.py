max = 0
book_with_max = ""

with open ('Winter2023/CSE110/books_and_chapters.txt') as scripture:
    for line in scripture:
        parts = line.strip()
        book = parts[0].split(':')
        chapters = int(parts[1])
        scripture = parts[2].strip()
        if chapters > max:
            max = chapters
            book_with_max = book
    print(f'The largest number of chapters in the scriptures is {max}')
    print(f'The book with the largest number of chapters is {book_with_max}')