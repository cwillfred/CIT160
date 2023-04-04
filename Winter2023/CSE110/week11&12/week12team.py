with open ('Winter2023/CSE110/books_and_chapters.txt') as books_file:
    max_chapters = 0
    max_data= []
    for line in books_file:
        line = line.strip()
        books_data = line.split(":")
        book = books_data[0]
        chapters = int(books_data[1])
        scripture = books_data[2]
        print(f'Scripture: {scripture}, Book: {book}, chapters: {chapters}')
        if chapters > max_chapters:
            max_chapters = chapters
            max_data = books_data
print(f'The book with the largest number of chapters is {max_data[0]} with {max_data[1]} chapters')